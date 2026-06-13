import math
from eelconecta import dicionario_eletrica, dicionario_eletronica
from eelconecta.dicionario_eletrica import disciplinas_eletrica
from eelconecta.dicionario_eletronica import disciplinas_eletronica

#Essa função calcula quais disciplinas o estudante pode cursar no estado atual (As que serão pintadas de verde)
def disponiveis(subjects_completed, course):
    # Disciplinas liberadas
    subjects_released = list()

    if course == 'eletrica':
        disciplinas = disciplinas_eletrica
    else:
        disciplinas = disciplinas_eletronica
    # Lista para armazenar disciplinas que têm "check" como pré-requisito e os pré-requisitos restantes
    contained = []

    # Verifica disciplinas dependentes de subjects_completed
    for check in subjects_completed:
        for c in disciplinas:
            # Verifica se "check" é um pré-requisito da disciplina "c"
            if check in disciplinas[c]["pre_requisitos"]:
                # Verifica se a disciplina "c" já está em "contained"
                encontrado = False
                for item in contained:
                    if item[0] == c:
                        encontrado = True
                        # Remove o pré-requisito "check" da lista de pré-requisitos pendentes
                        item[1] = [pre for pre in item[1] if pre != check]
                        break
                # Se "c" ainda não está em "contained", adiciona com os pré-requisitos restantes
                if not encontrado:
                    nao_cumpridos = [pre for pre in disciplinas[c]["pre_requisitos"] if pre != check]
                    contained.append([c, nao_cumpridos])


    for c in disciplinas:
        pre_requisitos = disciplinas[c]["pre_requisitos"]
    
        if c in subjects_completed:
            print(f"'{c}' já foi concluída e não deve ser adicionada.")
        elif (not pre_requisitos or all(pre in subjects_completed for pre in pre_requisitos)) and c not in subjects_released and c not in subjects_completed:
            print(f"Liberando disciplina: {c}, pois todos os pré-requisitos foram cumpridos ou não existem.")
            subjects_released.append(c)
    
    return(subjects_released)
    
