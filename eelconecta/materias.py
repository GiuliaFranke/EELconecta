import math

# dicionário completo de disciplinas
disciplinas_eletrica = {
    # Fase 1
    "EEL7011": {
        "nome": "Laboratório de Eletricidade Básica",
        "pre_requisitos": [],
        "creditos": 2,
        "fase": 1
    },
    "EEL7014": {
        "nome": "Introdução às Engenharias Elétrica e Eletrônica",
        "pre_requisitos": [],
        "creditos": 2,
        "fase": 1
    },
    "FSC5101": {
        "nome": "Física I",
        "pre_requisitos": [],
        "creditos": 4,
        "fase": 1
    },
    "LLV7801": {
        "nome": "Produção Textual Acadêmica",
        "pre_requisitos": [],
        "creditos": 4,
        "fase": 1
    },
    "MTM3100": {
        "nome": "Pré-Cálculo",
        "pre_requisitos": [],
        "creditos": 4,
        "fase": 1
    },
    "MTM3101": {
        "nome": "Cálculo 1",
        "pre_requisitos": ["MTM3100"],
        "creditos": 4,
        "fase": 1
    },
    "MTM3111": {
        "nome": "Geometria Analítica",
        "pre_requisitos": [],
        "creditos": 4,
        "fase": 1
    },
    "QMC5125": {
        "nome": "Química Geral Experimental A",
        "pre_requisitos": [],
        "creditos": 2,
        "fase": 1
    },
    "QMC5138": {
        "nome": "Química Geral",
        "pre_requisitos": [],
        "creditos": 2,
        "fase": 1
    },

    # Fase 2
    "EGR5619": {
        "nome": "Desenho Técnico para Engenharia Elétrica",
        "pre_requisitos": [],
        "creditos": 4,
        "fase": 2
    },
    "FSC5002": {
        "nome": "Física II",
        "pre_requisitos": ["FSC5101", "MTM3101"],
        "creditos": 4,
        "fase": 2
    },
    "FSC5122": {
        "nome": "Física Experimental I",
        "pre_requisitos": ["FSC5101"],
        "creditos": 3,
        "fase": 2
    },
    "INE5201": {
        "nome": "Introdução à Ciência da Computação",
        "pre_requisitos": [],
        "creditos": 3,
        "fase": 2
    },
    "MTM3102": {
        "nome": "Cálculo 2",
        "pre_requisitos": ["MTM3101"],
        "creditos": 4,
        "fase": 2
    },
    "MTM3112": {
        "nome": "Álgebra Linear",
        "pre_requisitos": ["MTM3111"],
        "creditos": 4,
        "fase": 2
    },

    # Fase 3
    "ECZ5102": {
        "nome": "Conservação de Recursos Naturais",
        "pre_requisitos": [],
        "creditos": 2,
        "fase": 3
    },
    "EEL5105": {
        "nome": "Circuitos e Técnicas Digitais",
        "pre_requisitos": ["EEL7011"],
        "creditos": 5,
        "fase": 3
    },
    "EEL7013": {
        "nome": "Laboratório de Transdutores",
        "pre_requisitos": ["EEL7011"],
        "creditos": 2,
        "fase": 3
    },
    "FSC5113": {
        "nome": "Física III",
        "pre_requisitos": ["FSC5002"],
        "creditos": 4,
        "fase": 3
    },
    "INE5118": {
        "nome": "Probabilidade Estatística e Processos Estocásticos",
        "pre_requisitos": ["MTM3102"],
        "creditos": 4,
        "fase": 3
    },
    "INE5202": {
        "nome": "Cálculo Numérico em Computadores",
        "pre_requisitos": ["INE5201", "MTM3102", "MTM3112"],
        "creditos": 4,
        "fase": 3
    },
    "MTM3103": {
        "nome": "Cálculo 3",
        "pre_requisitos": ["MTM3102", "MTM3111"],
        "creditos": 4,
        "fase": 3
    },

    # Fase 4
    "EEL7030": {
        "nome": "Microprocessadores",
        "pre_requisitos": ["EEL5105"],
        "creditos": 4,
        "fase": 4
    },
    "EEL7041": {
        "nome": "Eletromagnetismo",
        "pre_requisitos": ["FSC5113", "MTM3103"],
        "creditos": 4,
        "fase": 4
    },
    "EEL7045": {
        "nome": "Circuitos Elétricos A",
        "pre_requisitos": ["EEL7013", "FSC5113", "MTM3102"],
        "creditos": 6,
        "fase": 4
    },
    "EPS7019": {
        "nome": "Engenharia Econômica",
        "pre_requisitos": [],
        "creditos": 3,
        "fase": 4
    },
    "FSC5114": {
        "nome": "Física IV",
        "pre_requisitos": ["FSC5113"],
        "creditos": 4,
        "fase": 4
    },
    "MTM3104": {
        "nome": "Cálculo 4",
        "pre_requisitos": ["MTM3102"],
        "creditos": 4,
        "fase": 4
    },

    # Fase 5
    "EEL7051": {
        "nome": "Materiais Elétricos",
        "pre_requisitos": ["FSC5114", "QMC5125", "QMC5138"],
        "creditos": 4,
        "fase": 5
    },
    "EEL7052": {
        "nome": "Sistemas Lineares",
        "pre_requisitos": ["EEL7045", "MTM3104", "MTM3112"],
        "creditos": 5,
        "fase": 5
    },
    "EEL7053": {
        "nome": "Ondas Eletromagnéticas",
        "pre_requisitos": ["EEL7041", "EEL7045"],
        "creditos": 4,
        "fase": 5
    },
    "EEL7055": {
        "nome": "Circuitos Elétricos B",
        "pre_requisitos": ["EEL7045"],
        "creditos": 6,
        "fase": 5
    },
    "EEL7061": {
        "nome": "Eletrônica I",
        "pre_requisitos": ["EEL7045", "FSC5114"],
        "creditos": 6,
        "fase": 5
    },

    # Fase 6
    "DIR5998": {
        "nome": "Legislação e Ética em Engenharia Elétrica",
        "pre_requisitos": [],
        "creditos": 2,
        "fase": 6
    },
    "EEL7062": {
        "nome": "Princípios de Sistemas de Comunicação",
        "pre_requisitos": ["EEL7052", "INE5118"],
        "creditos": 5,
        "fase": 6
    },
    "EEL7063": {
        "nome": "Sistemas de Controle (Teoria e Laboratório)",
        "pre_requisitos": ["EEL7052"],
        "creditos": 6,
        "fase": 6
    },
    "EEL7064": {
        "nome": "Conversão Eletromecânica de Energia A",
        "pre_requisitos": ["EEL7041", "EEL7051", "EEL7055"],
        "creditos": 4,
        "fase": 6
    },
    "EEL7072": {
        "nome": "Projeto de Instalações Elétricas",
        "pre_requisitos": ["EEL7051", "EEL7055"],
        "creditos": 4,
        "fase": 6
    },
    "EEL7522": {
        "nome": "Processamento Digital de Sinais",
        "pre_requisitos": ["EEL7052"],
        "creditos": 4,
        "fase": 6
    },
    "EEL7071": {
        "nome": "Introdução a Sistemas de Energia Elétrica",
        "pre_requisitos": ["EEL7053", "EEL7064", "INE5202"],
        "creditos": 4,
        "fase": 6
    },
    "EEL7073": {
        "nome": "Conversão Eletromecânica de Energia B",
        "pre_requisitos": ["EEL7064"],
        "creditos": 4,
        "fase": 6
    },
    "EEL7074": {
        "nome": "Eletrônica de Potencia I ",
        "pre_requisitos":["EEL7061"],
        "creditos": 5,
        "fase": 6     },
        # Fase 7
    "EEL7071": {
        "nome": "Introdução a Sistemas de Energia Elétrica",
        "pre_requisitos": ["EEL7053", "EEL7064", "INE5202"],
        "creditos": 4,
        "fase": 7
    },
    "EEL7073": {
        "nome": "Conversão Eletromecânica de Energia B",
        "pre_requisitos": ["EEL7064"],
        "creditos": 4,
        "fase": 7
    },
    "EEL7074": {
        "nome": "Eletrônica de Potência I",
        "pre_requisitos": ["EEL7061"],
        "creditos": 5,
        "fase": 7
    },
    "EEL7300": {
        "nome": "Instrumentação Eletrônica",
        "pre_requisitos": ["EEL5105", "EEL7061"],
        "creditos": 5,
        "fase": 7
    },
    "EMC5425": {
        "nome": "Fenômenos de Transportes",
        "pre_requisitos": ["FSC5113", "FSC5122", "MTM3103"],
        "creditos": 4,
        "fase": 7
    },
    "INE5407": {
        "nome": "Ciência, Tecnologia e Sociedade",
        "pre_requisitos": [],
        "creditos": 3,
        "fase": 7
    },

    # Fase 8
    "EEL7080": {
        "nome": "Seminários de Engenharia Elétrica",
        "pre_requisitos": ["EEL7055", "LLV7801"],
        "creditos": 2,
        "fase": 8
    },
    "EEL7081": {
        "nome": "Aspectos de Segurança em Engenharia Elétrica",
        "pre_requisitos": ["EEL7072"],
        "creditos": 2,
        "fase": 8
    },
     # Fase 9
    "EEL7830": {
        "nome": "Estágio Curricular Curto I",
        "pre_requisitos": [],
        "creditos": 10,
        "fase": 9
    },
    "EEL7871": {
        "nome": "Estágio Curricular Curto II",
        "pre_requisitos": ["EEL7830"],
        "creditos": 10,
        "fase": 9
    },
    "EEL7889": {
        "nome": "Planejamento do Trabalho de Conclusão de Curso",
        "pre_requisitos": ["EEL7080"],
        "creditos": 2,
        "fase": 9
    },

    # Optativas (fase padronizada para 8)
    "EEL7083": {
        "nome": "Energia Elétrica e Sustentabilidade",
        "pre_requisitos": ["FSC5114", "FSC5002"],
        "creditos": 4,
        "fase": 8
    },
    "EEL7100": {
        "nome": "Operação de Sistemas de Energia Elétrica",
        "pre_requisitos": ["EEL7071"],
        "creditos": 4,
        "fase": 8
    },
    "EEL7101": {
        "nome": "Dinâmica e Controle de Sistemas Elétricos de Potência",
        "pre_requisitos": ["EEL7071"],
        "creditos": 4,
        "fase": 8
    },
    "EEL7102": {
        "nome": "Sistema de Distribuição de Energia Elétrica",
        "pre_requisitos": ["EEL7071"],
        "creditos": 4,
        "fase": 8
    },
    "EEL7103": {
        "nome": "Instalações Elétricas Industriais",
        "pre_requisitos": ["EEL7071", "EEL7072"],
        "creditos": 4,
        "fase": 8
    },
    "EEL7104": {
        "nome": "Planejamento e Regulação de Mercados de Energia Elétrica",
        "pre_requisitos": ["EEL7071"],
        "creditos": 4,
        "fase": 8
    },
    "EEL7105": {
        "nome": "Planejamento da Operação de Sistemas de Energia Elétrica",
        "pre_requisitos": ["EEL7100"],
        "creditos": 4,
        "fase": 8
    },
    "EEL7106": {
        "nome": "Proteção de Sistemas Elétricos",
        "pre_requisitos": ["EEL7071"],
        "creditos": 4,
        "fase": 8
    },
    "EEL7107": {
        "nome": "Transmissão de Energia Elétrica",
        "pre_requisitos": ["EEL7071"],
        "creditos": 4,
        "fase": 8
    },
    "EEL7200": {
        "nome": "Eletrônica de Potência II",
        "pre_requisitos": ["EEL7073", "EEL7074"],
        "creditos": 4,
        "fase": 8
    },
    "EEL7201": {
        "nome": "Aspectos Construtivos e Análise de Máquinas Elétricas",
        "pre_requisitos": ["EEL7073"],
        "creditos": 4,
        "fase": 8
    },
    "EEL7202": {
        "nome": "Acionamentos Elétricos e Eletrônicos",
        "pre_requisitos": ["EEL7074"],
        "creditos": 4,
        "fase": 8
    },
    "EEL7203": {
        "nome": "Projeto de Fontes Chaveadas",
        "pre_requisitos": ["EEL7074"],
        "creditos": 4,
        "fase": 8
    },
    "EEL7204": {
        "nome": "Processamento de Energia Fotovoltaica e Eólica",
        "pre_requisitos": ["EEL7063", "EEL7074"],
        "creditos": 4,
        "fase": 8
    },
    "EEL7205": {
        "nome": "Dispositivos de Armazenamento de Energia",
        "pre_requisitos": ["EEL7063", "EEL7074"],
        "creditos": 4,
        "fase": 8
    },
    "EEL7210": {
        "nome": "Modelagem Eletromagnética",
        "pre_requisitos": ["EEL7041"],
        "creditos": 4,
        "fase": 8
    },
    "EEL7211": {
        "nome": "Elementos Finitos em Engenharia Elétrica",
        "pre_requisitos": ["EEL7210"],
        "creditos": 4,
        "fase": 8
    },
    "EEL7212": {
        "nome": "Introdução à Compatibilidade Eletromagnética",
        "pre_requisitos": ["EEL7053", "EEL7061"],
        "creditos": 4,
        "fase": 8
    },
    "EEL7317": {
        "nome": "Projeto VLSI",
        "pre_requisitos": [],
        "creditos": 4,
        "fase": 8
    },
    "EEL7318": {
        "nome": "Projeto de Circuitos Integrados",
        "pre_requisitos": ["EEL7411"],
        "creditos": 4,
        "fase": 8
    },
    "EEL7319": {
        "nome": "Circuitos RF",
        "pre_requisitos": ["EEL7053", "EEL7061", "EEL7062"],
        "creditos": 4,
        "fase": 8
    },
    "EEL7320": {
        "nome": "Optoeletrônica",
        "pre_requisitos": ["EEL7051"],
        "creditos": 4,
        "fase": 8
    },
    # Adição de carga horária como pré-requisito
    "EEL7890": {
        "nome": "Trabalho de Conclusão de Curso (TCC)",
        "pre_requisitos": ["EEL7889", "carga_horaria_minima_ha: 432"],
        "creditos": 18,
        "fase": 10
    }
    
}

disciplinas_eletronica = {
    # Fase 1
    "EEL7011": {
        "nome": "Laboratório de Eletricidade Básica",
        "pre_requisitos": [],
        "creditos": 2,
        "fase": 1
    },
    "EEL7014": {
        "nome": "Introdução às Engenharias Elétrica e Eletrônica",
        "pre_requisitos": [],
        "creditos": 2,
        "fase": 1
    },
    "FSC5101": {
        "nome": "Física I",
        "pre_requisitos": [],
        "creditos": 4,
        "fase": 1
    },
    "LLV7801": {
        "nome": "Produção Textual Acadêmica",
        "pre_requisitos": [],
        "creditos": 4,
        "fase": 1
    },
    "MTM3100": {
        "nome": "Pré-Cálculo",
        "pre_requisitos": [],
        "creditos": 4,
        "fase": 1
    },
    "MTM3101": {
        "nome": "Cálculo 1",
        "pre_requisitos": ["MTM3100"],
        "creditos": 4,
        "fase": 1
    },
    "MTM3111": {
        "nome": "Geometria Analítica",
        "pre_requisitos": [],
        "creditos": 4,
        "fase": 1
    },
    "QMC5125": {
        "nome": "Química Geral Experimental A",
        "pre_requisitos": [],
        "creditos": 2,
        "fase": 1
    },
    "QMC5138": {
        "nome": "Química Geral",
        "pre_requisitos": [],
        "creditos": 2,
        "fase": 1
    },

    # Fase 2
    "EGR5619": {
        "nome": "Desenho Técnico para Engenharia Elétrica",
        "pre_requisitos": [],
        "creditos": 4,
        "fase": 2
    },
    "FSC5002": {
        "nome": "Física II",
        "pre_requisitos": ["FSC5101", "MTM3101"],
        "creditos": 4,
        "fase": 2
    },
    "FSC5122": {
        "nome": "Física Experimental I",
        "pre_requisitos": ["FSC5101"],
        "creditos": 3,
        "fase": 2
    },
    "INE5201": {
        "nome": "Introdução à Ciência da Computação",
        "pre_requisitos": [],
        "creditos": 3,
        "fase": 2
    },
    "MTM3102": {
        "nome": "Cálculo 2",
        "pre_requisitos": ["MTM3101"],
        "creditos": 4,
        "fase": 2
    },
    "MTM3112": {
        "nome": "Álgebra Linear",
        "pre_requisitos": ["MTM3111"],
        "creditos": 4,
        "fase": 2
    },

    # Fase 3
    "EEL5105": {
        "nome": "Circuitos e Técnicas Digitais",
        "pre_requisitos": ["INE5201"],
        "creditos": 5,
        "fase": 3
    },
    "EEL7013": {
        "nome": "Laboratório de Transdutores",
        "pre_requisitos": ["EEL7011"],
        "creditos": 2,
        "fase": 3
    },
    "FSC5113": {
        "nome": "Física III",
        "pre_requisitos": ["FSC5002"],
        "creditos": 4,
        "fase": 3
    },
    "INE5118": {
        "nome": "Probabilidade, Estatística e Processos Estocásticos",
        "pre_requisitos": ["MTM3101"],
        "creditos": 4,
        "fase": 3
    },
    "INE5202": {
        "nome": "Cálculo Numérico em Computadores",
        "pre_requisitos": ["INE5201", "MTM3102", "MTM3112"],
        "creditos": 4,
        "fase": 3
    },
    "MTM3103": {
        "nome": "Cálculo 3",
        "pre_requisitos": ["MTM3102", "MTM3111"],
        "creditos": 4,
        "fase": 3
    },

    # Fase 4
    "EEL7030": {
        "nome": "Microprocessadores",
        "pre_requisitos": ["EEL5105"],
        "creditos": 4,
        "fase": 4
    },
    "EEL7041": {
        "nome": "Eletromagnetismo",
        "pre_requisitos": ["FSC5113", "MTM3103"],
        "creditos": 4,
        "fase": 4
    },
    "EEL7045": {
        "nome": "Circuitos Elétricos A",
        "pre_requisitos": ["EEL7013", "FSC5113", "MTM3102"],
        "creditos": 6,
        "fase": 4
    },

    # Fase 5
    "EEL7051": {
        "nome": "Materiais Elétricos",
        "pre_requisitos": ["FSC5114", "QMC5125", "QMC5138"],
        "creditos": 4,
        "fase": 5
    },
    "EEL7052": {
        "nome": "Sistemas Lineares",
        "pre_requisitos": ["EEL7045", "MTM3104", "MTM3112"],
        "creditos": 5,
        "fase": 5
    },

    # Fase 6
   "EEL7062": {
        "nome": "Princípios de Sistemas de Comunicação",
        "pre_requisitos": ["EEL7052"],
        "creditos": 5,
        "fase": 6
    },
    "EEL7303": {
        "nome": "Circuitos Eletrônicos Analógicos",
        "pre_requisitos": ["EEL7052", "EEL7061"],
        "creditos": 5,
        "fase": 6
    },
    "EEL7522": {
        "nome": "Processamento Digital de Sinais",
        "pre_requisitos": ["EEL7052"],
        "creditos": 4,
        "fase": 6
    },
    "FSC5506": {
        "nome": "Estrutura da Matéria I",
        "pre_requisitos": ["FSC5114", "MTM3103"],
        "creditos": 6,
        "fase": 6
    },
    "INE5411": {
        "nome": "Organização de Computadores I",
        "pre_requisitos": ["EEL7030", "INE5406"],
        "creditos": 6,
        "fase": 6
    },

    # Fase 7
   "EEL7319": {
        "nome": "Circuitos RF",
        "pre_requisitos": ["EEL7053", "EEL7061", "EEL7062"],
        "creditos": 4,
        "fase": 7
    },
    "EEL7322": {
        "nome": "Dispositivos Eletrônicos",
        "pre_requisitos": ["EEL7061", "FSC5506"],
        "creditos": 4,
        "fase": 7
    },
    "EEL7417": {
        "nome": "Fundamentos de Comunicação Digital",
        "pre_requisitos": ["EEL7062"],
        "creditos": 4,
        "fase": 7
    },
    "EEL7802": {
        "nome": "Projeto em Eletrônica II",
        "pre_requisitos": ["EEL7801"],
        "creditos": 3,
        "fase": 7
    },
    "EEL7885": {
        "nome": "Fundamentos de Engenharia Biomédica",
        "pre_requisitos": ["EEL7061"],
        "creditos": 4,
        "fase": 7
    },

    # Fase 8
    "EEL7610": {
        "nome": "Tópico Especial em Gestão",
        "pre_requisitos": [],
        "creditos": 3,
        "fase": 8
    },

    # Fase 9
    "EEL7805": {
        "nome": "Ante-Projeto TCC",
        "pre_requisitos": [],
        "creditos": 4,
        "fase": 9
    },

    # Fase 10
    "EEL7806": {
        "nome": "Projeto Final TCC",
        "pre_requisitos": ["EEL7805"],
        "creditos": 16,
        "fase": 10
    }
}


escolha_de_curso = 1 #Variavel que tem seu valor definido quando o estudante escolhe o curso la no HTML ENTRE 1 E DOIS VER A PROXIMA LINHA)

if escolha_de_curso == 1:
    disciplinas = disciplinas_eletrica
elif escolha_de_curso == 2:
    disciplinas = disciplinas_eletronica


#Essa função calcula quais disciplinas o estudante pode cursar no estado atual (As que serão pintadas de verde)
def disponiveis(subjects_completed):
    # Disciplinas liberadas
    subjects_released = list()

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
    


#Essa função cria a melhor tragetória de disciplinas (As que serão pintadas de vermelho)
def recomendacao(subjects_released):
    #passo a passo
    # 1 -> Asumir uma dsciplina candidata
    # 2 -> Verificar todas as disiplinas do discionario com a condição de ter como prérequisito a disciplina candidata
    # 3 -> Adiciona essa diciplina como um sinônimo da candidata 
    # 4 -> Verifica a fase e se possui mais diciplinas para ser liberada
    # 5 -> Aplica a f_teta e adiciona esse valor a  disiplina 
    # 6 -> Somatório de todos os pesos 
    # 7 -> Assume outra disiciplina (return ->1)
    # ** NOTE delta f jamais sera negativo pois se uma disiplina exige a disciplina candidata como pré requisito ela jamais estara tera uma fase menor que F0 

       
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
    carga_min = 18
    carga_max = 24
    carga_atual = 0  # Contador de créditos acumulados
    selecionadas = []  # Lista de disciplinas escolhidas

    # Seleciona disciplinas até atingir pelo menos 15 créditos
    for disciplina, info in disciplinas_ordenadas:
        if carga_atual + info["creditos"] <= carga_max:
            selecionadas.append(disciplina)
            carga_atual += info["creditos"]
        if carga_atual >= carga_min:
            break  # Para a seleção se atingir o mínimo necessário

    # Se a carga mínima não for atingida, adiciona disciplinas de peso 0
    if carga_atual < carga_min:
        disciplinas_peso_zero = [d for d in dis_liberadas if status[d]["peso"] == 0]
        for d in disciplinas_peso_zero:
            if carga_atual + disciplinas[d]["creditos"] <= carga_max:
                selecionadas.append(d)
                carga_atual += disciplinas[d]["creditos"]
            if carga_atual >= carga_min:
                break  # Para ao atingir o mínimo necessário

    # Exibe as disciplinas recomendadas
    print("Disciplinas recomendadas:")
    for d in selecionadas:
        print(f"{d} - {disciplinas[d]['nome']} ({disciplinas[d]['creditos']} créditos)")

    return selecionadas  # Retorna a lista de disciplinas escolhidas

#As que ja foram concluidas
estado_atual = []

#As que podem ser cursada
liberadas_para_cursar = disponiveis(estado_atual)

#As mais indicadas para se cursar no momento
recomendacao(liberadas_para_cursar)