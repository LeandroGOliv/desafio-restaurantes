import os

restaurantes = [{"nome":"Hut", "categoria":"Pizzaria", "ativo":False}, 
                {"nome":"Mcdonalds", "categoria":"Fast Food", "ativo":True},
                {"nome":"Praça", "categoria":"Japonesa", "ativo":False}]

def exibir_cabecalho():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n""")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alterar status restaurante")
    print("4. Sair\n")

def finalizar_app(): #DEF = FUNCTION e : = {}
    exibir_subtitulo("Finalizando o app")
    
def voltar_ao_menu_principal():
    input("\nPressione qualquer tecla para voltar ao menu principal: ")
    main()        
    
def opcao_invalida():
    print("Opcao invalida")
    voltar_ao_menu_principal()
    
def exibir_subtitulo(texto):
    os.system("cls")   #no mac CLEAR 
    linha = "*" * len(texto) #coloca as bolinhas conforme o tamanho do texto pego no LEN
    print(linha)
    print(texto)
    print(linha)
    print()
    
def cadastrar_novo_restaurante():
    """ Essa função é responsável por cadastrar um novo restaurante
    
    Inputs:
    -Nome do restaurante
    -Categoria do restaurante
    
    Outputs:
    -Adiciona um novo restaurante a lista de restaurantes
    """ #docstring funciona para explicar o funciona mento de uma funcao
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input("Digite a categoria do restaurante: ")
    dados_do_restaurante = {"nome":nome_do_restaurante, "categoria":categoria, "ativo":False}
    restaurantes.append(dados_do_restaurante) #append = push do js, serve para colocar algo na lista
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo("Listando os restaurantes")
    print(f"{"Nome do Restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Status"} ") #ljust é pra espaçar e deixar alinhadinho
    for restaurante in restaurantes: # para cada item restaurante na lista restaurantes, fazer tal coisa
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        status = "ativado" if restaurante["ativo"] else "desativado"
        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {status}")
        
    voltar_ao_menu_principal()
    
def alterar_status_restaurante():
    exibir_subtitulo("Alternando status do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o status: ")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"] #o not inverte o que desejar
            mensagem = f"O {nome_restaurante} foi ativado com sucesso!" if restaurante["ativo"] else f"O {nome_restaurante} foi desativado com sucesso!" # (foi usado ternario)
            print(mensagem)
            
    if not restaurante_encontrado:
        print("Restaurante não foi encontrado")
            
    voltar_ao_menu_principal()
    
def escolher_opcao():  
    try:  # pede para ele tentar fazer essas instruções, se ele não conseguir como nesse caso que ele não consegue transformar em int, dai ele chama o except
        opcao_escolhida = int(input("Escolha uma opção: "))
        # opcao_escolhida = int(opcao_escolhida)  
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_status_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()    
    except:
        opcao_invalida()
    
def main(): # a ordem das funcoes importa
    os.system("cls")
    exibir_cabecalho() 
    exibir_opcoes()
    escolher_opcao()     

if __name__ == "__main__":
    main()