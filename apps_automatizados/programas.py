#bibliotecas
import pyautogui

import time

import subprocess


#navegador
def navegador():
 subprocess.run("start opera " , shell=True)

def calculadora():#calculadora
 subprocess.run("start calc",shell=True)

#arquivos
def arquivos():
  time.sleep(1)
  pyautogui.hotkey('win', 'e')
