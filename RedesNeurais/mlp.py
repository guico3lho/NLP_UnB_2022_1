import math

import numpy as np

def main():

    lr = 0.05
    data_xor = [[0,0],[0,1],[1,0],[1,1]]
    labels = [0,1,1,0]

    layer1_pesos = np.random.randn(4) # w11,w12,w13,w14
    layer2_pesos = np.random.randn(2) # w21,w22
    epochs = 0
    while epochs < 10:
        print("Epoca:", epochs)
        for i,x in enumerate(data_xor):
            net1 = data_xor[i][0]*layer1_pesos[0] + data_xor[i][1]*layer1_pesos[2] # x1*w11 + x2*w13
            net2 = data_xor[i][0]*layer1_pesos[1] + data_xor[i][1]*layer1_pesos[3] # x1*w12 + x2*w14

            O1 = funcAtivacao(net1,'sinoidal',0.5)
            O2 = funcAtivacao(net2,'sinoidal', 0.5)

            net3 = O1*layer2_pesos[0]+O2*layer2_pesos[1] # O1*W21 + O2*W22


            y = funcAtivacao(net3, 'sinoidal')

            loss = (y-labels[i])**2
            print("Loss:", loss)
            # para cada neuronio na camada de saida
            del3 = y*(1-y)*(y-labels[i])

            # para cada neuronio na camada oculta
            del1 = O1*(1-O1)*del3*layer2_pesos[0]
            del2 = O2*(1-O2)*del3*layer2_pesos[1]

            # atualizando pesos da rede camada 2
            delta = lr*del3*y
            layer2_pesos[0] += delta
            layer2_pesos[1] += delta

            # atualizando pesos da rede camada 1
            delta = lr*del1*O1
            layer1_pesos[0] += delta
            layer1_pesos[3] += delta

            delta = lr*del2*O2
            layer1_pesos[1] += delta
            layer1_pesos[3] += delta



            epochs += 1
            print("\n")

    #
    # ann = {}
    # ann['layer 0'] = {}
    # ann['layer 1'] = {}


def funcAtivacao(net, tipo,threshold=1):
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

if __name__ == "__main__":

    main()