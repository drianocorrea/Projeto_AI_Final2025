from mainSearch import mainSearch

# Lista de testes (origem, destino) para verificar
testes = [
    ("Milho", "Geracao_Eletrica"),
    ("Milho", "Etanol_Anidro"),
    ("Milho", "Melaco"),
    ("Cana_de_Acucar", "Acucar_Cristal"),
    ("Cana_de_Acucar", "Etanol_Anidro"),
    ("Cana_de_Acucar", "Etanol_Hidratado"),
    ("Cana_de_Acucar", "Melaco"),
    ("Cana_de_Acucar", "Geracao_Eletrica")
]

def teste_caminhos():
    for origem, destino in testes:
        print(f"\nTestando caminho de {origem} para {destino}:")
        resultado = mainSearch(None, origem, destino, "AMPLITUDE")
        if isinstance(resultado, list):
            print(" → ".join(resultado))
        else:
            print("Caminho não encontrado!")

if __name__ == "__main__":
    teste_caminhos()