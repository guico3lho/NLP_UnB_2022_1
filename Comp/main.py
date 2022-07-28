import pandas as pd

import ast

import regex as re

def main():
    with open(r'C:\Users\guimi\Documents\Programming\Python\NLP_UnB_2022_1\Assets\classes.txt') as f:
        lines = f.readlines()
    #
    print("2asd")

    classes_dict = {}



    for line in lines:
        word = re.findall(r'([^.]+)',line)[0]
        PoS = re.search(r'(PoS=)(\w+)',line).group(2)
        classes_dict[word] = PoS


    df = pd.read_csv(
            'https://raw.githubusercontent.com/viniciusrpb/cic0269_natural_language_processing/main/datasets/corpora/training.csv')

    print("\n")

    corpus_dict = {}
    for row in df.iterrows():
            corpus_dict['texto {}'.format(row[0])] = {}
            text = row[1]['text']
            text = normalizarString(text)
            text_words = text.split() # ['oi', 'tchau']
            for i,word in enumerate(text_words):
                if word in classes_dict:
                    corpus_dict['texto {}'.format(row[0])][word] = classes_dict[word]


def normalizarString(text):
	import unicodedata
	try:
		text = unicode(text, 'utf-8')
	except NameError:
		pass
	text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode("utf-8")
	return str(text.lower())


# df = pd.read_csv('https://raw.githubusercontent.com/viniciusrpb/cic0269_natural_language_processing/main/datasets/corpora/training.csv')
# print(df)

if __name__ == "__main__":
    main()
