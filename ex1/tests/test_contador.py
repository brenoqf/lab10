from contador import contar_palavras

def test_texto_vazio():
    assert contar_palavras("") == {}

def test_uma_palavra():
    assert contar_palavras("teste") == {"teste":1}

def test_duas_palavras():
    assert contar_palavras("bom dia") == {"bom":1, "dia":1}

def test_palavras_repetidas():
    assert contar_palavras("dia a dia") == {"dia":2, "a":1}

def test_palavras_maiusculas():
    assert contar_palavras("dia Dia DIA") == {"dia":3}

def test_quebra_linha():
    assert contar_palavras("bom\ndia") == {"bom":1, "dia":1}

def test_pontucao():
    assert contar_palavras("fim. fim, fim; fim: fim! fim?") == {"fim":6}

def test_so_pontuacao():
    assert contar_palavras(",;:!?") == {}

# def test_hifen():
#     assert contar_palavras("guarda-chuva") == {"guarda-chuva":1}