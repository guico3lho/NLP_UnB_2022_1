import nltk
import pandas as pd
import math
# nltk.download('reuters')
from nltk.corpus import reuters
import numpy as np
import cProfile




def generateVocab(corpus):
    tokens = []
    # corpus = df['text']
    # sentence = noticia
    for noticia in corpus:
        # noticia = ASIAN EXPORTERS FEAR DAMAGE FROM
        for word in noticia.split():
            tokens.append(word)
    # A then a

    vocab = sorted(set(tokens))
    return vocab
def generateBowBinario(corpus):
    # (i, noticia) = (0, ASIAN EXPORTERS FEAR DAMAGE FROM U.S.-JAPAN RIFT\n Mounting trade friction between the\n U.S. And Japa)
    bow_binario = {}
    for i,noticia in enumerate(corpus):
        bow_binario['noticia {}'.format(i)] = {}
        for word in noticia.split():
            bow_binario['noticia {}'.format(i)][word] = 1
    print("\n")

    df_bow_binario = pd.DataFrame().from_records(bow_binario).fillna(0).T.astype(int)
def generateBowContagem(corpus):
    bow_contagem = {}
    for i,noticia in enumerate(corpus):
        bow_contagem['noticia {}'.format(i)] = {}
        for word in noticia.split():
            if word in bow_contagem['noticia {}'.format(i)]:
                bow_contagem['noticia {}'.format(i)][word] += 1
            else:
                bow_contagem['noticia {}'.format(i)][word] = 1

    df_bow_contagem = pd.DataFrame().from_records(bow_contagem).fillna(0).T.astype(int)
    return df_bow_contagem, bow_contagem
def generateBowPonderado(corpus):
    bow_ponderado = {}
    N = {}
    # para cada noticia do corpus, fazer:
    for i,noticia in enumerate(corpus):
        # inicia dicionario para cada notícia
        bow_ponderado['noticia {}'.format(i)] = {}
        # N vai armazenar a quantidade de tokens de cada notícia
        N['noticia {}'.format(i)] = len(noticia.split())
        # para cada palavra de uma noticia
        for word in noticia.split():
            # se a palavra já está no dicionário da noticia, aumenta 1
            if word in bow_ponderado['noticia {}'.format(i)]:
                bow_ponderado['noticia {}'.format(i)][word] += 1
            else:
                bow_ponderado['noticia {}'.format(i)][word] = 1

    # para cada dicionário noticia do dicionario bow_contagem
    # for noticia in bow_contagem:
    #     # para cada palavra do dicionário noticia
    #     for word in noticia:
    # for noticia in bow_ponderado:
    for noticia in bow_ponderado:
        for word in bow_ponderado[noticia]:
            bow_ponderado[noticia][word] /= N[noticia]
    # bow_ponderado['noticia {}'.format(i)][word] = bow_ponderado['noticia {}'.format(i)][word]/N[i]

    df_bow_ponderado = pd.DataFrame().from_records(bow_ponderado).fillna(0).T.astype(float)

    return df_bow_ponderado, bow_ponderado
    print("\n")
def generateTfidf(vocab,corpus, bow_contagem, bow_ponderado):
    tf = {}
    idf = {}
    for word in vocab:
        tf[word] = 0
        for noticia in bow_contagem:
            if word in bow_contagem[noticia]:
                tf[word] += 1
    for word in tf:
        num = len(corpus)
        den = tf[word]
        idf[word] = math.log(num/den)

    bow_tfidf = {}
    for noticia in bow_ponderado:
        bow_tfidf[noticia] = {}
        for word in bow_ponderado[noticia]:
            a = bow_ponderado[noticia][word]
            b = idf[word]
            bow_tfidf[noticia][word] = a*b
    df_bow_tfidf = pd.DataFrame().from_records(bow_tfidf).fillna(0).T
    return df_bow_tfidf, bow_tfidf
def cossineSimilarity(vetor1, vetor2):
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

    return prod_interno / (norma_vetor1 * norma_vetor2)
def generateDfSim(df_bow_tfidf):

    df_similaridades = pd.DataFrame([])
    df_bow_tfidf.reset_index(inplace=True, drop=True)
    for i in range(0, len(df_bow_tfidf)):
        print(f"Similaridade da noticia {i}")
        similaridades = []

        # preenchendo a linha 0 de similaridade
        vetor1 = df_bow_tfidf.iloc[i].values.flatten().tolist()
        for j in range(0, len(df_bow_tfidf)):
            vetor2 = df_bow_tfidf.iloc[j].values.flatten().tolist()
            cos_sim = cossineSimilarity(vetor1, vetor2)
            similaridades.append(cos_sim)

        # a_row = pd.Series([1, 2])
        # df = pd.DataFrame([[3, 4], [5, 6]]) # vai adicionar dps
        #
        # row_df = pd.DataFrame([a_row])
        # df = pd.concat([row_df, df], ignore_index=True)

        df_similaridade = pd.DataFrame([similaridades])
        df_similaridades = pd.concat([df_similaridades, df_similaridade], ignore_index=True)

    np.fill_diagonal(df_similaridades.values, 0)
    return df_similaridades
    pass
def generateDfTop10(df_similaridades, df_reduced):

    indices_noticias_mais_similares_top10 = df_similaridades.apply(lambda s: s.abs().nlargest(10).index.tolist(), axis=1)
    df_top_10 = pd.DataFrame(0,index=np.arange(1), columns=np.arange(10))
    # for indice_noticia_consulta in range(0, len(df_reduced)):
    # para cada noticia de consulta

    for indice_noticia_consulta, lista in enumerate(indices_noticias_mais_similares_top10):
    # para cada lista contendo as top 10 noticias mais similares
        # ['trade']
        noticia_consulta_categorias = df_reduced.iloc[indice_noticia_consulta]['categories']
        # [['ipi','earn'], ['bop'], ['tin']]
        lista_tuplas_noticia_categoria = []
        for indice_noticia_similar in lista:
        #
            tupla_noticia_categoria = (indice_noticia_similar, df_reduced.iloc[indice_noticia_similar]['categories'])
            lista_tuplas_noticia_categoria.append(tupla_noticia_categoria)
        ranking = 0
        for tupla in lista_tuplas_noticia_categoria:
            for categoria in noticia_consulta_categorias:
                if categoria in tupla[1]:
                    df_top_10[ranking] += 1
                    break
            ranking += 1

    return df_top_10

def main():
    cats = reuters.categories()
    # print("Reuters has %d categories:\n%s" % (len(cats), cats))

    fileids = reuters.fileids()

    categories = []
    text = []

    for file in fileids:
        categories.append(reuters.categories(file))
        text.append(reuters.raw(file))

    df = pd.DataFrame({'ids': fileids, 'categories': categories, 'text': text})

    df_reduced = df.head(500)
    corpus = df_reduced['text']


    # df_bow_binario = generateBowBinario(corpus)
    vocab = generateVocab(corpus)
    df_bow_contagem, bow_contagem = generateBowContagem(corpus)
    df_bow_ponderado, bow_ponderado = generateBowPonderado(corpus)
    df_bow_tfidf, bow_tfidf = generateTfidf(vocab,corpus,bow_contagem, bow_ponderado)
    df_similaridades = generateDfSim(df_bow_tfidf)

    df_top_10 = generateDfTop10(df_similaridades, df_reduced)
    print("\n")





if __name__ == "__main__":
    cProfile.run('main()')
    # main()
