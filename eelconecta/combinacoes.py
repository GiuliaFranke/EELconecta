def posicao(D1, D2, D3):
    p = ((D1 - 2) * 14) + ((D2 - 730) // 90) + 1
    #print(f"\n\nP = {p}\n\n")
    P = []
    for c in range(0,D3):
        P.append(p + c)


    return P

def bin_str_to_int(bin_str):
    return int(bin_str, 2)

def encontrar_combinacao_sem_conflito(bitmakes_disciplinas, bitmake_analise):
    analise_opcoes = [bin_str_to_int(opcao[0]) for opcao in bitmake_analise[0]]

    disciplinas_ints = []
    for disciplina in bitmakes_disciplinas:
        opcoes = [bin_str_to_int(opcao[0]) for opcao in disciplina]
        disciplinas_ints.append(opcoes)

    n = len(disciplinas_ints)
    caminho = []

    def backtrack(i, atual):
        if i == n:
            for idx, a in enumerate(analise_opcoes):
                if (atual & a) == 0:
                    print("\n Combinação sem conflito encontrada!\n")
                    for j, (bloco_idx, bloco_val) in enumerate(caminho):
                        print(f"Disciplina {j+1}: opção {bloco_idx} -> {format(bloco_val, '070b')}")
                    print(f"Disciplina 4: opção {idx} -> {format(a, '070b')}")
                    return True
            return False

        for j, opcao in enumerate(disciplinas_ints[i]):
            if (atual & opcao) == 0:
                caminho.append((j, opcao))
                if backtrack(i + 1, atual | opcao):
                    return True
                caminho.pop()

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
    analise_bitmake = bitmake(em_analise)
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

LISTA_2 = [[['5.0820-2', '6.1010-2']]]

tem_combinacao_sem_conflito(LISTA_1,LISTA_2)
