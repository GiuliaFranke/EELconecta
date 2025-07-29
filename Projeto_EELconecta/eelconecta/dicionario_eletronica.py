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
