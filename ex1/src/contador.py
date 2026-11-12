PONTUACAO = ".,;:!?"


def contar_palavras(texto):
    contagem = {}
    for bruto in texto.lower().split():
        palavra = bruto.strip(PONTUACAO)
        if palavra:
            contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem