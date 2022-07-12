corpus = []
corpus.append('batatinha quando nasce esparrama pelo chão igual batatinha')
corpus.append('A pior experiência da minha vida')
corpus.append('Quero meu dinheiro de volta pois é meu e é meu')
corpus.append('A experiência do dinheiro esparrama minha vida')
corpus.append('Acai é a melhor coisa da vida')


unigram = {}
n=0
for i,doc in enumerate(corpus):
    unigram['sentenca {}'.format(i+1)] = dict()
    tokens = doc.split()
    for word in tokens:
        if word in unigram['sentenca {}'.format(i+1)]:
            unigram['sentenca {}'.format(i+1)][word] += 1
        else:
            unigram['sentenca {}'.format(i+1)][word] = 1
        n+=1

print(unigram)


bigram = {}

for i,doc in enumerate(corpus):
    bigram['sentenca {}'.format(i+1)] = dict()
    tokens = doc.split()
    for j in range(0,len(tokens)-1):
        par = (tokens[j],tokens[j+1])
        if par in bigram['sentenca {}'.format(i+1)]:
            bigram['sentenca {}'.format(i+1)][par] += 1
        else:
            bigram['sentenca {}'.format(i+1)][par] = 1

bigram

histograma_unigram = {}
histograma_bigram = {}

for doc in bigram:
    for par in bigram[doc]:
        if par in histograma_bigram:
            histograma_bigram[par] += bigram[doc][par]
        else:
            histograma_bigram[par] = bigram[doc][par]

for doc in unigram:
    for par in unigram[doc]:
        if par in histograma_unigram:
            histograma_unigram[par] += unigram[doc][par]
        else:
            histograma_unigram[par] = unigram[doc][par]


def prob(sentence):
    tokens = sentence.split()

    p = histograma_unigram[tokens[0]] / n

    for i in range(0, len(tokens) - 1):
        p = p * (histograma_bigram[(tokens[i], tokens[i + 1])] / histograma_unigram[tokens[i + 1]])

    return p

prob("Batatinha")