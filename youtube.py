#bibliotecas
import pyautogui

import time

import subprocess
#pergunta
pergunta = input("Qual video ou playlist deseja pesquisar? ")
#abrir o navegador e youtube
subprocess.run("start opera https://www.youtube.com" , shell=True)

#PESQUISAR VIDEO or playlist
time.sleep(8)

pyautogui.write(pergunta)
pyautogui.press('enter')
#minimize a aba

