from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_FormDevoluciones(object):
    def setupUi(self, FormDevoluciones):
        FormDevoluciones.setObjectName("FormDevoluciones")
        FormDevoluciones.resize(907, 790)
        
        self.frameDevoluciones = QtWidgets.QFrame(parent=FormDevoluciones)
        self.frameDevoluciones.setGeometry(QtCore.QRect(0, 0, 901, 791))
        self.frameDevoluciones.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frameDevoluciones.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameDevoluciones.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameDevoluciones.setObjectName("frameDevoluciones")
        
        self.BotonBuscarDev = QtWidgets.QPushButton(parent=self.frameDevoluciones)
        self.BotonBuscarDev.setGeometry(QtCore.QRect(640, 100, 91, 31))
        self.BotonBuscarDev.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.BotonBuscarDev.setObjectName("BotonBuscarDev")
        
        self.BotonNuevadev = QtWidgets.QPushButton(parent=self.frameDevoluciones)
        self.BotonNuevadev.setGeometry(QtCore.QRect(770, 100, 91, 31))
        self.BotonNuevadev.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.BotonNuevadev.setObjectName("BotonNuevadev")
        
        self.stackedWidget_5 = QtWidgets.QStackedWidget(parent=self.frameDevoluciones)
        self.stackedWidget_5.setGeometry(QtCore.QRect(50, 170, 811, 591))
        self.stackedWidget_5.setObjectName("stackedWidget_5")
        
        self.BuscarDevoluciones = QtWidgets.QWidget()
        self.BuscarDevoluciones.setObjectName("BuscarDevoluciones")
        
        self.frame_16 = QtWidgets.QFrame(parent=self.BuscarDevoluciones)
        self.frame_16.setGeometry(QtCore.QRect(0, 0, 811, 591))
        self.frame_16.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.frame_16.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_16.setObjectName("frame_16")
        
        self.tablaDevoluciones4 = QtWidgets.QTableWidget(parent=self.frame_16)
        self.tablaDevoluciones4.setGeometry(QtCore.QRect(0, 0, 811, 591))
        self.tablaDevoluciones4.setObjectName("tablaDevoluciones4")
        self.tablaDevoluciones4.setColumnCount(8)
        self.tablaDevoluciones4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablaDevoluciones4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaDevoluciones4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaDevoluciones4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaDevoluciones4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaDevoluciones4.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        
        self.tablaDevoluciones4.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaDevoluciones4.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaDevoluciones4.setHorizontalHeaderItem(7, item)
        self.stackedWidget_5.addWidget(self.BuscarDevoluciones)
        
        self.NuevaDev = QtWidgets.QWidget()
        self.NuevaDev.setObjectName("NuevaDev")
        
        self.frame_17 = QtWidgets.QFrame(parent=self.NuevaDev)
        self.frame_17.setGeometry(QtCore.QRect(200, 40, 411, 331))
        self.frame_17.setStyleSheet("border-color: rgb(6, 6, 6);")
        self.frame_17.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_17.setObjectName("frame_17")
        
        self.MotivoDev = QtWidgets.QLineEdit(parent=self.frame_17)
        self.MotivoDev.setGeometry(QtCore.QRect(230, 30, 113, 20))
        self.MotivoDev.setObjectName("MotivoDev")
        
        self.FechaDev = QtWidgets.QLineEdit(parent=self.frame_17)
        self.FechaDev.setGeometry(QtCore.QRect(230, 70, 113, 20))
        self.FechaDev.setObjectName("FechaDev")
        
        self.CantidadDev = QtWidgets.QLineEdit(parent=self.frame_17)
        self.CantidadDev.setGeometry(QtCore.QRect(230, 110, 113, 20))
        self.CantidadDev.setObjectName("CantidadDev")
        
        self.PagoDev = QtWidgets.QLineEdit(parent=self.frame_17)
        self.PagoDev.setGeometry(QtCore.QRect(230, 150, 113, 20))
        self.PagoDev.setObjectName("PagoDev")
        
        self.label_57 = QtWidgets.QLabel(parent=self.frame_17)
        self.label_57.setGeometry(QtCore.QRect(90, 30, 81, 16))
        self.label_57.setObjectName("label_57")
        self.label_58 = QtWidgets.QLabel(parent=self.frame_17)
        self.label_58.setGeometry(QtCore.QRect(90, 70, 47, 13))
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(parent=self.frame_17)
        self.label_59.setGeometry(QtCore.QRect(90, 110, 47, 13))
        self.label_59.setObjectName("label_59")
        self.label_60 = QtWidgets.QLabel(parent=self.frame_17)
        self.label_60.setGeometry(QtCore.QRect(90, 150, 81, 20))
        self.label_60.setObjectName("label_60")
        
        self.BotonCrearDev = QtWidgets.QPushButton(parent=self.frame_17)
        self.BotonCrearDev.setGeometry(QtCore.QRect(150, 230, 101, 41))
        self.BotonCrearDev.setStyleSheet("\n"
"background-color: rgb(85, 255, 127);")
        self.BotonCrearDev.setObjectName("BotonCrearDev")
        self.stackedWidget_5.addWidget(self.NuevaDev)
        
        
        self.inputBuscarDev = QtWidgets.QLineEdit(parent=self.frameDevoluciones)
        self.inputBuscarDev.setGeometry(QtCore.QRect(390, 100, 251, 31))
        self.inputBuscarDev.setObjectName("inputBuscarDev")
        
        self.label_69 = QtWidgets.QLabel(parent=self.frameDevoluciones)
        self.label_69.setGeometry(QtCore.QRect(50, 90, 201, 41))
        self.label_69.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_69.setObjectName("label_69")

        self.retranslateUi(FormDevoluciones)
        self.stackedWidget_5.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FormDevoluciones)
        
        #conectar metodos stackwidget   
        self.BotonBuscarDev.clicked.connect(self.mostrarBuscar)
        self.BotonNuevadev.clicked.connect(self.mostrarNuevo)
        

    def retranslateUi(self, FormDevoluciones):
        _translate = QtCore.QCoreApplication.translate
        FormDevoluciones.setWindowTitle(_translate("FormDevoluciones", "Form"))
        self.BotonBuscarDev.setText(_translate("FormDevoluciones", "BUSCAR"))
        self.BotonNuevadev.setText(_translate("FormDevoluciones", "Nueva devolucion"))
        item = self.tablaDevoluciones4.horizontalHeaderItem(0)
        item.setText(_translate("FormDevoluciones", "id"))
        item = self.tablaDevoluciones4.horizontalHeaderItem(1)
        item.setText(_translate("FormDevoluciones", "Almacenamiento"))
        item = self.tablaDevoluciones4.horizontalHeaderItem(2)
        item.setText(_translate("FormDevoluciones", "fecha"))
        item = self.tablaDevoluciones4.horizontalHeaderItem(3)
        item.setText(_translate("FormDevoluciones", "Cantidad"))
        item = self.tablaDevoluciones4.horizontalHeaderItem(4)
        item.setText(_translate("FormDevoluciones", "Precio unitario"))
        item = self.tablaDevoluciones4.horizontalHeaderItem(5)
        item.setText(_translate("FormDevoluciones", "Pago"))
        item = self.tablaDevoluciones4.horizontalHeaderItem(6)
        item.setText(_translate("FormDevoluciones", "Provedor"))
        item = self.tablaDevoluciones4.horizontalHeaderItem(7)
        item.setText(_translate("FormDevoluciones", "Borrar"))
        self.label_57.setText(_translate("FormDevoluciones", "Motivo"))
        self.label_58.setText(_translate("FormDevoluciones", "Fecha"))
        self.label_59.setText(_translate("FormDevoluciones", "Cantidad"))
        self.label_60.setText(_translate("FormDevoluciones", "ID Pago"))
        self.BotonCrearDev.setText(_translate("FormDevoluciones", "Crear"))
        self.label_69.setText(_translate("FormDevoluciones", "DEVOLUCIONES"))

    #metodos stackwidget
    def mostrarBuscar(self):
        self.stackedWidget_5.setCurrentIndex(0)
    def mostrarNuevo(self):
        self.stackedWidget_5.setCurrentIndex(1)
   