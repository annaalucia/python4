import os

restaurantes = ["Bombaxa do boi gordo", "Recanto Banha boa "]

def mostra_subtitulo(texto):
    os.system("clear")
    os.system("cls")
    print(texto)
    print()

def finalizar_app():
    os.system("clear")
    os.system("cls")
    print("Finalizando o app\n")
    mostra_subtitulo()

def escolher_opcoes():
    print("Programa Expresso\n")
    print("1 - Cadastrar restaurante")
    print("2 - Listar restaurante")
    print("3 - Ativar restaurante")
    print("4 - Sair\n")

def voltar_ao_menu_principal():        
    input("Digite uma tecla para voltar para o menu principal:")
    main()

def opcao_invalida():
    print("Opção inválida\n")
    voltar_ao_menu_principal()
    
def chamar_nome_do_app():
    print("Restaurante Expressao\n")

def listarRestaurantes(): 
    print('Listando os Restaurantes')
    for restaurante in restaurantes:
        print(f'-{restaurantes}')
        voltar_ao_menu_principal()
        
def cadastrar_novo_restaurante():
    os.system('cls')
    nome_do_restaurante = input("Digite o nome do novo restaurante: ")
    restaurantes.append(nome_do_restaurante)
    print(f"Você cadastrou o restaurante:-{nome_do_restaurante}")
    voltar_ao_menu_principal()
    
def escolher_opcoes():    
    try:
        opcaodigitada = int(input("Digite a opção desejada: "))
        if opcaodigitada == 1:
            #print("Você escolheu cadastrar restaurante\n")
            cadastrar_novo_restaurante()
        elif opcaodigitada == 2:
            listarRestaurantes()
        elif opcaodigitada == 3:
            print("Você escolheu ativar restaurante\n")
        elif opcaodigitada == 4:
            #print("Você escolheu sair do aplicativo\n")
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

if _name_ == "_main_":
    finalizar_app()
    main()
    