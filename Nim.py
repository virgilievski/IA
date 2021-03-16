import random
"""Programme permettant de faire jouer 2 machines au jeu de Nim.
Jeu de Nim: On dispose 21 batonnets l'un à coté de l'autre. 2 joueurs, tour par tour, choisissent 1, 2 ou 3 batonnet. Le joueur récupérant le dernier batonnet a perdu la partie
Par un jeu de récompense et de punition, on apprend aux machines à trouver le schéma permettant de gagner à tous les coups si on joue en premier."""
#  création d'une machine composé de n boites et de k billes de chaque types différents:(1, 2, 3) batons
def nouvelleMachine(n, k):
    machine=[]
    for j in range(n):
        machine.append([k,k,k])
    machine[0]=[k,0,0]
    machine[1]=[k,k,0]
    return machine

#  affichage d'une machine
def afficheMachine(machine):
    for i in range(0, len(machine)):
        print("[", i+1, "]\t", end='')
    print("\n", end='')
    for j in range(0, 3):
        for boite in machine:
            print(boite[j], "\t", end='')
        print("\n", end='')


#  réconpense (on donne des billes aux types qui ont permi le succès dans les bonnes boites)
def recompense(machine, listeCoups):
    for i in range(len(listeCoups)):
        k=listeCoups[i][0]
        p=listeCoups[i][1]
        machine[k-1][p-1]+=3
    return machine

#  punition (réciproque à récompense)
def punit(machine, listeCoups):
    for i in range(len(listeCoups)):
        k=listeCoups[i][0]
        p=listeCoups[i][1]
        machine[k-1][p-1]-=1
    return machine


#  l'IA fait un coup aléatoire dans la boite k (1, 2 ou 3 batons)
def joueCoup(machine, k):
    n=machine[k-1][0]+machine[k-1][1]+machine[k-1][2]
    if n==0:
        return -1
    else:
        x= random.randint(1, n)
        if x<=machine[k-1][0]:
            return 1
        elif x<=machine[k-1][1]+machine[k-1][0]:
            return 2
        elif x<=machine[k-1][0]+machine[k-1][1]+machine[k-1][2]:
            return 3


#  Partie entre 2 machines. Renvoie les listes des coups et le vainqueur
def jouePartie(machine1, machine2):
    n=len(machine1)
    listeCoup1=[]
    listeCoup2=[]
    while n!=0:
        k1=joueCoup(machine1, n)
        if k1==-1:
            return (listeCoup1, listeCoup2, 0)
        else:
            listeCoup1.append((n,k1))
            n=n-k1
            if n==0:
                return (listeCoup1, listeCoup2, 0)
            else:
                k2=joueCoup(machine2, n)
                if k2==-1:
                    return (listeCoup1, listeCoup2, 1)
                else:
                    listeCoup2.append((n,k2))
                    n=n-k2
    return (listeCoup1, listeCoup2, 1)


# Créez deux nouvelles machines
machine1 = nouvelleMachine(13, 2)
machine2 = nouvelleMachine(13, 2)

# Fonction qui prend deux machines, simule une partie, et renvoie les deux machines récompensée/punie
def Apprentissage(machine1, machine2):
    (coups1, coups2, result)= jouePartie(machine1, machine2)

    for i in range(0, len(coups1)):
        print(coups1[i][0], "bâtonnets restants : machine1 retire", coups1[i][1], "bâtonnets")
        if i < len(coups2):
            print(coups2[i][0], "bâtonnets restants : machine2 retire", coups2[i][1], "bâtonnets")
    if result == 1:
        print("machine1 a gagné")
        recompense(machine1, coups1)
        punit(machine2, coups2)
        return afficheMachine(machine1) , afficheMachine(machine2)
    else:
        print("machine1 a perdu")
        recompense(machine2, coups2)
        punit(machine1, coups1)
        return afficheMachine(machine1) , afficheMachine(machine2)
    
# Test sur un grand nombre de répétitions des étapes 2 et 3
for i in range(100):
    print(Apprentissage(machine1, machine2))
