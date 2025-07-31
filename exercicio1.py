palavras = {
    "cachorro": "dog",
    "gato": "cat",
    "casa": "house",
    "carro": "car",
    "livro": "book"
}
palavra_usuario = input("Digite uma palavra em português: ").strip().lower()
if palavra_usuario in palavras:
    print(f"A tradução de '{palavra_usuario}' é '{palavras[palavra_usuario]}'.")
else:
    print(f"A palavra '{palavra_usuario}' não foi encontrada no dicionário.")
