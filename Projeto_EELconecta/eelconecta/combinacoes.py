def posicao(D1, D2, D3):
    p = ((D1 - 2) * 14) + ((D2 - 730) // 90) + 1
    print(f"P = {p}")
    P = []
    if p < 70:
        for c in range(0,D3):
            P.append(p + c)    
    return P

def bin_str_to_int(bin_str):
    return int(bin_str, 2)

def bin_str_to_int(bin_str):
    val = int(bin_str, 2)
    return val if val != 0 else None  # Ignora opções sem horários

def encontrar_combinacao_sem_conflito(bitmakes_disciplinas, bitmake_analise):
    analise_opcoes = [
        val for opcao in bitmake_analise[0]
        if (val := bin_str_to_int(opcao[0])) is not None
    ]

    disciplinas_ints = []
    for idx, disciplina in enumerate(bitmakes_disciplinas):
        opcoes_validas = [
            val for opcao in disciplina
            if (val := bin_str_to_int(opcao[0])) is not None
        ]
        if not opcoes_validas:
            print(f"Erro: Disciplina {idx+1} não possui nenhuma opção válida (todas com bits zerados).")
            return False
        disciplinas_ints.append(opcoes_validas)

    if not analise_opcoes:
        print("Erro: A disciplina de análise não possui nenhuma opção válida (todas com bits zerados).")
        return False

    n = len(disciplinas_ints)
    caminho = []
    combinacao_valida = [None] * (n + 1)  # +1 para a disciplina de análise

    def backtrack(i, atual):
        if i == n:
            for idx, a in enumerate(analise_opcoes):
                if (atual & a) == 0:
                    # Armazenar opção válida da disciplina de análise
                    combinacao_valida[n] = a
                    print("\n Combinação sem conflito encontrada!\n")
                    for j in range(n):
                        valor = combinacao_valida[j]
                        print(f"Disciplina {j+1}: {format(valor, '070b')}")
                    print(f"Disciplina {n+1} (Análise): {format(a, '070b')}")
                    return True
            return False

        for j, opcao in enumerate(disciplinas_ints[i]):
            if (atual & opcao) == 0:
                caminho.append((j, opcao))
                combinacao_valida[i] = opcao  # Armazena esta opção
                if backtrack(i + 1, atual | opcao):
                    return True
                caminho.pop()
                combinacao_valida[i] = None  # Limpa ao desfazer backtrack

        return False

    if backtrack(0, 0):
        return True
    else:
        print(" Nenhuma combinação sem conflito possível.")
        return False


def bitmake(lista):
    tamanho = len(lista)
    lista_com_bitmake = []

    for N in range(tamanho):
        tamanho1 = len(lista[N])
        linha = []

        for n in range(tamanho1):
            # Cria o "bitmake" inicial com 70 zeros
            bloco = ["0" * 70]
            primeiro_bloco = lista[N][n]
            tamanho2 = len(primeiro_bloco)

            for n1 in range(tamanho2):
                aula_n = primeiro_bloco[n1]
                numero = ''.join(c for c in aula_n if c.isdigit())
                if len(numero) < 5:
                    continue  # ignora entradas inválidas
                D1 = int(numero[0])
                D2 = int(numero[1:5])
                D3 = int(numero[5])
                posicoes = posicao(D1, D2, D3)
                for k in posicoes:
                    if 1 <= k <= 70:
                        bin_list = list(bloco[0])
                        bin_list[k - 1] = '1'
                        bloco[0] = ''.join(bin_list)
                    else:
                        raise ValueError(f"Posição inválida: {k} (de D1={D1}, D2={D2})")

            linha.append(bloco)

        lista_com_bitmake.append(linha)

    return lista_com_bitmake



def tem_combinacao_sem_conflito(horarios_aderidos, em_analise):
    aderidos_bitmake = bitmake(horarios_aderidos)
    print(f"em analise\n{em_analise}\n")
    #tudo certinho até aqui <-
    print(f"Aderidos horarios\n{horarios_aderidos}\n")
    print(f"Variavel que chega = {em_analise}")
    container_em_analise = [em_analise]
    analise_bitmake = bitmake(container_em_analise)
    print(f"Aderidos bitmake\n{aderidos_bitmake}\n")
    print(f"analise bitmake\n{analise_bitmake}\n")


    if encontrar_combinacao_sem_conflito(aderidos_bitmake, analise_bitmake):
        return True
    return False
    



LISTA_1 = [ [['2.0820-2', '4.0820-2', '2.0820-2'],
              ['3.1330-2', '6.1510-2', '3.1330-2'], 
              ['2.1620-2', '4.1620-2', '2.1620-2'], 
              ['2.0730-2', '4.0730-2', '2.0730-2'], 
              ['3.1330-2', '6.1330-2', '3.1330-2'], 
              ['3.2020-2', '6.1830-2', '3.2020-2'], 
              ['2.1330-2', '4.1330-2', '2.1330-2'],
              ['4.1010-2', '6.1010-2', '4.1010-2'],
              ['2.1010-2', '4.1010-2', '2.1010-2']],
                
                [['2.1330-2', '3.1010-2', '5.1330-2'], 
                 ['2.1330-2', '4.1010-2', '5.1330-2'], 
                 ['2.1330-2', '3.1330-2', '5.1330-2']], 
                 
                 [['2.1330-2', '2.1330-2', '2.1330-2'],
                   ['5.1330-2', '5.1330-2', '5.1330-2'], 
                   ['5.1010-2', '5.1010-2', '5.1010-2'], 
                   ['6.0820-2', '6.0820-2', '6.0820-2']]]

LISTA_2 = [['5.0820-2', '6.1010-2'],['5.0820-2', '6.1010-2'],['5.0820-2', '6.1010-2']]

tem_combinacao_sem_conflito(LISTA_1,LISTA_2)
