from apps_automatizados.youtube import youtube
from apps_automatizados.spotfy import pesquisar_musica
from apps_automatizados.programas import arquivos ,calculadora, navegador


while True:
    print("==============================================")
    print("=                  AUTOMAÇÃO                  =")
    print("==============================================")

    print("(1) YouTube")
    print("(2) Spotify")
    print("(3) Programas")
    print("==============")
    print("(0) Sair")

    plataforma = input("Digite um número: ")

    if plataforma == "1":
        youtube()

    elif plataforma == "2":
        pesquisar_musica()

    elif plataforma == "3":

        while True:
            print()
            print("==============================================")
            print("=                  PROGRAMAS                 =")
            print("==============================================")

            print("(1) Navegador")
            print("(2) Calculadora")
            print("(3) Arquivos")
            print("(0) Voltar")

            programa = input("Digite um número: ")

            if programa == "1":
                print("Navegador")
                navegador()

            elif programa == "2":
                calculadora()

            elif programa == "3":
                print("Arquivos")
                arquivos()

            elif programa == "0":
                break

            else:
                print("Opção inválida.")

    elif plataforma == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")