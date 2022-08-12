import pandas

all_data = pandas.read_csv(r'C:\Users\guimi\Documents\Programming\Python\NLP_UnB_2022_1\Anotacao\annotation.csv')

dataclasses = all_data.sample(n=100, random_state=42)



print()