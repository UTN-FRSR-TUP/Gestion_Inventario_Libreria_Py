

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_FormADMI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1039, 855)
        
        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setGeometry(QtCore.QRect(10, 0, 901, 791))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        
        self.BotonBuscarEmpresa = QtWidgets.QPushButton(parent=self.frame)
        self.BotonBuscarEmpresa.setGeometry(QtCore.QRect(650, 100, 91, 31))
        self.BotonBuscarEmpresa.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.BotonBuscarEmpresa.setObjectName("BotonBuscarEmpresa")
        
        self.BotonCrearEmpresa_2 = QtWidgets.QPushButton(parent=self.frame)
        self.BotonCrearEmpresa_2.setGeometry(QtCore.QRect(770, 100, 91, 31))
        self.BotonCrearEmpresa_2.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.BotonCrearEmpresa_2.setObjectName("BotonCrearEmpresa_2")
        
        self.stackedWidget_2 = QtWidgets.QStackedWidget(parent=self.frame)
        self.stackedWidget_2.setGeometry(QtCore.QRect(60, 180, 811, 591))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        
        self.BuscarUsuarios = QtWidgets.QWidget()
        self.BuscarUsuarios.setObjectName("BuscarUsuarios")
        
        self.frame_4 = QtWidgets.QFrame(parent=self.BuscarUsuarios)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 811, 591))
        self.frame_4.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        
        self.tablaUsuarios = QtWidgets.QTableWidget(parent=self.frame_4)
        self.tablaUsuarios.setGeometry(QtCore.QRect(0, 0, 811, 591))
        self.tablaUsuarios.setObjectName("tablaUsuarios")
        self.tablaUsuarios.setColumnCount(9)
        self.tablaUsuarios.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablaUsuarios.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaUsuarios.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaUsuarios.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaUsuarios.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaUsuarios.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaUsuarios.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaUsuarios.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaUsuarios.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaUsuarios.setHorizontalHeaderItem(8, item)
        self.stackedWidget_2.addWidget(self.BuscarUsuarios)
        
        self.NuevoUsuario = QtWidgets.QWidget()
        self.NuevoUsuario.setObjectName("NuevoUsuario")
        
        self.frame_5 = QtWidgets.QFrame(parent=self.NuevoUsuario)
        self.frame_5.setGeometry(QtCore.QRect(240, 10, 351, 481))
        self.frame_5.setStyleSheet("border-color: rgb(6, 6, 6);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        
        self.InputNombreEmpresa = QtWidgets.QLineEdit(parent=self.frame_5)
        self.InputNombreEmpresa.setGeometry(QtCore.QRect(180, 30, 113, 20))
        self.InputNombreEmpresa.setObjectName("InputNombreEmpresa")
        self.InputTelefonoEmpresa = QtWidgets.QLineEdit(parent=self.frame_5)
        self.InputTelefonoEmpresa.setGeometry(QtCore.QRect(180, 70, 113, 20))
        self.InputTelefonoEmpresa.setObjectName("InputTelefonoEmpresa")
        self.InputCorreoEmpresa = QtWidgets.QLineEdit(parent=self.frame_5)
        self.InputCorreoEmpresa.setGeometry(QtCore.QRect(180, 110, 113, 20))
        self.InputCorreoEmpresa.setObjectName("InputCorreoEmpresa")
        self.inputCuilEmpresa = QtWidgets.QLineEdit(parent=self.frame_5)
        self.inputCuilEmpresa.setGeometry(QtCore.QRect(180, 150, 113, 20))
        self.inputCuilEmpresa.setObjectName("inputCuilEmpresa")
        self.InputLogoEmpresa = QtWidgets.QLineEdit(parent=self.frame_5)
        self.InputLogoEmpresa.setGeometry(QtCore.QRect(180, 190, 113, 20))
        self.InputLogoEmpresa.setObjectName("InputLogoEmpresa")
        
        self.label_4 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_4.setGeometry(QtCore.QRect(90, 30, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_5.setGeometry(QtCore.QRect(90, 70, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_6.setGeometry(QtCore.QRect(90, 110, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_7.setGeometry(QtCore.QRect(90, 150, 51, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_8.setGeometry(QtCore.QRect(90, 190, 81, 20))
        self.label_8.setObjectName("label_8")
        self.label_34 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_34.setGeometry(QtCore.QRect(90, 310, 101, 20))
        self.label_34.setObjectName("label_34")
        self.label_40 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_40.setGeometry(QtCore.QRect(90, 350, 101, 20))
        self.label_40.setObjectName("label_40")
        
        self.InputCiudadEmpresa = QtWidgets.QLineEdit(parent=self.frame_5)
        self.InputCiudadEmpresa.setGeometry(QtCore.QRect(180, 310, 113, 20))
        self.InputCiudadEmpresa.setObjectName("InputCiudadEmpresa")
        self.InputCalleEmpresa = QtWidgets.QLineEdit(parent=self.frame_5)
        self.InputCalleEmpresa.setGeometry(QtCore.QRect(180, 230, 113, 21))
        self.InputCalleEmpresa.setObjectName("InputCalleEmpresa")
        self.InputNumeroEmpresa = QtWidgets.QLineEdit(parent=self.frame_5)
        self.InputNumeroEmpresa.setGeometry(QtCore.QRect(180, 270, 113, 20))
        self.InputNumeroEmpresa.setObjectName("InputNumeroEmpresa")
        self.BotonCrearEmpresa = QtWidgets.QPushButton(parent=self.frame_5)
        self.BotonCrearEmpresa.setGeometry(QtCore.QRect(120, 400, 101, 41))
        self.BotonCrearEmpresa.setStyleSheet("\n"
"background-color: rgb(85, 255, 127);")
        
        self.BotonCrearEmpresa.setObjectName("BotonCrearEmpresa")
        
        self.InputEmpresa = QtWidgets.QLineEdit(parent=self.frame_5)
        self.InputEmpresa.setGeometry(QtCore.QRect(180, 350, 113, 20))
        self.InputEmpresa.setObjectName("InputEmpresa")
        
        self.label_46 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_46.setGeometry(QtCore.QRect(90, 230, 81, 20))
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_47.setGeometry(QtCore.QRect(90, 270, 71, 20))
        self.label_47.setObjectName("label_47")
        self.stackedWidget_2.addWidget(self.NuevoUsuario)
        
        self.ModificarUsuario = QtWidgets.QWidget()
        self.ModificarUsuario.setObjectName("ModificarUsuario")
        
        self.frame_6 = QtWidgets.QFrame(parent=self.ModificarUsuario)
        self.frame_6.setGeometry(QtCore.QRect(260, 10, 351, 481))
        self.frame_6.setStyleSheet("border-color: rgb(6, 6, 6);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        
        self.InputNombreEmpresaMod = QtWidgets.QLineEdit(parent=self.frame_6)
        self.InputNombreEmpresaMod.setGeometry(QtCore.QRect(180, 30, 113, 20))
        self.InputNombreEmpresaMod.setObjectName("InputNombreEmpresaMod")
        self.InputTelefonoEmpresaMod = QtWidgets.QLineEdit(parent=self.frame_6)
        self.InputTelefonoEmpresaMod.setGeometry(QtCore.QRect(180, 70, 113, 20))
        self.InputTelefonoEmpresaMod.setObjectName("InputTelefonoEmpresaMod")
        self.InputCorreoEmpresaMod = QtWidgets.QLineEdit(parent=self.frame_6)
        self.InputCorreoEmpresaMod.setGeometry(QtCore.QRect(180, 110, 113, 20))
        self.InputCorreoEmpresaMod.setObjectName("InputCorreoEmpresaMod")
        self.inputCuilEmpresaMod = QtWidgets.QLineEdit(parent=self.frame_6)
        self.inputCuilEmpresaMod.setGeometry(QtCore.QRect(180, 150, 113, 20))
        self.inputCuilEmpresaMod.setObjectName("inputCuilEmpresaMod")
        self.InputLogoEmpresaMod = QtWidgets.QLineEdit(parent=self.frame_6)
        self.InputLogoEmpresaMod.setGeometry(QtCore.QRect(180, 190, 113, 20))
        self.InputLogoEmpresaMod.setObjectName("InputLogoEmpresaMod")
        
        self.label_9 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_9.setGeometry(QtCore.QRect(90, 30, 47, 13))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_10.setGeometry(QtCore.QRect(90, 70, 47, 13))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_11.setGeometry(QtCore.QRect(90, 110, 47, 13))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_12.setGeometry(QtCore.QRect(90, 150, 51, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_13.setGeometry(QtCore.QRect(90, 190, 81, 20))
        self.label_13.setObjectName("label_13")
        self.label_35 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_35.setGeometry(QtCore.QRect(90, 310, 101, 20))
        self.label_35.setObjectName("label_35")
        self.label_41 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_41.setGeometry(QtCore.QRect(90, 350, 101, 20))
        self.label_41.setObjectName("label_41")
        
        
        self.InputCiudadEmpresaMod = QtWidgets.QLineEdit(parent=self.frame_6)
        self.InputCiudadEmpresaMod.setGeometry(QtCore.QRect(180, 310, 113, 20))
        self.InputCiudadEmpresaMod.setObjectName("InputCiudadEmpresaMod")
        self.InputCalleEmpresaMod = QtWidgets.QLineEdit(parent=self.frame_6)
        self.InputCalleEmpresaMod.setGeometry(QtCore.QRect(180, 230, 113, 21))
        self.InputCalleEmpresaMod.setObjectName("InputCalleEmpresaMod")
        self.InputNumeroEmpresaMod = QtWidgets.QLineEdit(parent=self.frame_6)
        self.InputNumeroEmpresaMod.setGeometry(QtCore.QRect(180, 270, 113, 20))
        self.InputNumeroEmpresaMod.setObjectName("InputNumeroEmpresaMod")
        
        self.BotonModEmpresa = QtWidgets.QPushButton(parent=self.frame_6)
        self.BotonModEmpresa.setGeometry(QtCore.QRect(120, 400, 101, 41))
        self.BotonModEmpresa.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.BotonModEmpresa.setObjectName("BotonModEmpresa")
        
        self.InputEmpresaMod = QtWidgets.QLineEdit(parent=self.frame_6)
        self.InputEmpresaMod.setGeometry(QtCore.QRect(180, 350, 113, 20))
        self.InputEmpresaMod.setObjectName("InputEmpresaMod")
        
        self.label_48 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_48.setGeometry(QtCore.QRect(90, 230, 81, 20))
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_49.setGeometry(QtCore.QRect(90, 270, 71, 20))
        self.label_49.setObjectName("label_49")
        self.stackedWidget_2.addWidget(self.ModificarUsuario)
        
        self.InputBuscarUsuario = QtWidgets.QLineEdit(parent=self.frame)
        self.InputBuscarUsuario.setGeometry(QtCore.QRect(280, 100, 371, 31))
        self.InputBuscarUsuario.setObjectName("InputBuscarUsuario")
        
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 90, 201, 41))
        self.label_3.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
         #conectar botones a funciones
        self.BotonCrearEmpresa_2.clicked.connect(self.mostrarNuevaEmpresa)
        self.BotonBuscarEmpresa.clicked.connect(self.mostrarBuscarEmpresa)
        self.BotonCrearEmpresa.clicked.connect(self.mostrarBuscarEmpresa)
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.BotonBuscarEmpresa.setText(_translate("Form", "Buscar empresas"))
        self.BotonCrearEmpresa_2.setText(_translate("Form", "Nueva empresa"))
        item = self.tablaUsuarios.horizontalHeaderItem(0)
        item.setText(_translate("Form", "id"))
        item = self.tablaUsuarios.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nombre"))
        item = self.tablaUsuarios.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Telefono"))
        item = self.tablaUsuarios.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Correo"))
        item = self.tablaUsuarios.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Fecha Nacimiento"))
        item = self.tablaUsuarios.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Logo"))
        item = self.tablaUsuarios.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Direccion"))
        item = self.tablaUsuarios.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Actualizar"))
        item = self.tablaUsuarios.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Borrar"))
        self.label_4.setText(_translate("Form", "Nombre"))
        self.label_5.setText(_translate("Form", "Telefono"))
        self.label_6.setText(_translate("Form", "Correo"))
        self.label_7.setText(_translate("Form", "Cuil"))
        self.label_8.setText(_translate("Form", "Logo"))
        self.label_34.setText(_translate("Form", "Ciudad"))
        self.label_40.setText(_translate("Form", "Pais"))
        self.BotonCrearEmpresa.setText(_translate("Form", "Crear"))
        self.label_46.setText(_translate("Form", "Calle"))
        self.label_47.setText(_translate("Form", "Numero"))
        self.label_9.setText(_translate("Form", "Nombre"))
        self.label_10.setText(_translate("Form", "Telefono"))
        self.label_11.setText(_translate("Form", "Correo"))
        self.label_12.setText(_translate("Form", "Cuil"))
        self.label_13.setText(_translate("Form", "Logo"))
        self.label_35.setText(_translate("Form", "Ciudad"))
        self.label_41.setText(_translate("Form", "Pais"))
        self.BotonModEmpresa.setText(_translate("Form", "Modificar"))
        self.label_48.setText(_translate("Form", "Calle"))
        self.label_49.setText(_translate("Form", "Numero"))
        self.label_3.setText(_translate("Form", "ADMINISTRACION"))

        #METODOS STACKED WIDGET
    def mostrarNuevaEmpresa(self):
        self.stackedWidget_2.setCurrentIndex(1)
    def mostrarBuscarEmpresa(self):
        self.stackedWidget_2.setCurrentIndex(0)
    def mostrarModificarEmpresa(self):
            self.stackedWidget_2.setCurrentIndex(2)