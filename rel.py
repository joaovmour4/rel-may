import csv

facsi = open('_PCA 2024 (02) - FACSI.csv', encoding='utf-8')
faec = open('_PCA 2024 (02) - FAEC.csv', encoding='utf-8')
faeel = open('_PCA 2024 (02) - FAEEL.csv', encoding='utf-8')
fageo = open('_PCA 2024 (02) - FAGEO.csv', encoding='utf-8')
fec = open('_PCA 2024 (02) - FEC.csv', encoding='utf-8')
femat = open('_PCA 2024 (02) - FEMAT.csv', encoding='utf-8')
femec = open('_PCA 2024 (02) - FEMEC.csv', encoding='utf-8')
femma = open('_PCA 2024 (02) - FEMMA.csv', encoding='utf-8')
feq = open('_PCA 2024 (02) - FEQ.csv', encoding='utf-8')
profinit = open('_PCA 2024 (02) - PROFINIT.csv', encoding='utf-8')

dic = {}

futureArq =  open('DEMANDAS CADASTRADAS PCA 2024 - LABOTATÓRIOS.csv', encoding='utf-8')
arq_read = csv.reader(futureArq, delimiter=',')
arq_facsi = csv.reader(faec, delimiter=',')

for line in arq_read:
    dic[f'{line[2]}'] = 0



for lineActArq in arq_facsi:
    for key in dic.keys():
        if(key == lineActArq[1]):
            if lineActArq[9] != '' and lineActArq[9] != 'Qtde.':
                dic[key] += int(lineActArq[9])
                # print(lineActArq[9])
                # print(f'cod arquivo futuro: {key}, arq original: {lineActArq[1]}')

print(dic.values())


facsi.close()
faec.close()
faeel.close()
fageo.close()
fec.close()
femat.close()
femec.close()
femma.close()
feq.close()
profinit.close()