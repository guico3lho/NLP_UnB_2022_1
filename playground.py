import math
import pandas as pd
import regex as re

def cosine_similarity(vetor1, vetor2):
    prod_interno = 0

    for elemento1, elemento2 in zip(vetor1,vetor2):
        prod_interno += elemento1*elemento2

    norma_vetor1 = 0
    for x in vetor1:
        norma_vetor1 += x * x
    norma_vetor1 = norma_vetor1 ** 0.5

    # norma_vetor1 = math.sqrt(sum([x**2 for x in vetor1]))

    norma_vetor2 = 0
    for x in vetor2:
        norma_vetor2 += x * x
    norma_vetor2 = norma_vetor2 ** 0.5
    try:
        result = prod_interno/(norma_vetor1 * norma_vetor2)
    except(ZeroDivisionError):
        result = 0

    return result

def stackoverflow():
    d = {
        "a": [1, 0, 1, 0, 1],
        "b": [1,0,1,1,1],
        "n": [1,0,1,0,1]
    }

    df = pd.DataFrame(d)

    # # df_note = df.loc[df.n == "d", ['a','b']].values.flatten().tolist()
    # df_note = df.iloc[0].values.flatten().tolist()
    print(df.shape)
    for i in range(0,len(df)):
        vetor1 = df.iloc[i].values.flatten().tolist()
        for j in range(i+1,len(df)):
            vetor2 = df.iloc[j].values.flatten().tolist()
            cos_sim = cosine_similarity(vetor1,vetor2)
    pass
def main():
    texto = ''
    municipio_estado = re.findall('[A-Z][^A-Z ]+[/][A-Z]{2}', texto)
    municipio = municipio_estado[0].split('/')[0] if len(municipio_estado) > 0 else ''
    splits = re.split(r'([Oo]bjeto:?|OBJETO:?|\.|objetivo|[Cc]ontratação|CONTRATAÇÃO)', texto)
    objeto = ""
    # [Ee]xecu[cç][aã]o)
    #
    percorrendoObjeto = False
    for split in splits:
        if percorrendoObjeto == True:
            objeto += split

        if re.match(r'([Oo]bjeto:?|OBJETO:?|objetivo|[Cc]ontratação|CONTRATAÇÃO)', split):
            percorrendoObjeto = True
        if split == '.' and percorrendoObjeto == True:
            break

    if objeto == "":
        objeto = texto
    if 'Objeto:' in objeto:
        objeto = re.sub(r'Objeto:', '', objeto)

    if municipio != '' and municipio.lower() not in objeto.lower():
        objeto += municipio_estado[0]
    return objeto





if __name__ == '__main__':
    main()