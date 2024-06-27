from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_FormUsuarios(object):
    def setupUi(self, FormUsuarios):
        FormUsuarios.setObjectName("FormUsuarios")
        FormUsuarios.resize(907, 790)#tamaño
        
        self.frameUsuarios = QtWidgets.QFrame(parent=FormUsuarios)
        self.frameUsuarios.setGeometry(QtCore.QRect(0, 0, 901, 791))#posicion
        self.frameUsuarios.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frameUsuarios.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameUsuarios.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameUsuarios.setObjectName("frameUsuarios")
        
        self.BotonBuscarUsuario = QtWidgets.QPushButton(parent=self.frameUsuarios)
        self.BotonBuscarUsuario.setGeometry(QtCore.QRect(650, 100, 91, 31))
        self.BotonBuscarUsuario.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.BotonBuscarUsuario.setObjectName("BotonBuscarUsuario")
        
        self.BotonCrearUsuario = QtWidgets.QPushButton(parent=self.frameUsuarios)
        self.BotonCrearUsuario.setGeometry(QtCore.QRect(770, 100, 91, 31))
        self.BotonCrearUsuario.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.BotonCrearUsuario.setObjectName("BotonCrearUsuario")
        
        self.stackedWidget_2 = QtWidgets.QStackedWidget(parent=self.frameUsuarios)
        self.stackedWidget_2.setGeometry(QtCore.QRect(50, 170, 811, 591))
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
        self.tablaUsuarios.setColumnCount(8)
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
        self.stackedWidget_2.addWidget(self.BuscarUsuarios)
        
        self.NuevoUsuario = QtWidgets.QWidget()
        self.NuevoUsuario.setObjectName("NuevoUsuario")
        
        self.frame_5 = QtWidgets.QFrame(parent=self.NuevoUsuario)
        self.frame_5.setGeometry(QtCore.QRect(230, 20, 411, 551))
        self.frame_5.setStyleSheet("border-color: rgb(6, 6, 6);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        
        self.InputNombreUsuario = QtWidgets.QLineEdit(parent=self.frame_5)
        self.InputNombreUsuario.setGeometry(QtCore.QRect(230, 30, 113, 20))
        self.InputNombreUsuario.setObjectName("InputNombreUsuario")
        
        self.InputApellidoUsuario = QtWidgets.QLineEdit(parent=self.frame_5)
        self.InputApellidoUsuario.setGeometry(QtCore.QRect(230, 70, 113, 20))
        self.InputApellidoUsuario.setObjectName("InputApellidoUsuario")
        
        self.InputCorreoUsuario = QtWidgets.QLineEdit(parent=self.frame_5)
        self.InputCorreoUsuario.setGeometry(QtCore.QRect(230, 110, 113, 20))
        self.InputCorreoUsuario.setObjectName("InputCorreoUsuario")
        
        self.inputTelefonoUsuario = QtWidgets.QLineEdit(parent=self.frame_5)
        self.inputTelefonoUsuario.setGeometry(QtCore.QRect(230, 150, 113, 20))
        self.inputTelefonoUsuario.setObjectName("inputTelefonoUsuario")
        
        self.InputFechaNacUsuario = QtWidgets.QLineEdit(parent=self.frame_5)
        self.InputFechaNacUsuario.setGeometry(QtCore.QRect(230, 190, 113, 20))
        self.InputFechaNacUsuario.setObjectName("InputFechaNacUsuario")
        
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
        self.label_8.setGeometry(QtCore.QRect(90, 190, 101, 20))
        self.label_8.setObjectName("label_8")
        self.label_33 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_33.setGeometry(QtCore.QRect(90, 230, 101, 20))
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_34.setGeometry(QtCore.QRect(90, 350, 101, 20))
        self.label_34.setObjectName("label_34")
        self.label_40 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_40.setGeometry(QtCore.QRect(90, 390, 101, 20))
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_41.setGeometry(QtCore.QRect(90, 430, 101, 20))
        self.label_41.setObjectName("label_41")
        
        self.InputCiudadUsuario = QtWidgets.QLineEdit(parent=self.frame_5)
        self.InputCiudadUsuario.setGeometry(QtCore.QRect(230, 350, 113, 20))
        self.InputCiudadUsuario.setObjectName("InputCiudadUsuario")
        
        self.InputImgUsuario = QtWidgets.QLineEdit(parent=self.frame_5)
        self.InputImgUsuario.setGeometry(QtCore.QRect(230, 230, 113, 20))
        self.InputImgUsuario.setObjectName("InputImgUsuario")
        
        self.InputCalleUsuario = QtWidgets.QLineEdit(parent=self.frame_5)
        self.InputCalleUsuario.setGeometry(QtCore.QRect(230, 270, 113, 20))
        self.InputCalleUsuario.setObjectName("InputCalleUsuario")
        
        self.InputNumeroUsuario = QtWidgets.QLineEdit(parent=self.frame_5)
        self.InputNumeroUsuario.setGeometry(QtCore.QRect(230, 310, 113, 20))
        self.InputNumeroUsuario.setObjectName("InputNumeroUsuario")
        
        self.BotonCrearUsuario_2 = QtWidgets.QPushButton(parent=self.frame_5)
        self.BotonCrearUsuario_2.setGeometry(QtCore.QRect(160, 490, 101, 41))
        self.BotonCrearUsuario_2.setStyleSheet("\n"
"background-color: rgb(85, 255, 127);")
        self.BotonCrearUsuario_2.setObjectName("BotonCrearUsuario_2")
        
        self.InputRolUsuario = QtWidgets.QLineEdit(parent=self.frame_5)
        self.InputRolUsuario.setGeometry(QtCore.QRect(230, 430, 113, 20))
        self.InputRolUsuario.setObjectName("InputRolUsuario")
        
        self.InputUsuario = QtWidgets.QLineEdit(parent=self.frame_5)
        self.InputUsuario.setGeometry(QtCore.QRect(230, 390, 113, 20))
        self.InputUsuario.setObjectName("InputUsuario")
        
        self.label_46 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_46.setGeometry(QtCore.QRect(90, 270, 101, 20))
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_47.setGeometry(QtCore.QRect(90, 310, 101, 20))
        self.label_47.setObjectName("label_47")
        self.stackedWidget_2.addWidget(self.NuevoUsuario)
        
        self.ModificarUsuario = QtWidgets.QWidget()
        self.ModificarUsuario.setObjectName("ModificarUsuario")
        
        self.frame_6 = QtWidgets.QFrame(parent=self.ModificarUsuario)
        self.frame_6.setGeometry(QtCore.QRect(210, 20, 411, 551))
        self.frame_6.setStyleSheet("border-color: rgb(6, 6, 6);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        
        self.InputNombreModUsuario = QtWidgets.QLineEdit(parent=self.frame_6)
        self.InputNombreModUsuario.setGeometry(QtCore.QRect(230, 30, 113, 20))
        self.InputNombreModUsuario.setObjectName("InputNombreModUsuario")
        
        self.InputApellidoModUsuario = QtWidgets.QLineEdit(parent=self.frame_6)
        self.InputApellidoModUsuario.setGeometry(QtCore.QRect(230, 70, 113, 20))
        self.InputApellidoModUsuario.setObjectName("InputApellidoModUsuario")
        
        self.InputCorreoModUsuario = QtWidgets.QLineEdit(parent=self.frame_6)
        self.InputCorreoModUsuario.setGeometry(QtCore.QRect(230, 110, 113, 20))
        self.InputCorreoModUsuario.setObjectName("InputCorreoModUsuario")
        
        self.InputTelefonoModUsuario = QtWidgets.QLineEdit(parent=self.frame_6)
        self.InputTelefonoModUsuario.setGeometry(QtCore.QRect(230, 150, 113, 20))
        self.InputTelefonoModUsuario.setObjectName("InputTelefonoModUsuario")
        
        self.InputFechaNacModUsuario = QtWidgets.QLineEdit(parent=self.frame_6)
        self.InputFechaNacModUsuario.setGeometry(QtCore.QRect(230, 190, 113, 20))
        self.InputFechaNacModUsuario.setObjectName("InputFechaNacModUsuario")
        
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
        self.label_13.setGeometry(QtCore.QRect(90, 190, 101, 20))
        self.label_13.setObjectName("label_13")
        self.label_42 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_42.setGeometry(QtCore.QRect(90, 230, 101, 20))
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_43.setGeometry(QtCore.QRect(90, 350, 101, 20))
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_44.setGeometry(QtCore.QRect(90, 390, 101, 20))
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_45.setGeometry(QtCore.QRect(90, 430, 101, 20))
        self.label_45.setObjectName("label_45")
        
        self.InputCiudadModUsuario = QtWidgets.QLineEdit(parent=self.frame_6)
        self.InputCiudadModUsuario.setGeometry(QtCore.QRect(230, 350, 113, 20))
        self.InputCiudadModUsuario.setObjectName("InputCiudadModUsuario")
        
        self.InputImgModUsuario = QtWidgets.QLineEdit(parent=self.frame_6)
        self.InputImgModUsuario.setGeometry(QtCore.QRect(230, 230, 113, 20))
        self.InputImgModUsuario.setObjectName("InputImgModUsuario")
        
        self.InputCalleModUsuario = QtWidgets.QLineEdit(parent=self.frame_6)
        self.InputCalleModUsuario.setGeometry(QtCore.QRect(230, 270, 113, 20))
        self.InputCalleModUsuario.setObjectName("InputCalleModUsuario")
        
        self.InputNumeroModUsuario = QtWidgets.QLineEdit(parent=self.frame_6)
        self.InputNumeroModUsuario.setGeometry(QtCore.QRect(230, 310, 113, 20))
        self.InputNumeroModUsuario.setObjectName("InputNumeroModUsuario")
        
        self.botoncrearModUsuario = QtWidgets.QPushButton(parent=self.frame_6)
        self.botoncrearModUsuario.setGeometry(QtCore.QRect(160, 490, 101, 41))
        self.botoncrearModUsuario.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.botoncrearModUsuario.setObjectName("botoncrearModUsuario")
        
        self.InputRolModUsuario = QtWidgets.QLineEdit(parent=self.frame_6)
        self.InputRolModUsuario.setGeometry(QtCore.QRect(230, 430, 113, 20))
        self.InputRolModUsuario.setObjectName("InputRolModUsuario")
        
        self.InputPaisModUsuario = QtWidgets.QLineEdit(parent=self.frame_6)
        self.InputPaisModUsuario.setGeometry(QtCore.QRect(230, 390, 113, 20))
        self.InputPaisModUsuario.setObjectName("InputPaisModUsuario")
        
        self.label_48 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_48.setGeometry(QtCore.QRect(90, 270, 101, 20))
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_49.setGeometry(QtCore.QRect(90, 310, 101, 20))
        self.label_49.setObjectName("label_49")
        self.stackedWidget_2.addWidget(self.ModificarUsuario)
        
        self.InputBuscarUsuario = QtWidgets.QLineEdit(parent=self.frameUsuarios)
        self.InputBuscarUsuario.setGeometry(QtCore.QRect(280, 100, 371, 31))
        self.InputBuscarUsuario.setObjectName("InputBuscarUsuario")
        
        self.label_3 = QtWidgets.QLabel(parent=self.frameUsuarios)
        self.label_3.setGeometry(QtCore.QRect(50, 90, 151, 41))
        self.label_3.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(FormUsuarios)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FormUsuarios)
        
        #funciones metodos 
        self.BotonBuscarUsuario.clicked.connect(self.mostrarBuscarUsuario)
        self.BotonCrearUsuario.clicked.connect(self.mostrarNuevoUsuario)
        self.BotonCrearUsuario_2.clicked.connect(self.mostrarBuscarUsuario)

    def retranslateUi(self, FormUsuarios):
        _translate = QtCore.QCoreApplication.translate
        FormUsuarios.setWindowTitle(_translate("FormUsuarios", "Form"))
        self.BotonBuscarUsuario.setText(_translate("FormUsuarios", "Buscar usuarios"))
        self.BotonCrearUsuario.setText(_translate("FormUsuarios", "Nuevo usuario"))
        item = self.tablaUsuarios.horizontalHeaderItem(0)
        item.setText(_translate("FormUsuarios", "id"))
        item = self.tablaUsuarios.horizontalHeaderItem(1)
        item.setText(_translate("FormUsuarios", "Apellido"))
        item = self.tablaUsuarios.horizontalHeaderItem(2)
        item.setText(_translate("FormUsuarios", "Nombre"))
        item = self.tablaUsuarios.horizontalHeaderItem(3)
        item.setText(_translate("FormUsuarios", "Direccion"))
        item = self.tablaUsuarios.horizontalHeaderItem(4)
        item.setText(_translate("FormUsuarios", "ciudad"))
        item = self.tablaUsuarios.horizontalHeaderItem(5)
        item.setText(_translate("FormUsuarios", "Fecha Nacimiento"))
        item = self.tablaUsuarios.horizontalHeaderItem(6)
        item.setText(_translate("FormUsuarios", "Actualizar"))
        item = self.tablaUsuarios.horizontalHeaderItem(7)
        item.setText(_translate("FormUsuarios", "Borrar"))
        self.label_4.setText(_translate("FormUsuarios", "Nombre"))
        self.label_5.setText(_translate("FormUsuarios", "Apellido"))
        self.label_6.setText(_translate("FormUsuarios", "Correo"))
        self.label_7.setText(_translate("FormUsuarios", "Telefono"))
        self.label_8.setText(_translate("FormUsuarios", "Fecha de nacimiento"))
        self.label_33.setText(_translate("FormUsuarios", "Imagen de usuario"))
        self.label_34.setText(_translate("FormUsuarios", "Ciudad"))
        self.label_40.setText(_translate("FormUsuarios", "Pais"))
        self.label_41.setText(_translate("FormUsuarios", "Rol"))
        self.BotonCrearUsuario_2.setText(_translate("FormUsuarios", "Crear"))
        self.label_46.setText(_translate("FormUsuarios", "Calle"))
        self.label_47.setText(_translate("FormUsuarios", "Numero"))
        self.label_9.setText(_translate("FormUsuarios", "Nombre"))
        self.label_10.setText(_translate("FormUsuarios", "Apellido"))
        self.label_11.setText(_translate("FormUsuarios", "Correo"))
        self.label_12.setText(_translate("FormUsuarios", "Telefono"))
        self.label_13.setText(_translate("FormUsuarios", "Fecha de nacimiento"))
        self.label_42.setText(_translate("FormUsuarios", "Imagen de usuario"))
        self.label_43.setText(_translate("FormUsuarios", "Ciudad"))
        self.label_44.setText(_translate("FormUsuarios", "Pais"))
        self.label_45.setText(_translate("FormUsuarios", "Rol"))
        self.botoncrearModUsuario.setText(_translate("FormUsuarios", "Modificar"))
        self.label_48.setText(_translate("FormUsuarios", "Calle"))
        self.label_49.setText(_translate("FormUsuarios", "Numero"))
        self.label_3.setText(_translate("FormUsuarios", "USUARIOS"))


    #metodos stackwidget
    def mostrarNuevoUsuario(self):
        self.stackedWidget_2.setCurrentIndex(1)
    def mostrarModificarUsuario(self):
        self.stackedWidget_2.setCurrentIndex(2)
    def mostrarBuscarUsuario(self):
        self.stackedWidget_2.setCurrentIndex(0)