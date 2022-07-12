import math
import numpy as np

def main():
    atributos = [0.5,1.1,0.1,0.2,0.7]

    # qtd pesos = qtd atributos
    pesos = np.random.randn(5)
    # pesos = [-1,-1,-1,-4,-2]
    bias = 0
    net = bias
    for atributo, peso in zip(atributos,pesos):
        net += atributo*peso

    y = funcAtivacao(net, 'sinoidal',0)
    print(y)

    # learn_and()
    and_vini()


def learn_and():
    pesos = np.random.randn(5)
    X = [[0,0], [0,1], [1,0], [1,1]]
    labels = [0,0,0,1]
    bias = 0
    net = bias

# [ 0.41797655 -1.1972179  -0.81969236  0.6041066  -0.83425944]

    for entradas, peso,label in zip(X,pesos,labels):
        # for a in atributo:
        for entrada in entradas:
            net += entrada*peso

        y = funcAtivacao(net,'degrau',0.5)

        print(f'[{entradas[0]},{entradas[1]}] Output perceptron: {y} Label: {label}')


def and_vini():
    X = [[0, 0], [0, 1], [1, 0], [1, 1]]

    labels = [0, 1, 1, 1]

    weights = np.random.random(2) / 1000

    bias = np.random.random() / 1000

    for id, exemplo in enumerate(X):
        input = np.array(exemplo)

        net = np.dot(input, weights) + bias

        y = funcAtivacao(net, "degrau", 0.5)

        print("predicted: {}".format(y))
        print("label: {}".format(labels[id]))


def funcAtivacao(net, tipo,threshold):
    if tipo == 'degrau':
        if net >= threshold:
            y = 1
        else:
            y = 0
    elif tipo == 'sinal':
        if net >= 0:
            y = 1
        else:
            y = -1
    elif tipo == 'sinoidal':
        y = 1/(1+math.exp(-net))
    else:
        y = 'Tipo inválido'
    print("\n")
    return y

if __name__ == "__main__":
    main()