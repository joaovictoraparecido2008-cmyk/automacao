from spotfy import pesquisar_musica
from youtube import youtube

#LISTA DE NOMES E ABREVIAMENTOS
youtube_names = ['youtube', 'yt', 'y']
spotify_names = ['spotify', 'sp', 's']
while True:
    print("==============================================")
    print("=                  AUTOMACAO                 =")
    print("==============================================")

    print('(1) youtube')
    print('(2) spotify')
    print('(3) sair')

    plataforma = input('digite um numero: ')

    #chamada das funções de acordo com a escolha do usuario
    if plataforma == '1':
        youtube() #chamada da função youtube

    elif plataforma == '2':
        pesquisar_musica() #chamada da função pesquisar_musica
    elif plataforma == '3':
        print("Saindo...")
        break
    
    else:
        print("Opção inválida. Digite novamente.")

        