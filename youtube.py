#bibliotecas
import pyautogui


import time

import subprocess

lista = ['sim','s', 'yes','y']# lista de sins que pode se digitar para minimizar a aba do youtube
#funcvao principal do youtube
def youtube_iniciar():
    #pergunta
    pesquisar = input("Qual video ou playlist deseja pesquisar? ")

    #abrir o navegador e youtube
    subprocess.run("start opera https://www.youtube.com" , shell=True)
    time.sleep(9)

    #PESQUISAR VIDEO or playlist
    pesquisa = pyautogui.locateOnScreen('pesquisa.png', confidence=0.7)
    if pesquisa:
        pyautogui.click(pesquisa)

        #digite 
        pyautogui.write(pesquisar)
        pyautogui.press('enter')
       
        #clicar
        time.sleep(2)

        videos = pyautogui.locateOnScreen('videos.png', confidence=0.8)
        if videos:
         pyautogui.click(videos)

         time.sleep(2 )
         pyautogui.click(x=609, y=326)#inicia o video
        else:
         print("Botão de pesquisa não encontrado na tela.")

    else:
        print("Botão de pesquisa não encontrado na tela.")


#essa funcao serve para minimizar a aba do youtube e deixar o video em uma janela flutuante
def janela_flutuante():
    #minimize ou nao a janela do navegador
    time.sleep(4)
    pyautogui.moveTo(x=509, y=326, duration=1.5)  # Move o mouse para a posição do vídeo

    #verificar o botao e clicar nele

    time.sleep(2)

    minimizar = pyautogui.locateOnScreen('minimize.png',confidence=0.7)
    if minimizar:
        time.sleep(2)
        pyautogui.moveTo(minimizar, duration=0.4)
        pyautogui.click(minimizar)

        #minimize aba
    
        pyautogui.hotkey('win', 'down')
    else:
        print("Botão de minimizar não encontrado na tela.")



#cabeçario
def youtube():
    
    print("==============================================")
    print("=            Pesquisa no YouTube             =")
    print("==============================================")


    minimizar = input("Deseja minimizar a aba do youtube? (sim/não) ")

    youtube_iniciar() #chamada da função youtube



    if minimizar.lower() in lista:

        janela_flutuante() #chamada da função janela_flutuante

