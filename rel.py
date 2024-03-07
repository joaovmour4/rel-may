import csv

arqFacs = []

arq1 = open('_PCA 2024 (02) - FACSI.csv', encoding='utf-8')
arq2 = open('_PCA 2024 (02) - FAEC.csv', encoding='utf-8')
arq3 = open('_PCA 2024 (02) - FAEEL.csv', encoding='utf-8')
arq4 = open('_PCA 2024 (02) - FAGEO.csv', encoding='utf-8')
arq5 = open('_PCA 2024 (02) - FEC.csv', encoding='utf-8')
arq6 = open('_PCA 2024 (02) - FEMAT.csv', encoding='utf-8')
arq7 = open('_PCA 2024 (02) - FEMEC.csv', encoding='utf-8')
arq8 = open('_PCA 2024 (02) - FEMMA.csv', encoding='utf-8')
arq9 = open('_PCA 2024 (02) - FEQ.csv', encoding='utf-8')
arq0 = open('_PCA 2024 (02) - PROFINIT.csv', encoding='utf-8')
arq10 = open('_PCA 2024 (02) - IGE.csv', encoding='utf-8')
arq11 = open('_PCA 2024 (02) - PPGCF.csv', encoding='utf-8')

arqFacs.append(csv.reader(arq1, delimiter=','))
arqFacs.append(csv.reader(arq2, delimiter=','))
arqFacs.append(csv.reader(arq3, delimiter=','))
arqFacs.append(csv.reader(arq4, delimiter=','))
arqFacs.append(csv.reader(arq5, delimiter=','))
arqFacs.append(csv.reader(arq6, delimiter=','))
arqFacs.append(csv.reader(arq7, delimiter=','))
arqFacs.append(csv.reader(arq8, delimiter=','))
arqFacs.append(csv.reader(arq9, delimiter=','))
arqFacs.append(csv.reader(arq0, delimiter=','))
arqFacs.append(csv.reader(arq10, delimiter=','))
arqFacs.append(csv.reader(arq11, delimiter=','))

facs = ['FACSI', 'FAEC', 'FAEEL', 'FAGEO', 'FEC', 'FEMAT', 'FEMEC', 'FEMMA', 'FEQ', 'PROFINIT', 'IGE', 'PPGCF']


# futureArq =  open('DEMANDAS CADASTRADAS PCA 2024 - LABOTATÓRIOS.csv', encoding='utf-8')
futureArq =  open('DEMANDAS CADASTRADAS PCA 2024 - FERRAMENTAS.csv', encoding='utf-8')
arq_read = csv.reader(futureArq, delimiter=',')

dic = {}
for line in arq_read:
    dic[f'{line[2]}'] = 0

def dicionario(dic, arqFac):
    for lineActArq in arqFac:
        for key in dic.keys():
            if(key == lineActArq[1]):
                if lineActArq[9] != '' and lineActArq[9] != 'Qtde.':
                    dic[key] = int(lineActArq[9])
                    # print(lineActArq[9])
                    # print(f'cod arquivo futuro: {key}, arq original: {lineActArq[1]}')
    return dic

finDic = {}
for key in dic.keys():
    finDic[f'{key}'] = ''

def finDicionario(dic, finDic, arqFacs, facs, i):
    # for i in range(len(arqFacs)):
    arq_fac = arqFacs[i]
    dic = dicionario(dic, arq_fac)
    for key in dic.keys():
        if dic[key] != 0 and key != '' and key != 'Código SIPAC':
            finDic[key] += f'{facs[i]}({dic[key]}), '
    return finDic




finDic = finDicionario(dic, finDic, arqFacs, facs, 0)
finDic = finDicionario(dic, finDic, arqFacs, facs, 1)
finDic = finDicionario(dic, finDic, arqFacs, facs, 2)
finDic = finDicionario(dic, finDic, arqFacs, facs, 3)
finDic = finDicionario(dic, finDic, arqFacs, facs, 4)
finDic = finDicionario(dic, finDic, arqFacs, facs, 5)
finDic = finDicionario(dic, finDic, arqFacs, facs, 6)
finDic = finDicionario(dic, finDic, arqFacs, facs, 7)
finDic = finDicionario(dic, finDic, arqFacs, facs, 8)
finDic = finDicionario(dic, finDic, arqFacs, facs, 9)
finDic = finDicionario(dic, finDic, arqFacs, facs, 10)
finDic = finDicionario(dic, finDic, arqFacs, facs, 11)


# print(finDic)

with open('relatorio_final.txt', 'w') as arq:
    for key in finDic.keys():
        if key != '' and key != 'Código SIPAC':
            arq.writelines(f'{key} = {finDic[key]}\n')

futureArq.close()
arq1.close()
arq2.close()
arq3.close()
arq4.close()
arq5.close()
arq6.close()
arq7.close()
arq8.close()
arq9.close()
arq0.close()
arq10.close()
arq11.close()
