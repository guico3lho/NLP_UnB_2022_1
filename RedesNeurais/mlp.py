import math

import numpy as np

def main():
    data_xor = [[0,0],[0,1],[1,0],[1,1]]
    labels = [0,1,1,0]

    layer1_pesos = np.random.randn(4) # w11,w12,w13,w14
    layer2_pesos = np.random.randn(2) # w21,w22

    for i,x in enumerate(data_xor):
        net1 = data_xor[i][0]*layer1_pesos[0] + data_xor[i][1]*layer1_pesos[2]
        net2 = data_xor[i][0]*layer1_pesos[1] + data_xor[i][1]*layer1_pesos[3]

        O1 = funcAtivacao(net1,'sinoidal',0.5)
        O2 = funcAtivacao(net2,'sinoidal', 0.5)

        net3 = O1*layer2_pesos[0]+O2*layer2_pesos[1]


        y = funcAtivacao(net3, 'sinoidal',0.5)
        print("\n")

    #
    # ann = {}
    # ann['layer 0'] = {}
    # ann['layer 1'] = {}


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

if __name__ == "__main__":

    main()