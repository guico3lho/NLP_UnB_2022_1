
raw_corpus = []
raw_corpus.append('Batatinha quando nasce esparrama pelo chão pelo chão')
raw_corpus.append('A pior experiência da minha vida')
raw_corpus.append('Quero me dinheiro de volta')
raw_corpus.append('A experiência do dinheiro esparrama minha vida')
raw_corpus.append('Acai é a melhor coisa da vida')

bigram = {}

for idx, doc in enumerate(raw_corpus):
    bigram[f'sentenca {idx + 1}'] = dict()
    tokens = doc.split()
    old_word = ''


    for word in tokens:
        new_word = word
        str_words = old_word + ' ' + new_word
        if word in bigram[f'sentenca {idx + 1}'] and old_word != '':
            print(word)
            bigram[f'sentenca {idx + 1}'][old_word + ' ' + new_word] += 1
        elif old_word != '':
            bigram[f'sentenca {idx + 1}'][old_word + ' ' + new_word] = 1
        old_word = word

        # for i in range(0,len(tokens)-1):
        #   par = (tokens[i],tokens[i])
# unigram = {}
#
# for i, doc in enumerate(corpus):
#     unigram['sentenca {}'.format(i+1)] = {}
#     tokens = doc.split()
#     for word in tokens:
#         if word in unigram['sentenca {}'.format(i+1)]:
#             unigram['sentenca {}'.format(i+1)][word] += 1
#         else:
#             unigram['sentenca {}'.format(i+1)][word] = 1
# print("\n")
bigram = {}

for i,doc in enumerate(raw_corpus):
    bigram['sentenca {}'.format(i+1)] = dict()
    tokens = doc.split()
    for j in range(0,len(tokens) -1):
        par = (tokens[j], tokens[j+1])
        if par in bigram['sentenca {}'.format(i+1)]:
            bigram['sentenca {}'.format(i+1)][par] +=1
        else:
            bigram['sentenca {}'.format(i+1)][par] = 1

print(bigram)

# text = 'A pior experiência da vida'
# P('A pior experiência da vida') = P('A') * P('pior'|'A') * P('experiência'|'pior') * P('da'|'experiência') * P('vida'|'da')

# text = " ".join(raw_corpus)
# tokens = text.split()
# vocab = sorted(set(tokens)) # palavras únicas
# all_vocab = sorted(tokens)
#
# for word in vocab:
#   p = all_vocab.count(word)/len(text.split())
#   print(all_vocab.count(word))



histograma_bigram = {}
histograma_unigram = {}
for doc in bigram:
    for par in bigram[doc]:
        if par in histograma_bigram:
            histograma_bigram[par] += bigram[doc][par]
        else:
            histograma_bigram[par] = bigram[doc][par]

def prob(sentence):
    tokens = sentence.split()
    p = 1
    for i in range(0,len(tokens)-1):
        p = p*hisograma_bigram[tokens[i+1]tokens[i]]
# unigram = {}
# bigram = ""
# for i, doc in enumerate(corpus):
#     unigram['sentenca {}'.format(i+1)] = {}
#     tokens = doc.split()
#
#     j= 1
#     for i in range(0,len(tokens)):






#
#     for word in tokens:
#         if j == 3:
#             break
#         bigram += " " + word
#         j += 1
#
#     if bigram in unigram['sentenca {}'.format(i+1)]:
#             unigram['sentenca {}'.format(i+1)][bigram] += 1
#     else:
#             unigram['sentenca {}'.format(i+1)][bigram] = 1
#     bigram = ""
# print("\n")


