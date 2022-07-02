import nltk
import pandas as pd
import math
# nltk.download('reuters')
from nltk.corpus import reuters



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
    corpus = df['text'].tolist()[:100]


    vocab = generateVocab(corpus)
    df_bow_binario = generateBowBinario(corpus)
    df_bow_contagem, bow_contagem = generateBowContagem(corpus)
    df_bow_ponderado, bow_ponderado = generateBowPonderado(corpus)
    df_bow_tfidf, bow_tfidf = generateTfidf(vocab,corpus,bow_contagem, bow_ponderado)
    print("\n")





if __name__ == "__main__":
    main()
