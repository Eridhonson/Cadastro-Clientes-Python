import json

#Criando um objeto python com os dados (nome, cpf, telefone, e-mail e endereço)

cliente = {
    "nome": "",
    "CPF": 0,
    "telefone": 0,
    "e-mail": "mail@mail",
    "endereco": ""
}

while True:
    for data in cliente:
        cliente[data] = input(f"Digite o {data} do cliente: ")
    interacao = input("Deseja cadastrar um novo cliente? (sim / não)").lower()
    if interacao == "não":
        break
    elif interacao == "sim":
        continue
    else:
        print("Digite uma resposta válida.")
        break

jsonStr = json.dumps(cliente)

#Gravando a string JSON em um arquivo
with open('clientes.json', 'a') as arquivo:
    arquivo.write('[' + jsonStr + ']\n')