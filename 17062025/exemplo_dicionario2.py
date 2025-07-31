#declarandoo diicionario
supermercado = {
    "café": 15.00,
    "achocolatado": 10.00,
    "pao": 5.00,
    "arroz": 8.00,  
}
print("**"*30)
for chave,valor in supermercado.items():
    print(f"{chave} - R$ {valor:.2f}") 
    #escolherndo produto
print("**"*30)
while True:
    produto = input("Digite o nome do produto que deseja pesquisar: ").strip().lower()
    if produto in supermercado:
        print(f"O produto {produto} que custa R$ {supermercado[produto]:.2f}")
        break
    else:
        print("Produto não encontrado, tente novamente.")