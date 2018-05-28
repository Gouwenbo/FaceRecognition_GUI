#-*- coding:utf-8 -*-
#rtsp://admin:@10.128.24.71:554/stream1
import sys
import time
import PIL.Image, PIL.ImageDraw, PIL.ImageFont,cv2
import os
import sys
import time
import re
import pymysql
import mxnet as mx
import Queue
from collections import Counter
import ConfigParser
import pyqtgraph as pg
import face_embedding
import datetime
from scipy import misc
import numpy as np
import base64
##mxnet-mtcnn
from core.symbol import P_Net, R_Net, O_Net
from core.imdb import IMDB
from core.config import config
from core.loader import TestLoader
from core.detector import Detector
from core.fcn_detector import FcnDetector
from tools.load_model import load_param
from core.MtcnnDetector import MtcnnDetector


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog 
from PyQt5.QtGui import QPixmap, QImage ,QKeyEvent,QStandardItemModel,QStandardItem
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt, QTimer
##ui
from ui.login import Ui_Dialog
from ui.manager_user import Ui_ManagerUser_Dialog
from ui.ManagerWindow import Ui_MainWindow
from ui.search_log import Ui_Searchlog_Dialog
try:  
    _fromUtf8 = QtCore.QString.fromUtf8  
except AttributeError:  
    def _fromUtf8(s):  
        return s 

class Arg_Data():
    def __init__(self,id_dir,model):
        self.image_size=[112,112]
        self.gpu=0
        self.det=5
        self.flip=0
        self.threshold=1.24
        self.model = model
        self.id_dir =id_dir

class ID_Data():
    def __init__(self, name, image_path,emb):
        self.name = name
        self.image_path = image_path
        self.embedding = emb

class ImageClass():
    "Stores the paths to images for a given class"
    def __init__(self, name, image_paths):
        self.name = name
        self.image_paths = image_paths
  
    def __str__(self):
        return self.name + ', ' + str(len(self.image_paths)) + ' images'
  
    def __len__(self):
        return len(self.image_paths)
  
class Box_id():
    def __init__(self,id_num,box,label):
        self.id_num = -1
        self.bbox= []
        self.labels = []
        self.id_num = id_num
        self.bbox.append(box)
        self.labels.append(label)
        self.releasenum = 10
        self.islog = False
    def add_box (self,box):
        if len(self.bbox)<=10:
            self.bbox.insert(0,box)
        else:
            temp = self.bbox.pop()
            self.bbox.insert(0,box)
    def add_label (self,label):
        if len(self.labels)<=10:
            self.labels.insert(0,label)
        else:
            temp = self.labels.pop()
            self.labels.insert(0,label)

class loginWindow(Ui_Dialog):
    def __init__(self, parent=None):
        super(loginWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.clearinput)
        
    def clearinput(self):
        self.textEdit_username.setText("")
        self.textEdit_userpasswd.setText("")

    def encodePsd(self, psd):
        bpsd = base64.b64encode(bytes(psd))
        return str(bpsd)
    def login(self):
        username = self.textEdit_username.text()
        userpwd = self.textEdit_userpasswd.text()
        db = pymysql.connect("localhost","root","root","sys",charset='utf8')
        cursor = db.cursor()
        sql = "select * from Users where idUsers='%s'" % (username)
        if cursor.execute(sql):
            data = cursor.fetchone()
            db.close()
            if self.encodePsd(userpwd) == data[2]:
                if data[3] == 'teacher':
                    self.managerWindow = managerWindow()
                    self.managerWindow.show()
                    self.close()
            else:
                QMessageBox.warning(self, ("警告"), ("\n密码错误!"))
        else:
            QMessageBox.warning(self, ("警告"), ("\n用户名错误!"))

class managerWindow(Ui_MainWindow):
    def __init__(self):
        super(managerWindow, self).__init__()
        self.setupUi(self)
        self.setlcd()
        ##
        self.pushButton_selectid.clicked.connect(lambda: self.folder_msg(1))
        self.pushButton_selectmodel.clicked.connect(lambda: self.folder_msg(2))

        
        self.pushButton_renamefloder.clicked.connect(lambda:self.progressBar_msg(1))
        self.pushButton_resizeimage.clicked.connect(lambda:self.progressBar_msg(2))
        ##
        
        self.pushButton_loadmodel.clicked.connect(lambda:self.progressBar_msg(4))
        self.pushButton_opencam.clicked.connect(lambda:self.progressBar_msg(5))
        self.pushButton_closecam.clicked.connect(lambda:self.progressBar_msg(6))
        ##
        self.radioButton.toggled.connect(lambda:self.camnum_meg(0))
        self.radioButton_2.toggled.connect(lambda:self.camnum_meg(1))
        self.radioButton_3.toggled.connect(lambda:self.camnum_meg(2))
        self.radioButton_4.toggled.connect(lambda:self.camnum_meg(3))
        
        ##
        self.checkBox_fps.stateChanged.connect(lambda:self.checkbox_meg(1))
        self.checkBox_box.stateChanged.connect(lambda:self.checkbox_meg(2))
        self.checkBox_id.stateChanged.connect(lambda:self.checkbox_meg(3))
        self.checkBox_landmarls.stateChanged.connect(lambda:self.checkbox_meg(4))
        self.checkBox_distance.stateChanged.connect(lambda:self.checkbox_meg(5))
        
        ##
        self.photo_match_id = []
        self.img_paths =[]
        self.photo_bbox=[]
        self.photo_currentindex=-1
        self.photo_dis =[]
        self.ret_dis = []
        self.camnum = 0
        self.modelcreat =False
        self.boxid  = []
        self.boxidnum = 0
        self.show_landmarks = False
        self.show_bb = False
        self.show_id = False
        self.show_fps = False
        self.show_distence= False
        self.font = cv2.FONT_HERSHEY_SIMPLEX

        self.pushButton_4.clicked.connect(self.show_manager_user)
        self.pushButton_7.clicked.connect(self.show_searchlog)
    def mat_inter(self,box1,box2):  
        # 判断两个矩形是否相交  
        # box=(xA,yA,xB,yB)  
        x01, y01, x02, y02 = box1  
        x11, y11, x12, y12 = box2  
      
        lx = abs((x01 + x02) / 2 - (x11 + x12) / 2)  
        ly = abs((y01 + y02) / 2 - (y11 + y12) / 2)  
        sax = abs(x01 - x02)  
        sbx = abs(x11 - x12)  
        say = abs(y01 - y02)  
        sby = abs(y11 - y12)  
        if lx <= (sax + sbx) / 2 and ly <= (say + sby) / 2:  
            return True  
        else:  
            return False  
      
    def solve_coincide(self,box1,box2):  
        # box=(xA,yA,xB,yB)  
        # 计算两个矩形框的重合度  
        if self.mat_inter(box1,box2)==True:  
            x01, y01, x02, y02 = box1  
            x11, y11, x12, y12 = box2  
            col=min(x02,x12)-max(x01,x11)  
            row=min(y02,y12)-max(y01,y11)  
            intersection=col*row  
            area1=(x02-x01)*(y02-y01)  
            area2=(x12-x11)*(y12-y11)  
            coincide=intersection/((area1+area2-intersection)*1.0)
            return coincide  
        else:  
            return False  
    def detect_boxid(self,box,label):
        result = False
        for item in self.boxid:
            tempbox = item.bbox[0]
            bb = [int(tempbox[0]),int(tempbox[1]),int(tempbox[2]),int(tempbox[3])]
            bb2 = [int(box[0]),int(box[1]),int(box[2]),int(box[3])]
            coincide = self.solve_coincide(bb,bb2)
            #print(coincide)
            if coincide > 0.618:
                result = True
                item.add_box(box)
                item.add_label(label)
                result_id = item.id_num
                item.releasenum+=2
                if len(item.labels)>=10:
                    c = Counter(item.labels)
                    result_label = c.most_common()[0][0]
                #print(result_label)
                    return result,result_id,result_label,self.boxid.index(item)
                else:
                    return result,result_id,"Null",self.boxid.index(item)
        return result,0,0,-1
    def setlcd(self):
        db = pymysql.connect("localhost","root","root","sys",charset='utf8')
        cursor = db.cursor()
        sql = "select * from Users where levUsers not like \'teacher\'"
        if cursor.execute(sql):
            data = cursor.fetchall()
            self.lcdNumber.setProperty("intValue", int(len(data)))
    def show_manager_user(self):
        self.manager_userWindow = manager_userWindow()
        QMessageBox.warning(self, ("操作说明"), ("\n根据提示添加用户信息\n 删除用户可根据： \n 用户ID \n 用户姓名\n 二选一 \n"))
        self.manager_userWindow.exec_()
    def show_searchlog(self):
        self.searchlog_Window = searchlog_Window()
        QMessageBox.warning(self, ("操作说明"), ("\n根据提示查询信息\n 查询考勤可根据： \n 用户ID \n 用户姓名\n 二选一 \n"))
        self.searchlog_Window.exec_()
    def folder_msg(self,n):    #文件夹按钮响应函数
        if n==1:
            directory = QFileDialog.getExistingDirectory(None,"选取ID文件夹",  "/home") 
            self.label_idfolder.setText(directory)
        if n==2:
            directory = QFileDialog.getExistingDirectory(None,"选取模型文件夹",  "/home") 
            self.label_modelfolder.setText(directory)
            
    def checkbox_meg(self,n):
        if n==1:
            if self.checkBox_fps.isChecked():
                self.show_fps = True
            else:
                self.show_fps = False
        if n==2:
            if self.checkBox_box.isChecked():
                self.show_bb = True
            else:
                self.show_bb = False
        if n==3:
            if self.checkBox_id.isChecked():
                self.show_id = True
            else:
                self.show_id = False
        if n==4:
            if self.checkBox_landmarls.isChecked():
                self.show_landmarks = True
            else:
                self.show_landmarks = False
        if n==5:
            if self.checkBox_distance.isChecked():
                self.show_distence = True
            else:
                self.show_distence = False

    def progressBar_msg(self,n): 
        if n==1:
            self.progressBar.setValue(0)
            if self.label_idfolder.text()!="":
                self.rename(self.label_idfolder.text())
            else:
                button=QMessageBox.warning(self, '警告',"目录尚未选择", QMessageBox.Yes)
        if n==2:  #resize images
            self.progressBar.setValue(0)
            
    
        if n==4:
            self.progressBar.setValue(0)
            if self.label_idfolder.text()!=""  and self.label_modelfolder.text()!="":
                self.args = Arg_Data(self.label_idfolder.text(),self.label_modelfolder.text()+'/model,0')
                self.loadModel()
                self.modelcreat = True
            else:
                button=QMessageBox.warning(self, '警告',"目录尚未选择", QMessageBox.Yes)
        if n==5:
            self.timer = QTimer()
            self.timer.setInterval(100)
            self.start(self.camnum)
        if n==6:
            self.closecap()
    def camnum_meg(self,n):
        if n == 0:
            if self.radioButton.isChecked():
                self.camnum = 0
            else:
                self.camnum = -1
        if n == 1:
            if self.radioButton_2.isChecked():
                self.camnum = 1
            else:
                self.camnum = -1
        if n == 2:
            if self.radioButton_3.isChecked():
                self.camnum = 2
            else:
                self.camnum = -1
        if n == 3:
            if self.radioButton_4.isChecked():
                self.camnum = 3
            else:
                self.camnum = -1
    def closecap(self):
        self.cap.release()
        self.boxid =[]
        self.boxidnum = 0
        self.label_video.setText("视频画面")
        
    def start(self,camnum):
        if self.modelcreat:
            #self.image_verify()
            if self.camnum !=-1 and  self.lineEdit.text() =="":
                devices = '/dev/video'+str(camnum)
                self.cap = cv2.VideoCapture(devices)
            else :
                devices = self.lineEdit.text()
                self.cap = cv2.VideoCapture(devices)
            self.timer.start()
            self.timer.timeout.connect(self.video_verify)    
        else:
            button=QMessageBox.warning(self, '警告',"模型没有建立", QMessageBox.Yes)
    
    def loadModel(self):
        self.model = face_embedding.FaceModel(self.args)
        detectors = [None, None, None]
        ctx = mx.gpu(0)
        prefix=['mtcnnmodel/pnet', 'mtcnnmodel/rnet', 'mtcnnmodel/onet']
        epoch = [16,16,16]
        batch_size = [2048, 256, 16]
        thresh=[0.6, 0.6, 0.7]
        min_face_size=24
        stride=2
        slide_window=False
        # load pnet model
        args, auxs = load_param(prefix[0], epoch[0], convert=True, ctx=ctx)
        if slide_window:
            PNet = Detector(P_Net("test"), 12, batch_size[0], ctx, args, auxs)
        else:
            PNet = FcnDetector(P_Net("test"), ctx, args, auxs)
        detectors[0] = PNet

        # load rnet model
        args, auxs = load_param(prefix[1], epoch[0], convert=True, ctx=ctx)
        RNet = Detector(R_Net("test"), 24, batch_size[1], ctx, args, auxs)
        detectors[1] = RNet

        # load onet model
        args, auxs = load_param(prefix[2], epoch[2], convert=True, ctx=ctx)
        ONet = Detector(O_Net("test"), 48, batch_size[2], ctx, args, auxs)
        detectors[2] = ONet

        self.mtcnn_detector = MtcnnDetector(detectors=detectors, ctx=ctx, min_face_size=min_face_size,
                                       stride=stride, threshold=thresh, slide_window=slide_window)
        #print (self.model)
        self.id_dataset ,self.idnums = self.get_id_data(self.args.id_dir)
        
    def find_matching_id(self, embedding):
        threshold = 1.12  #1.1 if dist less than this ,believe person id
        min_dist = 10.0  #10.0
        matching_id = 'Unkown'
        for id_data in self.id_dataset :
            if id_data.embedding is not None:
                dist = self.get_embedding_distance(id_data.embedding, embedding)

                if dist < threshold and dist < min_dist:
                #if dist < threshold :
                    min_dist = dist
                    matching_id = id_data.name
            #return matching_id, min_dist
        return matching_id, min_dist

    def get_embedding_distance(self,emb1, emb2):
        dist = np.sqrt(np.sum(np.square(np.subtract(emb1, emb2)))) #Euclodean distence
        return dist

    def get_id_data(self,id_folder):
        id_dataset = []
        ids = os.listdir(os.path.expanduser(id_folder))
        ids.sort()
        for i in range(len(ids)):
            id_dir = os.path.join(id_folder, ids[i])
            image_names = os.listdir(id_dir)
            image_paths = [os.path.join(id_dir, img) for img in image_names]
            for image_path in image_paths:
                #print image_path
                self.progressBar.setValue(i/len(ids))
                
                img = cv2.imread(image_path.encode('utf-8'))
                boxes, boxes_c = self.mtcnn_detector.detect_pnet(img)
                if boxes_c is not None:
                    boxes, boxes_c = self.mtcnn_detector.detect_rnet(img, boxes_c)
                if boxes_c is not None:
                    boxes, boxes_c = self.mtcnn_detector.detect_onet(img, boxes_c)
                if boxes_c is not None: 
                    for b in boxes_c:
                        bb = [int(b[0]),int(b[1]),int(b[2]),int(b[3])]
                        #cv2.rectangle(img, (int(b[0]), int(b[1])), (int(b[2]), int(b[3])), (0, 255, 255), 1)
                        temp_img  = img[int(b[1]):int(b[3]),int(b[0]):int(b[2])]
                        f1,_,_ = self.model.get_feature(temp_img)
                        #print f1
                        id_dataset.append(ID_Data(ids[i], image_path,f1))
        self.progressBar.setValue(100)
        return id_dataset ,len(ids)       ##
    def video_verify(self):  #视频检测
        if (self.cap.isOpened()):
            fla, img = self.cap.read()
            frame_height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            start = time.time()
            acc_box_id = -1
            fonts = PIL.ImageFont.truetype("./fonts/simhei.ttf", 20, encoding="utf-8") 
            if fla:
                img = cv2.resize(img,(840,560))
                frame = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) ##第一次预检测
                boxes, boxes_c = self.mtcnn_detector.detect_pnet(img)
                if boxes_c is not None:
                    boxes, boxes_c = self.mtcnn_detector.detect_rnet(img, boxes_c)
                if boxes_c is not None:
                    boxes, boxes_c = self.mtcnn_detector.detect_onet(img, boxes_c)
                if boxes_c is not None:
                    for b in boxes_c:
                        bb = [int(b[0]),int(b[1]),int(b[2]),int(b[3])]
                        #cv2.rectangle(img, (int(b[0]), int(b[1])), (int(b[2]), int(b[3])), (0, 255, 255), 1)
                        temp_img  = frame[int(b[1]):int(b[3]),int(b[0]):int(b[2])]
                        f,bbox,points = self.model.get_feature(temp_img)
                        
                        self.pil_im = PIL.Image.fromarray(frame)
                        draw = PIL.ImageDraw.Draw(self.pil_im) # 括号中为需要打印的canvas，这里就是在图片上直接打印

                        matching_id ='Unkown'
                        dist = self.args.threshold
                        if f is not None:
                            matching_id, dist = self.find_matching_id(f)
                            ret = self.detect_boxid(b,matching_id)
                            if ret[0] == False:
                                self.boxidnum +=1
                                tempitem = Box_id(self.boxidnum,b,matching_id)
                                self.boxid.append(tempitem)
                            else:
                                matching_id = ret[2]
                                acc_box_id = ret[1]
                                index = ret[3]
                                if self.boxid[index].islog:
                                    self.label_18.setText("已录入成功")
                                else:
                                    if matching_id =="Null":
                                        self.label_18.setText("识别中")
                                    else:
                                        if self.addlog2dataset(matching_id) :
                                            self.label_18.setText("录入成功")
                                            self.boxid[index].islog = True
                                        else:
                                            self.label_18.setText("录入失败")
                            self.label_16.setText(matching_id.encode('utf-8'))
                            if self.show_id:
                                #cv2.putText(img, matching_id.encode('utf-8'), (bb[0], bb[3]), self.font, 1, (255, 255, 255), 1, cv2.LINE_AA) #white
                                draw.text((bb[0], bb[3]), matching_id, (255, 255, 255), font=fonts) 
                                #self.label_16.setText(matching_id.encode('utf-8'))  
                                img = cv2.cvtColor(np.array(self.pil_im), cv2.COLOR_RGB2BGR)
                                #cv2.putText(img, acc_matching_id, (bb[0], bb[3]), self.font, 1, (255, 255, 255), 1, cv2.LINE_AA) #white
                            if self.show_bb:
                                cv2.rectangle(img, (bb[0], bb[1]), (bb[2], bb[3]), (255, 0, 0), 2)
                                cv2.putText(img, 'BOX_ID: %d' %(acc_box_id), (int(bb[0]+5), int(bb[1])), self.font,0.5, (255, 255, 255), 1)
                            if self.show_distence:
                                cv2.putText(img, '%.3f'%dist, (int(bb[0]), int(bb[1])+20), self.font, 0.4, (255, 255, 255), 1)
                            if self.show_landmarks:
                                for j in range(5): # 0: righteye 1:lefteye 2:nose 3:rightmouth 4:leftmouth
                                    cv2.circle(img, (bb[0]+points[j][0], bb[1]+points[j][1]), 1, (0, 0, 255), 2)
                end = time.time()
                seconds = end - start
                fps = round(1 / seconds, 2)
                if self.show_fps:
                    cv2.putText(img, str(fps), (0, int(frame_height) - 5), self.font, 1, (255, 255, 255), 1, cv2.LINE_AA)
                        #out.write(img)
                    height, width, bytesPerComponent = img.shape
                    bytesPerLine = 3 * width
                    cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
                    QImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
                    pixmap = QPixmap.fromImage(QImg)
                    self.label_video.setPixmap(pixmap)
                else:
                    for item in self.boxid:
                        item.releasenum-=1
                        if item.releasenum <=0:
                            self.boxid.remove(item)
                            if len(self.boxid) == 0:
                                self.boxidnum = 0
                    height, width, bytesPerComponent = img.shape
                    bytesPerLine = 3 * width
                    cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
                    QImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
                    pixmap = QPixmap.fromImage(QImg)
                    self.label_video.setPixmap(pixmap)
    def addlog2dataset(self,name):
        db = pymysql.connect("localhost","root","root","sys",charset='utf8')
        cursor = db.cursor()
        sql = "select * from Users where nameUsers = \'%s\'" %(name)
        if cursor.execute(sql):
            data = cursor.fetchone()
            userid = data[0]
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            neartime = (datetime.datetime.now() - datetime.timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S")
            
            sqlnear = "select * from Log where nameLog = \'%s\' and timeLog >= \'%s\'"%(name,neartime)
            print (sqlnear)
            if cursor.execute(sqlnear):
                return True
            else:
                sql2 = "insert into Log(idLog,nameLog,timeLog) values(%d,\'%s\',\'%s\')"%(userid,name,time)
                if cursor.execute(sql2):
                    db.commit()
                    db.close()
                    return True
                else:
                    db.close()
                    return False
        else:
            db.close()
            return False
    def rename(self,dirs):
        image_rename_paths = []
        image_paths = []
        ids = os.listdir(os.path.expanduser(dirs))
        for id_name in ids:
            id_dir = os.path.join(dirs, id_name)
            if os.path.isdir(id_dir):
                #print(os.path.isdir(id_dir))
                image_names = os.listdir(id_dir)
                for img in image_names:
                    image_paths.append(os.path.join(id_dir, img).encode('utf-8'))
            else:
                continue
            filecount = 0
            for img in image_names:
                filecount = filecount+1
                filename = id_name+'_'+'%04d' %(filecount)+'.png'
                image_rename_paths.append(os.path.join(id_dir, filename.encode('utf-8')))
        for i in range(len(image_paths)):
            os.rename(image_paths[i],image_rename_paths[i])
            self.progressBar.setValue(i*100/len(image_paths))
        self.progressBar.setValue(100)

class searchlog_Window(Ui_Searchlog_Dialog):
    def __init__(self):
        super(searchlog_Window, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Searchlog)

        self.data = []
        self.acdata = []
    def keyPressEvent(self, event):
        keyevent = QKeyEvent(event)
        if keyevent == Qt.Key_Enter:
            self.focusNextChild()
    def Searchlog(self):
        idnum = self.lineEdit.text()
        name = self.lineEdit_2.text()
        startday = self.dateEdit.date()
        endday = self.dateEdit_2.date()
        if startday > endday:
            QMessageBox.warning(self, ("提示"), ("\n起始日期大于结束日期"))
        self.amstime = self.timeEdit.time()
        self.ametime = self.timeEdit_2.time()
        self.pmstime = self.timeEdit_3.time()
        self.pmetime = self.timeEdit_4.time()
        if self.amstime > self.ametime or self.pmstime > self.pmetime:
            QMessageBox.warning(self, ("提示"), ("\n起始时间大于结束时间"))
        self.reflashlist(idnum,name,startday,endday)
    def qtimetotime(self,qtime):
        return datetime.datetime.strptime(qtime.toString(Qt.ISODate), "%H:%M:%S")
    def reflashlist(self,idnum,name,startday,endday):
        self.label_lognum.setText("null")
        self.label_logacnum.setText("null")
        self.data = []
        self.acdata = []
        sql = ""
        model = QStandardItemModel()
        model.setColumnCount(3) 
        model.setHorizontalHeaderLabels(['ID','姓名','考勤时间'])
        db = pymysql.connect("localhost","root","root","sys",charset='utf8')
        cursor = db.cursor()
        if idnum !="":
            sql = "select * from Log where idLog = %d and timeLog >= \'%s\'and timeLog <= \'%s\'"%(int(idnum),startday.toString(Qt.ISODate),endday.toString(Qt.ISODate))
            #print (sql)
        elif name !="":
            sql = "select * from Log where nameLog = \'%s\' and timeLog >= \'%s\'and timeLog <= \'%s\' "%(name,startday.toString(Qt.ISODate),endday.toString(Qt.ISODate))
        elif idnum !="" and name !="":
            sql = "select * from Log where nameLog = \'%s\' and idLog = %d and timeLog >= \'%s\'and timeLog <= \'%s\' "%(name,int(idnum),startday.toString(Qt.ISODate),endday.toString(Qt.ISODate))
        else:
            QMessageBox.warning(self, ("提示"), ("\n未输入用户信息!"))
        if cursor.execute(sql):
            self.data = cursor.fetchall()
            for i in range(len(self.data)):
                if (self.data[i][2].time()>= self.qtimetotime(self.amstime).time() and self.data[i][2].time()<=self.qtimetotime(self.ametime).time()) or (self.data[i][2].time()>=self.qtimetotime(self.pmstime).time() and self.data[i][2].time()<=self.qtimetotime(self.pmetime).time()):
                    self.acdata.append(self.data[i])
                item1 = QStandardItem(str(self.data[i][0]))
                item1.setTextAlignment(QtCore.Qt.AlignCenter)
                item2 = QStandardItem(_fromUtf8(self.data[i][1]))
                item2.setTextAlignment(QtCore.Qt.AlignCenter)
                item3 = QStandardItem(self.data[i][2].strftime("%Y-%m-%d %H:%M:%S"))
                item3.setTextAlignment(QtCore.Qt.AlignCenter)
                model.setItem(i, 0, item1)
                model.setItem(i, 1, item2)
                model.setItem(i, 2, item3)
            self.label_lognum.setText(str(len(self.data)))
            self.label_logacnum.setText(str(len(self.acdata)))
        self.tableView.setModel(model)
        self.tableView.setColumnWidth(0,120)
        self.tableView.setColumnWidth(1,120)
        self.tableView.setColumnWidth(2,355)
        self.tableView.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        self.tableView.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
        self.tableView.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
        db.close()
    def plot_point(self):
        print()
class manager_userWindow(Ui_ManagerUser_Dialog):
    def __init__(self):
        super(manager_userWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.AddUser)
        self.pushButton_2.clicked.connect(self.DeletUser)
        self.radioButton.toggled.connect(lambda:self.radiobuttonmsg(1))
        self.radioButton_2.toggled.connect(lambda:self.radiobuttonmsg(2))
        self.reflashlist()
    def keyPressEvent(self, event):
        keyevent = QKeyEvent(event)
        if keyevent == Qt.Key_Enter:
            self.focusNextChild()
    def reflashlist(self):
        model = QStandardItemModel()
        model.setColumnCount(3) 
        model.setHorizontalHeaderLabels(['ID','姓名','权限'])
        db = pymysql.connect("localhost","root","root","sys",charset='utf8')
        cursor = db.cursor()
        sql = "select * from Users where levUsers not like \'manager\'"
        if cursor.execute(sql):
            data = cursor.fetchall()
            for i in range(len(data)):
                item1 = QStandardItem(str(data[i][0]))
                item1.setTextAlignment(QtCore.Qt.AlignCenter)
                item2 = QStandardItem(_fromUtf8(data[i][1]))
                item2.setTextAlignment(QtCore.Qt.AlignCenter)
                item3 = QStandardItem(_fromUtf8(data[i][3]))
                item3.setTextAlignment(QtCore.Qt.AlignCenter)
                model.setItem(i, 0, item1)
                model.setItem(i, 1, item2)
                model.setItem(i, 2, item3)
        self.tableView.setModel(model)
        db.close()
    def radiobuttonmsg(self,n):
        if n==1:
            if self.radioButton.isChecked():
                self.levUsers = "teacher"
            else:
                self.levUsers = ""
        if n==2:
            if self.radioButton_2.isChecked():
                self.levUsers = "student"
            else:
                self.levUsers = ""
    def AddUser(self):
        db = pymysql.connect("localhost","root","root","sys",charset='utf8')
        cursor = db.cursor()
        self.idUsers = self.textEdit.text()
        self.nameUsers = self.textEdit_2.text()
        self.psdUsers = self.textEdit_3.text()
        if self.idUsers and self.nameUsers and self.psdUsers:
            sql = "insert into Users(idUsers,nameUsers,psdUsers,levUsers) values(%d,\'%s\',\'%s\',\'%s\')"%(int(self.idUsers),self.nameUsers,self.psdUsers,self.levUsers)
            try:
                if cursor.execute(sql):
                    db.commit()
                    QMessageBox.warning(self, ("提示"), ("\n添加用户成功!"))
                else:
                    QMessageBox.warning(self, ("提示"), ("\n添加用户失败!"))
            except:
                QMessageBox.warning(self, ("警告"), ("\n数据库操作失败，请检查用户ID唯一性!"))
        else:
            QMessageBox.warning(self, ("提示"), ("\n未输入用户信息!"))
        db.close()
        self.reflashlist()
    def DeletUser(self):
        self.idUsers = self.textEdit.text()
        self.nameUsers = self.textEdit_2.text()
        db = pymysql.connect("localhost","root","root","sys",charset='utf8')
        cursor = db.cursor()
        
        if self.nameUsers =="" and self.idUsers =="":
            QMessageBox.warning(self, ("提示"), ("\n未输入用户信息!"))
        elif self.idUsers !="" and self.nameUsers =="" :
            sql = "delete from Users where idUsers = %d" %(int(self.idUsers))
            if cursor.execute(sql):
                db.commit()
                QMessageBox.warning(self, ("提示"), ("\n删除用户成功!"))
                
            else:
                QMessageBox.warning(self, ("提示"), ("\n删除用户失败!"))
                db.close()
        elif self.nameUsers!="" and self.idUsers =="":
            sql = "delete from Users where nameUsers = \'%s\'" %(self.nameUsers)
            if cursor.execute(sql):
                db.commit()
                QMessageBox.warning(self, ("提示"), ("\n删除用户成功!"))
                
            else:
                QMessageBox.warning(self, ("提示"), ("\n删除用户失败!"))
                
        else:
            sql = "delete from Users where nameUsers = \'%s\' and idUsers = %d" %(self.nameUsers,int(self.idUsers))
            if cursor.execute(sql):
                db.commit()
                QMessageBox.warning(self, ("提示"), ("\n删除用户成功!"))
                
            else:
                QMessageBox.warning(self, ("提示"), ("\n删除用户失败!"))
        db.close()
        self.reflashlist()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = loginWindow()
    ex.show()
    sys.exit(app.exec_())
