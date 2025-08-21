from eelconecta.choque import extrair_horarios
from eelconecta.combinacoes import tem_combinacao_sem_conflito
import os
from eelconecta import dicionario_eletrica, dicionario_eletronica
from eelconecta.dicionario_eletrica import disciplinas_eletrica
from eelconecta.dicionario_eletronica import disciplinas_eletronica


#Lógica em análise

def conflitos(codigos, creditos, horarios_aderidos): #Esse parametro são as disciplinas que vão ser analizadas até o momento   
    pdf_path = os.path.join(os.path.dirname(__file__), "cadastro_de_turmas.pdf")
    print(f"\n\n\n codigos = {codigos}\n")
    
    FORCADO = [codigos]
    horarios = extrair_horarios(pdf_path, FORCADO, creditos)

    disciplinas_horarios = horarios
    #print(len(disciplinas_horarios))
    print(f"\n\nvariavel que sai = {disciplinas_horarios}\n\n")
    
    

    if tem_combinacao_sem_conflito(horarios_aderidos, disciplinas_horarios):
        print("Existe ao menos uma combinação sem conflito!")
        return True
    else:
        print("Todas as combinações geram conflito. ")
        print(disciplinas_horarios)

def recomendacao(subjects_released, disciplinas, carga_max):
    #passo a passo
    # 1 -> Asumir uma dsciplina candidata
    # 2 -> Verificar todas as disiplinas do discionario com a condição de ter como prérequisito a disciplina candidata
    # 3 -> Adiciona essa diciplina como um sinônimo da candidata 
    # 4 -> Verifica a fase e se possui mais diciplinas para ser liberada
    # 5 -> Aplica a f_teta e adiciona esse valor a  disiplina 
    # 6 -> Somatório de todos os pesos 
    # 7 -> Assume outra disiciplina (return ->1)
    # ** NOTE delta f jamais sera negativo pois se uma disiplina exige a disciplina candidata como pré requisito ela jamais estara tera uma fase menor que F0 
    if disciplinas == 'eletrica':
        disciplinas = disciplinas_eletrica
    else:
        disciplinas = disciplinas_eletronica
       
    dis_liberadas = subjects_released  # Disciplinas que podem ser cursadas
    status = {}  # Dicionário para armazenar informações sobre cada disciplina liberada

    def f_teta(f1, f0, n):
        """
        Função de peso para avaliar a importância de uma disciplina com base em sua dependência de outras.
        
        Parâmetros:
            f1 (int): Fase da disciplina dependente
            f0 (int): Fase da disciplina candidata
            n (int): Número de pré-requisitos da disciplina dependente
        
        Retorna:
            float: Peso atribuído à disciplina candidata
        """
        if (f1 - f0) == 0 or n == 0:
            return 0  # Prevenção contra divisão por zero
        return 1 / ((f1 - f0) * (n / 2))

    # Calcula o peso de cada disciplina liberada
    for candidata in dis_liberadas:
        sinonimos = [candidata]  # Lista de disciplinas associadas
        peso_da_candidata = 0  # Peso inicial
        
        for c in disciplinas:
            # Verifica se a disciplina candidata é pré-requisito de alguma outra disciplina
            if candidata in disciplinas[c]["pre_requisitos"]:
                peso_da_candidata += f_teta(
                    disciplinas[c]["fase"], 
                    disciplinas[candidata]["fase"], 
                    len(disciplinas[c]["pre_requisitos"])
                )
                sinonimos.append(c)
        
        # Armazena o peso, disciplinas associadas e carga horária
        status[candidata] = {
            "peso": peso_da_candidata,
            "sinonimos": sinonimos,
            "creditos": disciplinas[candidata]["creditos"]
        }

    # Ordena as disciplinas por peso em ordem decrescente
    disciplinas_ordenadas = sorted(
        status.items(), 
        key=lambda x: x[1]["peso"], 
        reverse=True
    )

    # Definição dos limites da carga horária
    carga_min = 15
    #carga_max = 22
    carga_atual = 0  # Contador de créditos acumulados
    selecionadas = []  # Lista de disciplinas escolhidas
    pdf_path = os.path.join(os.path.dirname(__file__), "cadastro_de_turmas.pdf")
    horarios_aderidos = []
    

    print("\n--- INICIANDO SELEÇÃO DE DISCIPLINAS ---")

    # Adiciona a disciplina com maior peso diretamente
    if disciplinas_ordenadas:
        disciplina_mais_pesada, info = disciplinas_ordenadas[0]
        selecionadas.append(disciplina_mais_pesada)
        horarios_aderidos.append(extrair_horarios(pdf_path, disciplina_mais_pesada, info["creditos"]))
        carga_atual += info["creditos"]
        print(f"[SELECIONADA SEM CONFLITO] {disciplina_mais_pesada} | Créditos: {info['creditos']} | Carga atual: {carga_atual}")

    for disciplina, info in disciplinas_ordenadas[1:]:
        creditos_restantes = carga_max - carga_atual
        print(f"\n[AVALIANDO] {disciplina} | Créditos: {info['creditos']} | Peso: {info['peso']:.4f}")
        print(f"    -> Créditos restantes: {creditos_restantes}")
        
        if creditos_restantes < 4:
            print(f"    -> Parando: espaço restante ({creditos_restantes}) insuficiente.")
            break

        if carga_atual + info["creditos"] <= carga_max:
            print(f"    -> Verificando conflito para {disciplina}")
            if conflitos(disciplina, info["creditos"],horarios_aderidos):
                selecionadas.append(disciplina)
                horarios_aderidos.append(extrair_horarios(pdf_path, disciplina, info["creditos"]))
                carga_atual += info["creditos"]
                print(f"[ADICIONADA] {disciplina} | Nova carga: {carga_atual}")
            else:
                print(f"[CONFLITO] {disciplina} não adicionada por conflito de horário.")
        else:
            print(f"    -> Não adicionada: ultrapassa carga máxima ({carga_atual + info['creditos']} > {carga_max})")

    print("\n--- RESULTADO FINAL ---")
    print(f"Disciplinas selecionadas ({len(selecionadas)}): {selecionadas}")
    print(f"Carga horária final: {carga_atual}")

    if carga_atual < carga_min:
        print(f"[AVISO] Carga mínima não atingida ({carga_atual} < {carga_min})")

    return selecionadas
