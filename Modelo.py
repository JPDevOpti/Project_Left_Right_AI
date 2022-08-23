# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 00:49:16 2020

@author: Admin
"""


from sklearn.decomposition import FastICA

# esta clase maneja toda la logica para manejar la bioseÃ±al
class Biosenal(object):
    # el metodo constructor recibe todos los datos si no se entregan por defecto estaran vacios
    def __init__(self,data=None):
        if data is not None:
            self.asignarDatos(data)
        else:
            self.data=[]
            self.canales=0
            self.puntos=0
            self.epocas=0 
    
    def asignarDatos(self,data):
        self.data=data
        self.canales = data.shape[0] #Le asigna las filas
        self.puntos = data.shape[1] #Le asignamos las columnas
        self.epocas = data.shape[2] #Le asignamos las submatrices
    
    def devolverSegmento (self, x_min, x_max):
        if x_min >= x_max:
            return None
        #Develve todas las filas y las columnas desde x_min hasta x_max
        return self.data[:,x_min:x_max]

    
    def devolverSegmento2(self,canal_min,canal_max,punto_min,punto_max,epoca_min,epoca_max):
        if canal_min >= canal_max:
            if punto_min >= punto_max:
                if epoca_min >= epoca_max:
                    return None   
                
        return self.data[canal_min:canal_max,punto_min:punto_max,epoca_min:epoca_max]
        
    # def escalar_senal(self,x_min,x_max,escala):
    #     # el slicing no genera copia de los datos sino qye devielve un segmento de los originales 
    #     # para no modificar la original se debe hacer una copia
    #     if x_min >= x_max:
    #         return None
    #     copia_data = self.data[:,x_min,x_max].copy()
    #     return copia_data*escala
    
    def devolveSegmentoEpoca(self,epoca):
        return self.data[:,:,epoca]
    
    def devolverIca(self,data,epoca):
        S = []
        A = []
        
        ica = FastICA(n_components=len(data[0]), max_iter=1000, tol=0.1)
        S_ = ica.fit_transform(data[epoca].T)  # Reconstruct signals
        A_ = ica.mixing_  # Get estimated mixing matrix
            
        S.append(S_)
        A.append(A_)
        # print("Modelo 65")
        # print(S[0].shape)
            
        # print("Hola" + str(S))
        # print("Es a:" + str(A))
        return S
        
        