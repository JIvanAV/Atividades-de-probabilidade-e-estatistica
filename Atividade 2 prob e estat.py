'''
Questão 2:

2- Pediu-se a 36 pessoas para classificarem o Sistema de Saúde em Portugal de acordo com
a seguinte escala: 1 (péssimo), 2 (mau), 3 (pouco razoável), 4 (razoável), 5 (muito
razoável), 6 (bom), 7 (muito bom), 8 (excelente). As classificações foram:

5   2   7   6   3   7   8   3   2   6   3   6   3   7   5   3   6   7
3   7   6   4   3   5   8   6   5   4   3   6   6   5   7   8   4   3

a) Proceda à organização dos dados, construindo uma tabela de frequências (absolutas,
relativas, absolutas acumuladas e relativas acumuladas).

b) Calcule a média, mediana, moda e o desvio padrão desta amostra.

'''

import statistics

print ("\n QUESTÃO 1) \n")

dados = [5, 2, 7, 6, 3, 7, 8, 3, 2, 6, 3, 6, 3, 7, 5, 3, 6, 7, 3, 7, 6, 4, 3, 5, 8, 6, 5, 4, 3, 6, 6, 5, 7, 8, 4, 3]

tabela_frequencias = {}
total = len(dados)

for valor in set(dados):
    frequencia_absoluta = dados.count(valor)
    frequencia_relativa = frequencia_absoluta / total
    frequencia_absoluta_acumulada = sum(1 for x in dados if x <= valor)
    frequencia_relativa_acumulada = frequencia_absoluta_acumulada / total

    tabela_frequencias[valor] = {
        'Frequência Absoluta': frequencia_absoluta,
        'Frequência Relativa': frequencia_relativa,
        'Frequência Absoluta Acumulada': frequencia_absoluta_acumulada,
        'Frequência Relativa Acumulada': frequencia_relativa_acumulada
    }

print("Letra a):\n") #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

print("Tabela de Frequências:")
print("{:<5} {:<20} {:<20} {:<30} {:<30}".format('Valor', 'Freq. Absoluta', 'Freq. Relativa', 'Freq. Absoluta Acumulada', 'Freq. Relativa Acumulada'))

for valor, dados_frequencia in tabela_frequencias.items():
    print("{:<5} {:<20} {:<20} {:<30} {:<30}".format(valor, dados_frequencia['Frequência Absoluta'], round(dados_frequencia['Frequência Relativa'], 2), dados_frequencia['Frequência Absoluta Acumulada'], round(dados_frequencia['Frequência Relativa Acumulada'], 2)))

media = statistics.mean(dados)
mediana = statistics.median(dados)
moda = statistics.mode(dados)
desvio_padrao = statistics.stdev(dados)

print("Letra b):\n") #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

print("Média:         {:.2f}".format(media))
print("Mediana:       {}".format(mediana))
print("Moda:          {}".format(moda))
print("Desvio Padrão: {:.2f}".format(desvio_padrao))

'''
Questão 4: 

4- Calcule a média aritmética, a mediana e a moda para cada um dos seguintes conjuntos
de dados.

a1) 20; 22; 20; 18; 25; 23; 27; 24; 24; 28; 20
a3) 5; 4; 5; 7; 2; 1; 8; 4; 9; 5; 4; 1; 1; 4; 5; 1
a2) 20; 22; 20; 18; 25; 23; 27; 24; 24; 200 ; 20
a4) 113; 105; 108; 107; 110; 105; 113; 109

b) Que conclusões retira da comparação dos resultados de a1) com a2)?

'''
print ("\n QUESTÃO 2) \n")
a1 = [20, 22, 20, 18, 25, 23, 27, 24, 24, 28, 20]
a2 = [20, 22, 20, 18, 25, 23, 27, 24, 24, 200, 20]
a3 = [5, 4, 5, 7, 2, 1, 8, 4, 9, 5, 4, 1, 1, 4, 5, 1]
a4 = [113, 105, 108, 107, 110, 105, 113, 109]

media_a1 = sum(a1) / len(a1)
mediana_a1 = statistics.median(a1)
moda_a1 = statistics.mode(a1)

media_a2 = sum(a2) / len(a2)
mediana_a2 = statistics.median(a2)
moda_a2 = statistics.mode(a2)

media_a3 = sum(a3) / len(a3)
mediana_a3 = statistics.median(a3)
moda_a3 = statistics.mode(a3)

media_a4 = sum(a4) / len(a4)
mediana_a4 = statistics.median(a4)
moda_a4 = statistics.mode(a4)

print("a1) Média: {:.2f}, Mediana: {}, Moda: {}".format(media_a1, mediana_a1, moda_a1))
print("a2) Média: {:.2f}, Mediana: {}, Moda: {}".format(media_a2, mediana_a2, moda_a2))
print("a3) Média: {:.2f}, Mediana: {}, Moda: {}".format(media_a3, mediana_a3, moda_a3))
print("a4) Média: {:.2f}, Mediana: {}, Moda: {}".format(media_a4, mediana_a4, moda_a4))