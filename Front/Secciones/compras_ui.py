from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_FormCompra(object):
    def setupUi(self, FormCompra):
        FormCompra.setObjectName("FormCompra")
        FormCompra.resize(912, 797)
        
        self.frameCompra = QtWidgets.QFrame(parent=FormCompra)
        self.frameCompra.setGeometry(QtCore.QRect(0, 0, 901, 791))
        self.frameCompra.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frameCompra.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameCompra.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameCompra.setObjectName("frameCompra")
        
        self.BotonBuscarCom = QtWidgets.QPushButton(parent=self.frameCompra)
        self.BotonBuscarCom.setGeometry(QtCore.QRect(420, 100, 91, 31))
        self.BotonBuscarCom.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.BotonBuscarCom.setObjectName("BotonBuscarCom")
        
        self.BotonNuevaCom = QtWidgets.QPushButton(parent=self.frameCompra)
        self.BotonNuevaCom.setGeometry(QtCore.QRect(770, 100, 91, 31))
        self.BotonNuevaCom.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.BotonNuevaCom.setObjectName("BotonNuevaCom")
        
        self.stackedWidget_4 = QtWidgets.QStackedWidget(parent=self.frameCompra)
        self.stackedWidget_4.setGeometry(QtCore.QRect(50, 170, 811, 591))
        self.stackedWidget_4.setObjectName("stackedWidget_4")
        
        self.BuscarCompras = QtWidgets.QWidget()
        self.BuscarCompras.setObjectName("BuscarCompras")
        
        self.frame_12 = QtWidgets.QFrame(parent=self.BuscarCompras)
        self.frame_12.setGeometry(QtCore.QRect(0, 0, 811, 591))
        self.frame_12.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.frame_12.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_12.setObjectName("frame_12")
        
        self.tablaCompras = QtWidgets.QTableWidget(parent=self.frame_12)
        self.tablaCompras.setGeometry(QtCore.QRect(0, 0, 811, 591))
        self.tablaCompras.setObjectName("tablaCompras")
        self.tablaCompras.setColumnCount(9)
        self.tablaCompras.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablaCompras.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaCompras.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaCompras.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaCompras.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaCompras.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaCompras.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaCompras.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaCompras.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaCompras.setHorizontalHeaderItem(8, item)
        self.stackedWidget_4.addWidget(self.BuscarCompras)
        
        ##nueva compra
        self.NuevaCompra = QtWidgets.QWidget()
        self.NuevaCompra.setObjectName("NuevaCompra")
        self.frame_13 = QtWidgets.QFrame(parent=self.NuevaCompra)
        self.frame_13.setGeometry(QtCore.QRect(200, 40, 411, 491))
        self.frame_13.setStyleSheet("border-color: rgb(6, 6, 6);")
        self.frame_13.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_13.setObjectName("frame_13")
        #inputs
        self.inputAlmacenamientoCom = QtWidgets.QLineEdit(parent=self.frame_13)
        self.inputAlmacenamientoCom.setGeometry(QtCore.QRect(230, 30, 113, 20))
        self.inputAlmacenamientoCom.setObjectName("inputAlmacenamientoCom")
        
        self.inputFechaCom = QtWidgets.QLineEdit(parent=self.frame_13)
        self.inputFechaCom.setGeometry(QtCore.QRect(230, 70, 113, 20))
        self.inputFechaCom.setObjectName("inputFechaCom")
        
        self.inputCantidadCom = QtWidgets.QLineEdit(parent=self.frame_13)
        self.inputCantidadCom.setGeometry(QtCore.QRect(230, 110, 113, 20))
        self.inputCantidadCom.setObjectName("inputCantidadCom")
        
        self.inputPrecioUnarioCom = QtWidgets.QLineEdit(parent=self.frame_13)
        self.inputPrecioUnarioCom.setGeometry(QtCore.QRect(230, 150, 113, 20))
        self.inputPrecioUnarioCom.setObjectName("inputPrecioUnarioCom")
        
        self.inputProvedorCom = QtWidgets.QLineEdit(parent=self.frame_13)
        self.inputProvedorCom.setGeometry(QtCore.QRect(230, 190, 113, 20))
        self.inputProvedorCom.setObjectName("inputProvedorCom")
        
        #labels
        self.label_25 = QtWidgets.QLabel(parent=self.frame_13)
        self.label_25.setGeometry(QtCore.QRect(90, 30, 81, 16))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(parent=self.frame_13)
        self.label_26.setGeometry(QtCore.QRect(90, 70, 47, 13))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(parent=self.frame_13)
        self.label_27.setGeometry(QtCore.QRect(90, 110, 47, 13))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(parent=self.frame_13)
        self.label_28.setGeometry(QtCore.QRect(90, 150, 81, 20))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(parent=self.frame_13)
        self.label_29.setGeometry(QtCore.QRect(90, 190, 101, 20))
        self.label_29.setObjectName("label_29")
        
        #boton compra
        self.BotonCrearCompra = QtWidgets.QPushButton(parent=self.frame_13)
        self.BotonCrearCompra.setGeometry(QtCore.QRect(160, 410, 101, 41))
        self.BotonCrearCompra.setStyleSheet("\n"
"background-color: rgb(85, 255, 127);")
        self.BotonCrearCompra.setObjectName("BotonCrearCompra")
        
        #parte pagos
        self.label_36 = QtWidgets.QLabel(parent=self.frame_13)
        self.label_36.setGeometry(QtCore.QRect(200, 240, 101, 20))
        self.label_36.setObjectName("label_36")
        
        self.InputOrigenCom = QtWidgets.QLineEdit(parent=self.frame_13)
        self.InputOrigenCom.setGeometry(QtCore.QRect(230, 350, 113, 20))
        self.InputOrigenCom.setObjectName("InputOrigenCom")
        
        self.InputTipoCom = QtWidgets.QLineEdit(parent=self.frame_13)
        self.InputTipoCom.setGeometry(QtCore.QRect(230, 270, 113, 20))
        self.InputTipoCom.setObjectName("InputTipoCom")
        
        self.inputCuotasCom = QtWidgets.QLineEdit(parent=self.frame_13)
        self.inputCuotasCom.setGeometry(QtCore.QRect(230, 310, 113, 20))
        self.inputCuotasCom.setObjectName("inputCuotasCom")
        
        self.label_37 = QtWidgets.QLabel(parent=self.frame_13)
        self.label_37.setGeometry(QtCore.QRect(90, 270, 101, 20))
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(parent=self.frame_13)
        self.label_38.setGeometry(QtCore.QRect(90, 310, 101, 20))
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(parent=self.frame_13)
        self.label_39.setGeometry(QtCore.QRect(90, 350, 101, 16))
        self.label_39.setObjectName("label_39")
        self.stackedWidget_4.addWidget(self.NuevaCompra)
        
        ##nuevo provedor
        self.NuevoProvedor = QtWidgets.QWidget()
        self.NuevoProvedor.setObjectName("NuevoProvedor")
        
        self.frame_14 = QtWidgets.QFrame(parent=self.NuevoProvedor)
        self.frame_14.setGeometry(QtCore.QRect(210, 50, 411, 291))
        self.frame_14.setStyleSheet("border-color: rgb(6, 6, 6);")
        self.frame_14.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_14.setObjectName("frame_14")
        
        #inputs
        self.inputNombreProv = QtWidgets.QLineEdit(parent=self.frame_14)
        self.inputNombreProv.setGeometry(QtCore.QRect(230, 30, 113, 20))
        self.inputNombreProv.setObjectName("inputNombreProv")
        
        self.inputTelProv = QtWidgets.QLineEdit(parent=self.frame_14)
        self.inputTelProv.setGeometry(QtCore.QRect(230, 70, 113, 20))
        self.inputTelProv.setObjectName("inputTelProv")
        
        self.InputContactoProv = QtWidgets.QLineEdit(parent=self.frame_14)
        self.InputContactoProv.setGeometry(QtCore.QRect(230, 110, 113, 20))
        self.InputContactoProv.setObjectName("InputContactoProv")
        
        #labels
        self.label_30 = QtWidgets.QLabel(parent=self.frame_14)
        self.label_30.setGeometry(QtCore.QRect(90, 30, 81, 16))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(parent=self.frame_14)
        self.label_31.setGeometry(QtCore.QRect(90, 70, 47, 13))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(parent=self.frame_14)
        self.label_32.setGeometry(QtCore.QRect(90, 110, 47, 13))
        self.label_32.setObjectName("label_32")
        
        #boton provedor
        self.BotonCrearProv = QtWidgets.QPushButton(parent=self.frame_14)
        self.BotonCrearProv.setGeometry(QtCore.QRect(140, 190, 101, 41))
        self.BotonCrearProv.setStyleSheet("\n"
"background-color: rgb(85, 255, 127);")
        self.BotonCrearProv.setObjectName("BotonCrearProv")
        self.stackedWidget_4.addWidget(self.NuevoProvedor)
        
        #buscar
        self.inputBuscarCom = QtWidgets.QLineEdit(parent=self.frameCompra)
        self.inputBuscarCom.setGeometry(QtCore.QRect(170, 100, 251, 31))
        self.inputBuscarCom.setObjectName("inputBuscarCom")
        self.label_35 = QtWidgets.QLabel(parent=self.frameCompra)
        self.label_35.setGeometry(QtCore.QRect(50, 90, 111, 41))
        self.label_35.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_35.setObjectName("label_35")
        
        #boton nuevo provedor
        self.BotonNuevoPro = QtWidgets.QPushButton(parent=self.frameCompra)
        self.BotonNuevoPro.setGeometry(QtCore.QRect(590, 100, 91, 31))
        self.BotonNuevoPro.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.BotonNuevoPro.setObjectName("BotonNuevoPro")

        self.retranslateUi(FormCompra)
        self.stackedWidget_4.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FormCompra)
        
        #conectar botones a funciones
        self.BotonBuscarCom.clicked.connect(self.mostrarBusqueda)
        self.BotonNuevaCom.clicked.connect(self.mostrarNuevaCompra)
        self.BotonNuevoPro.clicked.connect(self.mostrarNuevoProvedor)

    def retranslateUi(self, FormCompra):
        _translate = QtCore.QCoreApplication.translate
        FormCompra.setWindowTitle(_translate("FormCompra", "Form"))
        self.BotonBuscarCom.setText(_translate("FormCompra", "BUSCAR"))
        self.BotonNuevaCom.setText(_translate("FormCompra", "Nueva Compra"))
        item = self.tablaCompras.horizontalHeaderItem(0)
        item.setText(_translate("FormCompra", "id"))
        item = self.tablaCompras.horizontalHeaderItem(1)
        item.setText(_translate("FormCompra", "Almacenamiento"))
        item = self.tablaCompras.horizontalHeaderItem(2)
        item.setText(_translate("FormCompra", "fecha"))
        item = self.tablaCompras.horizontalHeaderItem(3)
        item.setText(_translate("FormCompra", "Cantidad"))
        item = self.tablaCompras.horizontalHeaderItem(4)
        item.setText(_translate("FormCompra", "Precio unitario"))
        item = self.tablaCompras.horizontalHeaderItem(5)
        item.setText(_translate("FormCompra", "Pago"))
        item = self.tablaCompras.horizontalHeaderItem(6)
        item.setText(_translate("FormCompra", "Provedor"))
        item = self.tablaCompras.horizontalHeaderItem(7)
        item.setText(_translate("FormCompra", "Actualizar"))
        item = self.tablaCompras.horizontalHeaderItem(8)
        item.setText(_translate("FormCompra", "Borrar"))
        self.label_25.setText(_translate("FormCompra", "Almacenamiento"))
        self.label_26.setText(_translate("FormCompra", "Fecha"))
        self.label_27.setText(_translate("FormCompra", "Cantidad"))
        self.label_28.setText(_translate("FormCompra", "Precio Unitario"))
        self.label_29.setText(_translate("FormCompra", "Provedor"))
        self.BotonCrearCompra.setText(_translate("FormCompra", "Crear"))
        self.label_36.setText(_translate("FormCompra", "PAGO"))
        self.label_37.setText(_translate("FormCompra", "Tipo"))
        self.label_38.setText(_translate("FormCompra", "Cuotas"))
        self.label_39.setText(_translate("FormCompra", "Origen"))
        self.label_30.setText(_translate("FormCompra", "Nombre"))
        self.label_31.setText(_translate("FormCompra", "Telefono"))
        self.label_32.setText(_translate("FormCompra", "Contacto Principal"))
        self.BotonCrearProv.setText(_translate("FormCompra", "Crear"))
        self.label_35.setText(_translate("FormCompra", "COMPRAS"))
        self.BotonNuevoPro.setText(_translate("FormCompra", "Nuevo Provedor"))


    
    def mostrarBusqueda(self):
        self.stackedWidget_4.setCurrentIndex(0)
    def mostrarNuevaCompra(self):
        self.stackedWidget_4.setCurrentIndex(1)
    def mostrarNuevoProvedor(self):
        self.stackedWidget_4.setCurrentIndex(2)