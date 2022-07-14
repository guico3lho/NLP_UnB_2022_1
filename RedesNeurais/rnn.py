import math
import numpy as np

def main():


    learn_and_vini()
    # and_vini()





def learn_and_vini():
    data_and = [[0, 0], [0, 1], [1, 0], [1, 1]]
    labels = [0, 0, 0, 1]
    d = 2

    lr = 0.2
    pesos = np.random.randn(2)
    l = np.array(labels)
    X = np.array(data_and)
    t = 0

    while t < 15:

        loss = 0

        print(f'Epoch: {t}')

        for i, x in enumerate(X):

            net = 0
            for j in range(0, d):
                net += pesos[j] * x[j]

            y = funcAtivacao(net, 'degrau', 0.4)

            erro = (labels[i] - y) ** 2

            loss += erro

            if labels[i] != y:

                for j in range(0, d):
                    delta = lr * x[j] * (labels[i] - y)
                    pesos[j] += delta
        t += 1
        print(f'Loss function: {loss}')










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

    return y


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

def learn_and():
    pesos = np.random.randn(2)
    X = [[0,0], [0,1], [1,0], [1,1]]
    labels = [0,0,0,1]
    bias = 0
    d = 2
    net = bias

    t = 0
    E = 5
    e = 0.25
    learning_rate = 0.1
    loss = 0
# [ 0.41797655 -1.1972179  -0.81969236  0.6041066  -0.83425944]
    while t < 10:
        print(t)
        for entradas, label in zip(X,labels):
            # for a in atributo:
            for entrada,peso in zip(entradas,pesos):
                net += entrada*peso

            y = funcAtivacao(net,'degrau',0.5)

            # print(f'[{entradas[0]},{entradas[1]}] Output perceptron: {y} Label: {label}')


            if y != label:
                loss += (y-label)**2
                for i,peso in enumerate(pesos):
                    delta = learning_rate*peso*entradas[i]*(label - y)
                    pesos[i] = pesos[i] + delta
        print("loss:", loss)
        t += 1




                # if y != label:
                #     peso = 0.1*entrada*(label - y)
if __name__ == "__main__":
    main()