import math
import pandas as pd

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
    # cos_sim = cosine_similarity([1,1,1,1],[1,1,1,1])
    stackoverflow()
    print("end\n")



if __name__ == '__main__':
    main()