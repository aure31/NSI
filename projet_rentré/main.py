import csv
from os.path import abspath, dirname, join

def pathToList(path:str) -> list[dict]:
    listdict = []
    with open((path+'.csv'), newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            if row['ANNEE'] != '':
                listdict.append(row)
    return listdict

def toTuple(l:list[dict]) -> list[tuple]:
    listtuple = []
    for d in l:
        tuple = (d['CD_STATION'], toFloat(d['MOYPTOT']),toFloat(d['MAXPTOT']))
        listtuple.append(tuple)
    return listtuple


def triList(l:list[tuple],n:int) -> list[tuple]:
    if n == 2 or n==3:
        n-=1
        for t in range(len(l)):
            min = t
            for i in range(t+1,len(l)):
                if l[i][n] < l[min][n]:
                    min = i
            l[t],l[min] = l[min],l[t]
    return l

def toFloat(str:str) -> float:
    return float(str.replace(',','.'))

def divList(l:list[tuple]) -> list[tuple]:
    good= []
    bad= []
    limit = []
    for t in range(len(l)):
        #print(l[t][1])
        if l[t][1] < 0.1:
            if(l[t][2] > 0.5):
                limit.append(l[t])
            else:
                good.append(l[t])
        else:
            bad.append(l[t])
    return (good,bad,limit)

def toFile(l:list[tuple],pathr:str):
    with open((dirname(abspath(__file__))+"/"+pathr+'.csv'), mode='w', newline='') as csvfile:
        fieldnames = ['CD_STATION', 'MOYPTOT', 'MAXPTOT']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        for t in l:
            writer.writerow({'CD_STATION': t[0], 'MOYPTOT': t[1], 'MAXPTOT': t[2]})

def allFile():
    l = pathToList('/workspaces/NSI/projet_rentré/moy_tot_quantif_2012')
    good = divList(triList(toTuple(l),2))[0]
    toFile(good,'result/good')
    bad = divList(triList(toTuple(l),2))[1]
    toFile(bad,'result/bad')
    limit = divList(triList(toTuple(l),2))[2]
    toFile(limit,'result/limit')

allFile()