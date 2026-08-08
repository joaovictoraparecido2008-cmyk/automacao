from spotfy import pesquisar_musica
from youtube import youtube

#LISTA DE NOMES E ABREVIAMENTOS
youtube_names = ['youtube', 'yt', 'y']
spotify_names = ['spotify', 'sp', 's']
while True:
    print("==============================================")
    print("=                                            =") 
    print("=            Central de Pesquisa             =")
    print("=                                            =")
    print("==============================================")

    plataforma = input("Qual plataforma deseja pesquisar? (youtube/spotify) ")

    if plataforma.lower() in youtube_names:
        youtube() #chamada da função youtube
    elif plataforma.lower() in spotify_names:
        pesquisar_musica() #chamada da função pesquisar_musica
    else:
        print("Plataforma não reconhecida. Por favor, escolha entre 'youtube' ou 'spotify'.")
    if input("Deseja pesquisar novamente? (s/n) ").lower() != 's':
        break