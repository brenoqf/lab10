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

def test_hifen():
    assert contar_palavras("guarda-chuva") == {"guarda-chuva":1}

# c) 9 GREENs, sem nenhum RED
# 8c7a0db (HEAD -> main) GREEN: teste de palavra com hífen retornou a palavra corretamente, sem dividir em duas palavras diferentes
# cb6d637 GREEN: teste de só pontuação retornou um dicionário vazio
# a26fe19 GREEN: teste de separação de uma mesma palavra por várias pontuações retornou um dicionário com a palavra repetida 6 vezes sem a interferência da pontuação
# 08e35da GREEN: teste de quebra de linha(\n) entre 2 palavras retornou um dicionário com as 2 palavras escritas corretamente
# 32d9772 GREEN: teste de uma mesma palavra repetida 2 vezes retorna um dicionário com essa mesma palavra com 2 repetições
# bda8975 GREEN: teste de uma mesma palavra repetida 2 vezes retorna um dicionário com essa mesma palavra com 2 repetições
# c28a9d1 GREEN: teste de 2 palavras diferentes registra um dicionário com as 2 palavras
# f543bc4 GREEN: teste de uma palavra registra dicionário com a palavra identificada 1 vez
# 6e33bbd GREEN: texto vazio gera dicionário vazio
# 98c4581 (origin/main, origin/HEAD) Initial commit

# d) Todos os testes passaram na primeira execução, porque o código principal aborda as exceções que deveriam funcionar.

# e) 4 ramos percorridos e gerou 12 mutantes, todos foram mortos 