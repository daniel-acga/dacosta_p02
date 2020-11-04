#!/home/dacosta/anaconda3/bin/python3.8
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 08:59:16 2020

@author: dacosta
"""

##Práctica 02 - Herramientas bioinformáticas en Python
##4/11/2020
##Por Daniel E. Acosta

def descuento (total):
    if total >= 100:
        desc = total*.10 
        print ("Pago neto: ", total - desc)
    else:
        print ("Pago neto: ", total)

descuento(400)    



def area_triangulo (b,h):
    area = (b*h)/2
    print ("El valor del área es: ", round(area, 2))

area_triangulo(5, 15.99098)



def IMC (m, h):
    if h == 0 or m == 0:
        print ("No es posible calcular el IMC")  
    elif m > 0 and 0 > h < 2.3:
        i = (m/ (h**2))  
        print ("El valor del IMC  es: ", (i))
    elif h >= 2.3:                          #Record de altura máxima en metros
        h = h/100
        i = (m/ (h**2))  
        print ("El valor del IMC  es: ", (i))

IMC (58, 173)