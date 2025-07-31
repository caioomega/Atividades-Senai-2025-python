frutas = {}
for i in range(3):
    fruta = input("digite o nome da fruta: ").strip().lower()
    preco = float(input(f"digite o preço por quilo da fruta {fruta}: "))
    frutas[fruta] = preco
    for chave, valor in frutas.items():
        print(f"{chave} - R$ {valor:.2f}")