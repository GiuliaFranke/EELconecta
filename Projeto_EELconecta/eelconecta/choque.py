import fitz #type: ignore
import re
import os

def extrair_horarios(pdf_path, codigos_disciplinas, creditos_necessarios):

    pdf_path = "eelconecta/cadastro_de_turmas.pdf"
    


    if isinstance(codigos_disciplinas, str):
        codigos_disciplinas = [codigos_disciplinas]

    print(f"\n\n\n codigos = {codigos_disciplinas}\n")
    doc = fitz.open(pdf_path)
    texto = ""
    for pagina in doc:
        texto += pagina.get_text()

    linhas = texto.splitlines()
    resultado_matriz = []

    padrao_horario = re.compile(r"(\d\.\d{4})-(\d)")  # mais robusto
    codigos_set = set(codigos_disciplinas)

    for codigo in codigos_disciplinas:
        i = 0
        while i < len(linhas):
            linha = linhas[i]
            if codigo in linha:
                j = i + 7  # volta ao comportamento original
                creditos_acumulados = 0
                grupo_horarios = []

                while j < len(linhas):
                    l = linhas[j].strip()
                    match = padrao_horario.search(l)

                    if match:
                        horario_limpo = match.group(0)
                        grupo_horarios.append(horario_limpo)
                        creditos_acumulados += int(match.group(2))

                        if creditos_acumulados >= creditos_necessarios:
                            resultado_matriz.append(grupo_horarios)
                            break

                    elif any(outro_codigo in l for outro_codigo in codigos_set if outro_codigo != codigo):
                        break
                    elif not l or l.replace(" ", "").isalpha():
                        break

                    j += 1
                i = j
            else:
                i += 1

    resultado_matriz2 = agrupar_horarios(resultado_matriz)
    return resultado_matriz2


def agrupar_horarios(resultado_matriz):
    grupos_unicos = []
    conjuntos_vistos = set()

    for grupo in resultado_matriz:
        conjunto = frozenset(grupo)
        if conjunto not in conjuntos_vistos:
            grupos_unicos.append(grupo)
            conjuntos_vistos.add(conjunto)

    return grupos_unicos

#EXEMPLO DE USO
#pdf_path = "CADASTRO_TURMAS_20251 (1).pdf"
#creditos = 4
#codigo = ["EEL7041"]

#print(extrair_horarios(pdf_path, codigo, creditos))

