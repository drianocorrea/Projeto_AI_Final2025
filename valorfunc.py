def valorfunc(v1, v2):
    # v1 = 3
    # v2 = 2
    valor = sum([v1, v2])
    return valor

# print(valorfunc())


def compara(selecao):
    # selecao = 1
    if selecao == "1":
        mostra1 = "Seleção 1"
        #print("Seleção 1")
        return mostra1
    elif selecao == "2":
        print("Seleção 2")
    elif selecao == "3":
        print("Seleção 3")
    else:
        print("Seleção inválida")
    return selecao
