# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 19:13:33 2020

@author: Admin
"""

from PyQt5.QtWidgets import  QMainWindow, QVBoxLayout, QFileDialog, QMessageBox, QDialog

from matplotlib.figure import Figure
#Cargar elementos del designer
from PyQt5.uic import loadUi 

#FigureCanvasQTAgg = permite agregar elemntos de tipo Figure dentro de nuestra interfaz
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas 
import numpy as np
#Cargar las señales 
import scipy.io as sio

# import scipy.stats as stats
from scipy.stats import kurtosis

from scipy.stats import skew

from pyentrp import entropy as ent



#Clase que herede de FigureCanvas  para mostrar en la interfaz los graficos matplotlib
#En esta clase se manipula todo lo de los graficos 

class MyGraphCanvas (FigureCanvas):
    #Metodo Constructor
    def __init__(self, width=5, height=4, dpi=100): # se le asigna altura , tamaño y resolucion 
        # se crea objeto figura 
        self.fig = Figure(figsize=(width, height), dpi=dpi) 
        #Añadimos unos ejes
        self.axes = self.fig.add_subplot(1,1,1)
        # se inicializa la clase FigureCanvas con el objeto fig
        FigureCanvas.__init__(self,self.fig)  
        
     
    def graficarSenal(self,senal,x_min=0,x_max=500):
        #se limpia los ejes del grafico
        self.axes.clear()
        #se grafica la senal
        for canal in range(senal.shape[0]):
            self.axes.plot( senal[canal,:,0] + canal*10,label='canal ' + str(canal))
        #Metodos de los axes
        #Fijamos la leyenda en la parte superior derecha.
        self.axes.legend(loc='upper right')
        #Etiquetas para el eje x
        self.axes.set_xlabel('Tiempo (mS)')
        self.axes.set_ylabel('Voltaje(μV)')
        self.axes.set_title('Señales EEG')
        #Fijamos los limites
        # self.axes.set_ylim([-20,100])
        self.axes.set_xlim(x_min, x_max)
        #Marcas para el eje x
        self.axes.set_xticks(np.arange(0,500,50))
        #se actualiza el grafico
        self.axes.figure.canvas.draw()
            
    def graficarCampo1(self, senal):
        #limpiamos el grafico
        self.axes.clear()
        #ingresamos el nuevo grafico iterando entre canales y dejando espacio entre ellos
        
        for c in range(senal.shape[0]):
            #self.axes.plot(senal[c,:] + c*10)
            self.axes.plot(senal[c,:] + c*10,label='canal ' + str(c))
        
            self.axes.legend(loc='upper right')
            self.axes.set_xlabel('Tiempo (mS)')
            self.axes.set_ylabel('Voltaje (μV)')
            self.axes.set_title('Señales EEG')
            
            # self.axes.set_ylim([-20,100])
            self.axes.set_xlim(0,500)
            self.axes.set_xticks(np.arange(0,500,50))
            #se actualiza el grafico
     
            self.axes.figure.canvas.draw()
            
    def graficarCampo2(self,senal,punto_min,punto_max):
        #se limpia los ejes del grafico
        self.axes.clear()
        #se grafica la senal
        for canal in range(senal.shape[0]):
            self.axes.plot(np.arange(punto_min,punto_max), senal[canal,:] + canal*10,label='canal ' + str(canal))
            
            self.axes.legend(loc='upper right')
            self.axes.set_xlabel('Tiempo (mS)')
            self.axes.set_ylabel('Voltaje (μV)')
            self.axes.set_title('Señales EEG')
            # self.axes.set_ylim([-20,100])
            self.axes.set_xlim(punto_min,punto_max)
            self.axes.set_xticks(np.arange(punto_min,punto_max,100))
            #se actualiza el grafico
            self.axes.figure.canvas.draw()   
            
    def graficarCampo3(self, senal_ica):
        #limpiamos el grafico
        self.axes.clear()
        #ingresamos el nuevo grafico iterando entre canales y dejando espacio entre ellos
        
        # print("señal ica:"+ str(senal_ica))
        # print("Tipo de señal ica en campo3")
        # print(type(senal_ica))
        # print(senal_ica)
        # print("Línea 104")
        for c in range(senal_ica.shape[0]):
            #self.axes.plot(senal[c,:] + c*10)
            self.axes.plot(senal_ica[:,c] + c*(1/5),label='fuente ' + str(c))
        
            self.axes.legend(loc='upper right')
            self.axes.set_xlabel('Tiempo (mS)')
            self.axes.set_ylabel('Voltaje (μV)')
            self.axes.set_title('Señales ICA')
            
            # self.axes.set_ylim([-20,100])
            self.axes.set_xlim(0,500)
            self.axes.set_xticks(np.arange(0,500,50))
            #se actualiza el grafico
     
            self.axes.figure.canvas.draw()
         
            
  
class InterfazGrafica(QMainWindow):
    # metodo constructor
    def __init__(self,ppal = None):
        super(InterfazGrafica, self).__init__(ppal)# se hereda la clase padre 
        #se carga el diseño
        loadUi('interfaz_proyecto.ui',self)
        # se llama la rutina donde se configura la interfaz 
        self.__mi_ventana_principal = ppal
        
        #self.senal_ica = []
        
        self.setup() # para configurar los slots
        #se muestra la interfaz 
        self.show()
        
        
        
    # def asignarICA(self, ica):
    #     self.senal_ica = ica
    
    def asignarICA(self, ica):
        self.senal_ica = ica
        # print(self.senal_ica)
        # print("línea 147")
        
    def retornarICA(self):
        # print("línea 150")
        return self.senal_ica
        
    
    # def asignarICA(self, ica):
    #     self.senal_ica = ica
        
        # self.__
            
    def setup(self):
        
        # los layout permiten organizar widgets en un contenedor 
        Layout=QVBoxLayout() # permite acomodar añadir al campo grafico elementos grapcanvas
        #le asignamos al Layout ese widget campo grafico
        self.campo_grafico.setLayout(Layout)
        #se crea un ojeto para el manejo de los graficos 
        self.sc = MyGraphCanvas( width=5, height=4, dpi=100)
        # llamamos al Layout y se le añade el campo grafico
        Layout.addWidget(self.sc)
        
        #Creamos dos objetos Graphcanvas y los añadimos a la interfaz.
        Layout2 =QVBoxLayout()
        self.campo_grafico2.setLayout(Layout2)
        self.sc1 = MyGraphCanvas( width=5, height=4, dpi=100)
        Layout2.addWidget(self.sc1)
    
        
        #se organizan las señales slots
        #A cada señal se le asocia su respectivo slot
        self.boton_cargar.clicked.connect(self.cargarSenal)# se define el slot 
        self.boton_cargar.clicked.connect(self.senalIca)
        self.boton_adelante.clicked.connect(self.adelantarSenal)
        self.boton_adelante.clicked.connect(self.senalIca)
        self.boton_atras.clicked.connect(self.atrasarSenal)
        self.boton_atras.clicked.connect(self.senalIca)
        
        
        self.boton_graficar.clicked.connect(self.recuperarInfo)
        
        self.boton_sumar.clicked.connect(self.sumarCanales)
        self.boton_restar.clicked.connect(self.restarCanales)
        #Se ponen en False cuando inicalizamos la interfaz ya que aun no hemos cargado la señal.
        self.boton_adelante.setEnabled (False)
        self.boton_atras.setEnabled (False)
        
        self.boton_ica.clicked.connect(self.abrirVentana)
        
    
    def abrirVentana(self):
        icaRetornada = self.retornarICA()
        ventana_ica = VentanaIca(self)
        ventana_ica.recuperarICA(icaRetornada)
        #la ventana principal se oculte
        # self.hide()
        #la ventana paciente se hace visible
        ventana_ica.show()
        
        
    def cargarSenal(self):
        
        #se abre el cuedro de dialogo para cargar un archivo .mat
        #le pasamos la clase padre(Interfaz grafico), titulo y el filtro de los archivos 
        archivo_cargado, _= QFileDialog.getOpenFileName(self,'Abrir señal','','Todos los archivos (*);; Archivos mat (*.mat)')
        #si le damos cancelar el archivo se vuelve none y no hace nada.
        if archivo_cargado!= None :
            
            # 1 CARGAR EL ARCHIVO
            #Devuelve el diccionario
            data = sio.loadmat(archivo_cargado)
            
            #Necesitamos la clave data
            data = data['X']
            # print("Dimensionaes data original, 222")
            # print(data.shape)
            data = np.transpose(data,[1,0,2]) #shape 
            
        
            self.operar_senal = data
            self.cambiar_epoca = data
            self.datos_ica = np.transpose(data, [2, 0, 1])
            # print("228, dimensión datos_ica")
            # print(self.datos_ica.shape)
            
            dimension = data.ndim
            
            if dimension != 3:
                 texto_resultado = "Dimensiones no validas" 
                 msg = QMessageBox(self)
                 msg.setIcon(QMessageBox.Information)
                 msg.setText(texto_resultado)
                 msg.setWindowTitle("ERROR")
                 msg.show()
                 
            elif dimension ==3:
                canales, puntos, epocas = data.shape
                
                #print(archivo_cargado)
       
                
                self.__mi_coordinador.recibirDatosSenal(data)
                #Mostrar los datos entre 0 y 500
                self.x_min = 0
                self.x_max = 500
                self.epoca = 0
                
                
                
                
                canales = data.shape[0]
                epocas = data.shape[2]
                dimen = data.ndim
                
                datos = ""
                k = 0
                
                for i in range(canales):
                    c = data[i, self.epoca, :]
                    promedio = round(np.mean(c),3)
                    desviacion = round(np.std(c),3)
                    minim = round(np.min(c),3)
                    maxim = round(np.max(c),3)
                    #kur = kurtosis(c,fisher=True)
                    #print(round(float(kur), 3))
                    #print(kur)
                
                
                    
                    t = "\nCanal " + str(k) + ":" + " Promedio: " + str(promedio) + "  Desviación estandar: " + str(desviacion) + " Valor mínimo: " + str(minim) + "  Valor máximo: " + str(maxim)
                    datos = datos + t
                    k = k + 1
                self.info_senal.setText("Canales: " + str(canales) + " Épocas: " + str(epocas) + " Dimensiones: " + str(dimen) + datos)
                self.sc.graficarSenal(self.__mi_coordinador.devolverDatosSenal(self.x_min,self.x_max),self.x_min,self.x_max)
                self.boton_adelante.setEnabled (True)
                self.boton_atras.setEnabled (True)
                #kur = kurtosis(data[1, 1, :])
                #print(kur)
         
    def recuperarInfo(self):
      
        canal_min = self.canal_inicial.value()
        canal_max = self.canal_final.value()
        punto_min = self.punto_inicial.value()
        punto_max = self.punto_final.value()
        epoca_min =self.epoca_inicial.value()
        epoca_max = self.epoca_final.value()
        
        if canal_min >= canal_max or punto_min >= punto_max or epoca_min >= epoca_max:
            texto_resultado = "Rangos invalidos" 
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setText(texto_resultado)
            msg.setWindowTitle("ERROR")
            msg.show()
                
        else:
            segmento = self.__mi_coordinador.recibirRangos(canal_min,canal_max,punto_min,punto_max,epoca_min,epoca_max)
                
            canales, puntos, epocas = segmento.shape
            segmento = np.reshape(segmento,(canales, puntos*epocas))
            self.sc1.graficarCampo2(segmento,punto_min*(epoca_max - epoca_min),punto_max*(epoca_max - epoca_min))
           
    def asignarControlador(self,controlador):
        self.__mi_coordinador = controlador
        
    def sumarCanales(self):
        
        data = self.operar_senal
        punto = data.shape[1]
        self.canal_min = self.canal_inicial.value()
        self.canal_max = self.canal_final.value()
        suma = np.add(data[self.canal_min, :, 0], data[self.canal_max, :, 0])
        senal_suma = np.reshape(suma,(1, data.shape[1]))
        self.sc1.graficarCampo2(senal_suma, 0, punto)
        
        

    def restarCanales(self):
 
        data = self.operar_senal
        punto = data.shape[1]
        self.canal_min = self.canal_inicial.value()
        self.canal_max = self.canal_final.value()
        resta = np.subtract(data[self.canal_min, :, 0], data[self.canal_max, :, 0])
        senal_resta = np.reshape(resta,(1, data.shape[1]))
        self.sc1.graficarCampo2(senal_resta, 0, punto)
       


    def adelantarSenal(self):
        self.epoca = self.epoca + 1 
      
        
        data = self.cambiar_epoca
        #print(data)
        
        canales = data.shape[0]
        epocas = data.shape[2]
        dimen = data.ndim
              
        datos = ""
        k = 0
        for i in range(canales):
            c = data[i, self.epoca , :]
            promedio = round(np.mean(c),3)
            desviacion = round(np.std(c),3)
            minim = round(np.min(c),3)
            maxim = round(np.max(c),3)
            #kur = kurtosis(c,fisher=True)
            #print(round(float(kur), 3))
            #print(kur)
        
        
            
            t = "\nCanal " + str(k) + ":" + " Promedio: " + str(promedio) + "  Desviación estandar: " + str(desviacion) + " Valor mínimo: " + str(minim) + "  Valor máximo: " + str(maxim)
            datos = datos + t
            k = k + 1
        self.info_senal.setText("Canales: " + str(canales) + " Épocas: " + str(epocas) + " Dimensiones: " + str(dimen) + datos)
        self.sc.graficarSenal(self.__mi_coordinador.devolverDatosSenal(self.x_min,self.x_max),self.x_min,self.x_max)
        self.boton_adelante.setEnabled (True)
        self.boton_atras.setEnabled (True)
        #kur = kurtosis(data[1, 1, :])
        #print(kur)
        self.sc.graficarCampo1(self.__mi_coordinador.devolverEpoca(self.epoca))
            
    def atrasarSenal(self):
        #no me puedo atrasar si estoy en menos del rango
        if self.epoca < 1:
            return None
            
        self.epoca = self.epoca - 1
        
        
        data = self.cambiar_epoca
        #print(data)
        
        canales = data.shape[0]
        epocas = data.shape[2]
        dimen = data.ndim
              
        datos = ""
        k = 0
        for i in range(canales):
            c = data[i, self.epoca , :]
            promedio = round(np.mean(c),3)
            desviacion = round(np.std(c),3)
            minim = round(np.min(c),3)
            maxim = round(np.max(c),3)
            #kur = kurtosis(c,fisher=True)
            #print(round(float(kur), 3))
            #print(kur)
        
        
            
            t = "\nCanal " + str(k) + ":" + " Promedio: " + str(promedio) + "  Desviación estandar: " + str(desviacion) + " Valor mínimo: " + str(minim) + "  Valor máximo: " + str(maxim)
            datos = datos + t
            k = k + 1
        self.info_senal.setText("Canales: " + str(canales) + " Épocas: " + str(epocas) + " Dimensiones: " + str(dimen) + datos)
        self.sc.graficarSenal(self.__mi_coordinador.devolverDatosSenal(self.x_min,self.x_max),self.x_min,self.x_max)
        self.boton_adelante.setEnabled (True)
        self.boton_atras.setEnabled (True)
        
        #kur = kurtosis(data[1, 1, :])
        #print(kur)
        self.sc.graficarCampo1(self.__mi_coordinador.devolverEpoca(self.epoca))       
    
        
    def senalIca(self):
        
        data = self.datos_ica
        
        self.senal_ica = self.__mi_coordinador.recibirIca(data,self.epoca)
        self.senal_ica = self.senal_ica[0]
        # print ("ESTA ES LA ESE: ")
        # print(type(self.senal_ica))
        # print("Epoca")
        # print(self.epoca)
        
        
        # SI = InterfazGrafica()
        
        self.asignarICA(self.senal_ica)
        
        # print(self.senal_ica)
        # print("Línea 412")
        # SI.asignarICA(self.senal_ica)
        # print(self.senal_ica)
        #asignarICA(senal_ica)
        # x = self.retornarICA()
        # print(x)
        # print("línea 414")
        
        # # x = SI.retornarICA()
        # print("línea 433")
        # # print(x)
        # # print(type(x))
        # print("línea 436")
        
    # x = senalIca(self.senal_ica)
        
        
        # self.__mi_ventana_principal.graficarICA(self.senal_ica)
        
    
        
                
        #self.__mi_ventana_principal.recibirSenalIca(self.senal_ica)
    
        
class VentanaIca(QDialog):
    
     def __init__(self, ppal = None):
        super(VentanaIca, self).__init__(ppal)
        loadUi("ventana_ica.ui", self)

        self.setup()
        
     def setup(self):
         #Creamos dos objetos Graphcanvas y los añadimos a la interfaz.
         
         self.boton_graficar_ica.clicked.connect(self.graficarICA)
         
         
         Layout3 =QVBoxLayout()
         self.campo_grafico3.setLayout(Layout3)
         self.sc2 = MyGraphCanvas( width=5, height=4, dpi=100)
         Layout3.addWidget(self.sc2)
         
         #self.sc2.graficarCampo3(senal_ica)
         
    
     # def recibirSenalIca(self,senal_ica):
     #     self.sc2.graficarCampo3(senal_ica)
     
     def recuperarICA(self, ica2):
         self.ica2 = ica2
         # self.ica2 = np.transpose(self.ica2, (1, 2, 0))
         # print(self.ica2.shape)
         # print(self.ica2)
         # print(type(self.ica2))
         # print("Se recuperó el ICA, línea 481")
         return self.ica2
         
     
     
     def graficarICA(self):
         
         # print("graficar ICA inicio")
         # print(self.ica2)
         # print("línea 492")
         # x = InterfazGrafica.retornarICA(self)
         # print ("Senal ica antes de pasarla: " + str(y))
         # print(self.ica2.shape)
         
         # print(type(self.ica2))
         puntos = self.ica2.shape[0]
         canales = self.ica2.shape[1]
         dimen = self.ica2.ndim
         # print((canales))
         # print(type(canales))
         datos = ""
         k = 0
        
         for i in range(canales):
             c = self.ica2[i, :]
             promedio = round(np.mean(c),3)
             desviacion = round(np.std(c),3)
             minim = round(np.min(c),3)
             maxim = round(np.max(c),3)
             kur = round(kurtosis(c,fisher=True),3)
             sk = round(abs(skew(self.ica2[i])),3)
             se = round(abs(float(ent.sample_entropy(self.ica2[i], 1, 0.2*desviacion ))),3)
             
             # print(round(float(kur), 3))
             #print(kur)
            
             t = "\nCanal " + str(k) + ":" + " Promedio: " + str(promedio) + "  Desviación estandar: " + str(desviacion) + " Valor mínimo: " + str(minim) + "  Valor máximo: " + str(maxim) + "\nKurtosis: " + str(kur) + " Skewness: " + str(sk) + " Sample Entropy: " + str(se)
             datos = datos + t
             k = k + 1
         self.info_senal_ica.setText("Canales: " + str(canales) + " Dimensiones: " + str(dimen) + datos)
         
         
         self.sc2.graficarCampo3(self.ica2)
         
         
        

        
            
        
        
        
        
    
    
        
        
        
