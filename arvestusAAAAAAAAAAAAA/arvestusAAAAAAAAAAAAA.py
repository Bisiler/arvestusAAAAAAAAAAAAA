import random 
sportsman=[] 
results=[] 
mins=50 
b = sorted(results) 
def names(sportsman,results): 
    for i in range (3): 
        man=(input("имя спортсмена ?")) 
        result=random.randint(3,60) 
        sportsman.append(man) 
        results.append(result)
    return sportsman,results

def SpisokDej(jhj, asda):
    print("лучшие результаты-BestRes \n дисквалификация-WorstRes")
    vibor=input("выбирай...")
    if vibor=='BestRes':
        luchshij(Fresults_dict)
        
    elif vibor=='WorstRes':
        worst(Fresults_dict,c,d)

def luchshij(fresults_dict):
    c = sorted(Fresults_dict)
    print('лучший результат это:',c[0],'минут',Fresults_dict[c[0]])

def Worst(c):
    d = c.reverse
    print('худший результаты:',c[0],'минут',Fresults_dict[d[0]])

sportsman, results=names(sportsman, results)
Fresults_dict = dict(zip(results, sportsman))
while True:
    SpisokDej(Fresults_dict, Worst)


#def Tres(sportsman,results,mins): 
 #Fresults_dict = dict(zip(sportsman, results)) 
 #print(Fresults_dict) 
 
 #for c in results: 
 #if c<mins: 
 #print 
 #results.remove(c)
