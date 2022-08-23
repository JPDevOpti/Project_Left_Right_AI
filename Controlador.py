# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 00:23:26 2020

@author: Admin
"""

from Modelo import Biosenal
from Vista import InterfazGrafica
import sys
from PyQt5.QtWidgets import QApplication

class Coordinador(object):
    # como el coordinador enlza la vista y el modelo, debe tener acceso a ambos
    def __init__ (self, vista,biosenal):
        self.__mi_vista = vista
        self.__mi_biosenal = biosenal
    #la idea es que la vista pase los datos que carga de la senal al controlador y con esa se cree el objeto de Biosenal
    
    def recibirIca(self,data,epoca):
        
        return self.__mi_biosenal.devolverIca(data,epoca)
        
        
    def recibirDatosSenal(self,data):
        # se le asiganan lo datos a la senal
        #Pasa los datos al modelo
        self.__mi_biosenal.asignarDatos(data)
        
    def devolverDatosSenal(self, x_min, x_max):
        return self.__mi_biosenal.devolverSegmento(x_min, x_max)

    def devolverDatosSenal2(self, y_min, y_max, x_min, x_max, ep_min, ep_max):
        return self.__mi_biosenal.devolverSegmento(y_min, y_max, x_min, x_max, ep_min, ep_max)
    
    def recibirRangos(self,canal_min,canal_max,punto_min,punto_max,epoca_min,epoca_max):
        return self.__mi_biosenal.devolverSegmento2(canal_min,canal_max,punto_min,punto_max,epoca_min,epoca_max)

    def devolverEpoca(self,epoca):
          return self.__mi_biosenal.devolveSegmentoEpoca(epoca)
# se realiza el codigo cliente
def main():
    app = QApplication(sys.argv)
    #creamos la vista
    mi_vista = InterfazGrafica()
    #creamos el modelo
    modelo = Biosenal()
    #creamos el controlador
    controlador = Coordinador(mi_vista,modelo)
    #le asignamos a la vista el controlador
    mi_vista.asignarControlador(controlador)
    
    mi_vista.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
    