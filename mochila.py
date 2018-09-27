def mochila(capacidade, valxpeso, tamanho):
    K = [[0 for x in range(capacidade+1)] for x in range(tamanho+1)]

    for i in range(tamanho + 1):
        for w in range(capacidade + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif valxpeso[i - 1][1] <= w:
                K[i][w] = max(valxpeso[i - 1][0] + K[i - 1][w - valxpeso[i - 1][1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]


    capsobrando = capacidade
    escolhidos =[]


    for i in range(tamanho, 0, -1):
        if K[i][capsobrando] != K[i-1][capsobrando]:
            escolhidos.append(valxpeso[i-1])
            capsobrando = capsobrando - valxpeso[i-1][1]



    return escolhidos, K[tamanho][capacidade]

valxpeso = [[60,10], [100,20], [120,30]]
W = 50
n = len(valxpeso)


print(mochila(W, valxpeso, n))

