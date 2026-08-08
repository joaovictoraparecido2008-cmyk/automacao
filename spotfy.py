#bibliotecas
import pyautogui

import time

import subprocess

#pergunta
def pesquisar_musica(): #função para spotify
    print("==============================================")
    print("=                   spotify                  =")
    print("==============================================")
    
    pesquisa_musica = input("Qual musica voce quer pesquisar? ")
    #abrir spotify
    subprocess.run("spotify", shell=True)

    #presquisar musica
    time.sleep(8)
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.write(pesquisa_musica)
    pyautogui.press('enter')

    #clicar 
    time.sleep(3)
    botao_play = pyautogui.locateOnScreen('play.png', confidence=0.7)

    if botao_play:
        pyautogui.moveTo(botao_play, duration=0.4)
        pyautogui.click(botao_play)

        #minimize aba
        pyautogui.hotkey('win', 'down')
    else:
        print("Botão de play não encontrado na tela.")

