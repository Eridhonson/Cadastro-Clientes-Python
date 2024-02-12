import json

#Criando um objeto python com os dados (nome, cpf, telefone, e-mail e endereço)

def inserirCliente():
    #Criação e inserção dos dados no arquivo JSON.
    nome = input(f"Digite o nome do cliente: ")
    cpf = input(f"Digite o CPF do cliente: ")
    telefone = input(f"Digite o telefone do cliente: ")
    email = input(f"Digite o e-mail do cliente: ")
    endereco = input(f"Digite o endereço do cliente: ")

    cliente = {
    "nome": nome,
    "CPF": cpf,
    "telefone": telefone,
    "e-mail": email,
    "endereco": endereco
    }

    dados = []

    dados.append(cliente)

#Gravando a string JSON em um arquivo
    with open('clientes.json', 'a') as arquivo:
        json.dump(dados, arquivo, indent=4)
    
    print("Cliente cadastrado.")

def main():
    while True:
        print("1. Cadastrar")
        print("0. Sair")
        interacao = input("Escolha uma opção:")
        if interacao == "1":
            inserirCliente()
        elif interacao == "2":
            break
        else:
            print("Digite uma opção válida.")
            continue

main()