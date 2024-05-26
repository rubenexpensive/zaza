import pydicom 
from PyQt5.QtCore import QObject
import matplotlib.pyplot as plt
import os
class basededatos(QObject):
    def __init__(self):
        super().__init__()
        self.__login = '' #loging 
        self.__password = '' 
        self.__carpeta = ""

    def validaruser(self, l, p):
        return self.__login == l and self.__password == p

    def get_path(self, f): 
        self.__carpeta = f
