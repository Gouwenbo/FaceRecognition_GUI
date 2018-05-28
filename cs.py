# -*- coding=utf-8 -*-  
from PyQt5.QtWidgets import QWidget,QApplication,QLCDNumber,QSlider,QVBoxLayout  
from PyQt5.QtCore import Qt  
import sys  
class Example(QWidget):  
    def __init__(self):  
        super(Example,self).__init__()  
        self.initUI()  
  
    def initUI(self):  
        lcd = QLCDNumber(self)#数字  
        sld = QSlider(Qt.Horizontal,self) #水平拖动条  
        vbox = QVBoxLayout() #建立一个垂直布局  
        vbox.addWidget(lcd) #加入布局  
        vbox.addWidget(sld)  
  
        self.setLayout(vbox) #固定布局  
        sld.valueChanged.connect(lcd.display)#将水平拖动条的变化和数字连接起来  
  
        self.setGeometry(300,300,300,300)  
        self.setWindowTitle(u'宋存最美')  
        self.show()  
if __name__ == '__main__':  
    app = QApplication(sys.argv)  
    ex = Example()  
    sys.exit(app.exec_())  
    '''class managerWindow(manager_Dialog):
    def __init__(self):
        super(managerWindow, self).__init__()
        self.setupUi(self)
        self.setlcd()
        self.pushButton.clicked.connect(self.loadModel)
        self.pushButton_2.clicked.connect(self.loadId)
        self.pushButton_4.clicked.connect(self.show_manager_user)
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
                #self.progressBar.setValue(i/len(ids))
                img = cv2.imread(image_path)
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
        #self.progressBar.setValue(100)
        return id_dataset ,len(ids)       ##
    def readconfig(self):
        args = Arg_Data()
        cf = ConfigParser.ConfigParser()
        cf.read("project.conf")
        model_dir = cf.get("model", "model_dir")
        id_dir = cf.get("model","id_dir")
        test_dir = cf.get("model","test_dir")
        #print(model_dir+" "+id_dir+" "+test_dir)
        args.setdir(id_dir,test_dir,model_dir+'/model,0')
        return args

    def loadModel(self):
        self.argv = self.readconfig()
        self.model = face_embedding.FaceModel(self.argv)
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
        QMessageBox.warning(self, ("提示"), ("\n检测环境与模型载入完成!"))
    def loadId(self):
        
        self.id_dataset ,self.idnums = self.get_id_data(self.argv.id_dir)
        
        QMessageBox.warning(self, ("提示"), ("\nID数据库载入完成!"))
    def setlcd(self):
        db = pymysql.connect("localhost","root","root","sys",charset='utf8')
        cursor = db.cursor()
        sql = "select * from Users where levUsers not like \'manager\'"
        if cursor.execute(sql):
            data = cursor.fetchall()
            self.lcdNumber.display(int(len(data)))
    def show_manager_user(self):
        self.manager_userWindow = manager_userWindow()
        QMessageBox.warning(self, ("操作说明"), ("\n根据提示添加用户信息\n 删除用户可根据： \n 用户ID \n 用户姓名\n 二选一 \n"))
        self.manager_userWindow.exec_()
        '''
