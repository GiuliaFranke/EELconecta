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
         "nome": "Pre calc",
        "pre_requisitos": [],
        "creditos": 4,
        "fase": 1
    },
    "MTM3101": {
        "nome": "Cálculo 1",
        "pre_requisitos": [],
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
        "creditos": 6,
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
        "creditos": 6,
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
        "creditos": 6,
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
