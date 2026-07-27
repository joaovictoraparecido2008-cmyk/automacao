#bibliotecas
import pyautogui
import time
import subprocess
#pergunta
musica = input("Qual musica voce quer pesquisar? ")
#abrir spotify
subprocess.run("spotify", shell=True)
#presquisar musica
time.sleep(8)
pyautogui.hotkey('ctrl', 'l')
pyautogui.write(musica)
pyautogui.press('enter')
#clicar 
time.sleep(3)
play = pyautogui.locateOnScreen('play.png', confidence=0.7)
pyautogui.click(play)
#fechar aba
pyautogui.hotkey('win', 'down')