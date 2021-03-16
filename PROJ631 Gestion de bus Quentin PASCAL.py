#-*- coding: utf-8 -*-
import datetime

# Implémentaion de l'exemple des deux lignes de bus

data_file_name_l1 = 'C:/Users/Donnees/data/1_Poisy-ParcDesGlaisins.txt'
data_file_name_l2 = 'C:/Users/Donnees/data/2_Piscine-Patinoire_Campus.txt'

try:
    with open(data_file_name_l1, 'r', encoding = 'utf-8') as f:
        content_l1 = f.read()
except OSError:
    # 'File not found' error message.
    print("File not found")

try:
    with open(data_file_name_l2, 'r', encoding = 'utf-8') as f:
        content_l2 = f.read()
except OSError:
    # 'File not found' error message.
    print("File not found")
    
def dates2dic(dates):
    dic = {}
    splitted_dates = dates.split("\n")
    #print(splitted_dates)
    for stop_dates in splitted_dates:
        tmp = stop_dates.split(" ")
        dic[tmp[0]] = tmp[1:]
        #print(tmp[0])
        #print(tmp[1:])
    return dic

slited_content_l1 = content_l1.split("\n\n")
slited_content_l2 = content_l2.split("\n\n")

regular_path_l1 = slited_content_l1[0]
#print(regular_path)
regular_date_go_l1 = dates2dic(slited_content_l1[1])
#print(regular_date_go)
regular_date_back_l1 = dates2dic(slited_content_l1[2])

regular_path_l2 = slited_content_l2[0]
#print(regular_path_l2)
regular_date_go_l2 = dates2dic(slited_content_l2[1])
#print(regular_date_go)
regular_date_back_l2 = dates2dic(slited_content_l2[2])

#we_holidays_path = slited_content[3]
#we_holidays_date_go = dates2dic(slited_content[4])
#we_holidays_date_back = dates2dic(slited_content[5])


# Création de la classe Arrêt qui représente les arrÃªts de bus

class Arret:
    
    def __init__(self, label, heuresD = []):
    
        self.label = label
        self.heuresD = heuresD
        
    def estTerminus(self):
            
        return self.children == None
    
    def get_label(self):
            
        return self.label
    
    def get_heuresD(self):
            
        return self.heuresD
    
    
    def prochain_depart_le_plus_proche(self, heure_selec): #Méthode permettant de donner le prochain arrêt à un arrêt de bus en fonction d'une heure passée en paramètre
        
        heure = datetime.datetime.strptime(heure_selec, '%H:%M') #On transforme la chaine de caractères passée en paramètre en une date au format Heure:Minute
        
        compteur_terminus = 1 #On initialise un compteur qui va permettre de tester le dernier horaire 
        for arret in range(len(self.get_heuresD())): #On test donc tous les horaires
            
            if self.get_heuresD()[-compteur_terminus] == '-': #Si l'horaire correspond à '-' dans les données
                
                compteur_terminus += 1 #On test avec l'arrêt précédent
            
        if heure > datetime.datetime.strptime(self.get_heuresD()[-compteur_terminus], '%H:%M'): #Si cette heure est supérieur au dernier arrêt de la journée
            
            texte_plus_de_bus = "Il n'y a plus de bus aujourd'hui" #C'est qu'il n'y a plus de bus aujourd'hui
            return texte_plus_de_bus
            
        else: #Sinon, il faut trouver le prochain arrêt
            intervalle_le_moins_grand = abs(heure - datetime.datetime.strptime(self.get_heuresD()[-compteur_terminus], '%H:%M')) #L'intervale le plus grand est établi entre l'horaire en paramètre et le dernier bus de la jounée
            prochain_départ_le_plus_proche = dates2dic(self.get_heuresD()[0]) # Le prochain départ est établi comme étant le premier départ de la journée
    
        for arret in range(len(self.get_heuresD())): #Nous allons tester tous les horaires des arrêts des bus
            
            if self.get_heuresD()[arret] == '-': #On gère le problème des bus qui ne s'arrêtent pas à certains arrêts
                
                continue; #Permet de revenir en haut de la boucle for
            
            
            if abs(heure - datetime.datetime.strptime(self.get_heuresD()[arret], '%H:%M')) < intervalle_le_moins_grand: #Si l'intervale entre l'horaire en paramètre et celui testé est plus petit que le plus petit intervalle 
                
                if datetime.datetime.strptime(self.get_heuresD()[arret], '%H:%M') - heure < (datetime.datetime.strptime('00:00', '%H:%M') - datetime.datetime.strptime('00:00', '%H:%M')): #Si l'horaire de l'arrêt de bus n'est pas avant l'horaire passé en paramètre
                    
                    pass; #On ne le compte pas
                
                else:
                    
                    intervalle_le_moins_grand = datetime.datetime.strptime(self.get_heuresD()[arret], '%H:%M') - heure #On réassigne l'intervalle le moins grand avec le nouvel horaire

                
                    prochain_départ_le_plus_proche = self.get_heuresD()[arret] #Le prochain départ deviens l'horaire qu'on testait 

                    return prochain_départ_le_plus_proche #On retourne la première heure valide pour gagner du temps et ne pas continuer à faire tourner le programme
        
    
        
#Créations des arrêts pour chaques lignes

    
a1 = Arret("LYCÉE_DE_POISY", dates2dic(slited_content_l1[1]).get("LYCÉE_DE_POISY"))
a2 = Arret("POISY_COLLÈGE", dates2dic(slited_content_l1[1]).get("POISY_COLLÈGE"))
a3 = Arret("Vernod", dates2dic(slited_content_l1[1]).get("Vernod"))
a4 = Arret("Meythet_Le_Rabelais", dates2dic(slited_content_l1[1]).get("Meythet_Le_Rabelais"))
a5 = Arret("Chorus", dates2dic(slited_content_l1[1]).get("Chorus"))
a6 = Arret("Mandallaz", dates2dic(slited_content_l1[1]).get("Mandallaz"))
a7 = Arret("GARE", dates2dic(slited_content_l1[1]).get("GARE"))
a8 = Arret("France_Barattes", dates2dic(slited_content_l1[1]).get("France_Barattes"))
a9 = Arret("C.E.S._Barattes", dates2dic(slited_content_l1[1]).get("C.E.S._Barattes"))
a10 = Arret("VIGNIÈRES", dates2dic(slited_content_l1[1]).get("VIGNIÈRES"))
a11 = Arret("Ponchy", dates2dic(slited_content_l1[1]).get("Ponchy"))
a12 = Arret("PARC_DES_GLAISINS", dates2dic(slited_content_l1[1]).get("PARC_DES_GLAISINS"))

a12_r = Arret("LYCÉE_DE_POISY", dates2dic(slited_content_l1[2]).get("LYCÉE_DE_POISY"))
a11_r = Arret("POISY_COLLÈGE", dates2dic(slited_content_l1[2]).get("POISY_COLLÈGE"))
a10_r = Arret("Vernod", dates2dic(slited_content_l1[2]).get("Vernod"))
a9_r = Arret("Meythet_Le_Rabelais", dates2dic(slited_content_l1[2]).get("Meythet_Le_Rabelais"))
a8_r = Arret("Chorus", dates2dic(slited_content_l1[2]).get("Chorus"))
a7_r = Arret("Mandallaz", dates2dic(slited_content_l1[2]).get("Mandallaz"))
a6_r = Arret("GARE", dates2dic(slited_content_l1[2]).get("GARE"))
a5_r = Arret("France_Barattes", dates2dic(slited_content_l1[2]).get("France_Barattes"))
a4_r = Arret("C.E.S._Barattes", dates2dic(slited_content_l1[2]).get("C.E.S._Barattes"))
a3_r = Arret("VIGNIÈRES", dates2dic(slited_content_l1[2]).get("VIGNIÈRES"))
a2_r = Arret("Ponchy", dates2dic(slited_content_l1[2]).get("Ponchy"))
a1_r = Arret("PARC_DES_GLAISINS", dates2dic(slited_content_l1[2]).get("PARC_DES_GLAISINS"))

#Création des arrêts de la ligne 2

b1 = Arret("PISCINE-PATINOIRE", dates2dic(slited_content_l2[1]).get("PISCINE-PATINOIRE"))
b2 = Arret("Arcadium", dates2dic(slited_content_l2[1]).get("Arcadium"))
b3 = Arret("Parc_des_Sports", dates2dic(slited_content_l2[1]).get("Parc_des_Sports"))
b4 = Arret("Place_des_Romains", dates2dic(slited_content_l2[1]).get("Place_des_Romains"))
b5 = Arret("Courier", dates2dic(slited_content_l2[1]).get("Courier"))
b6 = Arret("GARE", dates2dic(slited_content_l2[1]).get("GARE"))
b7 = Arret("Bonlieu", dates2dic(slited_content_l2[1]).get("Bonlieu"))
b8 = Arret("Préfecture_Pâquier", dates2dic(slited_content_l2[1]).get("Préfecture_Pâquier"))
b9 = Arret("Impérial", dates2dic(slited_content_l2[1]).get("Impérial"))
b10 = Arret("Pommaries", dates2dic(slited_content_l2[1]).get("Pommaries"))
b11 = Arret("VIGNIÈRES", dates2dic(slited_content_l2[1]).get("VIGNIÈRES"))
b12 = Arret("CAMPUS", dates2dic(slited_content_l2[1]).get("CAMPUS"))

b12_r = Arret("PISCINE-PATINOIRE", dates2dic(slited_content_l2[2]).get("PISCINE-PATINOIRE"))
b11_r = Arret("Arcadium", dates2dic(slited_content_l2[2]).get("Arcadium"))
b10_r = Arret("Parc_des_Sports", dates2dic(slited_content_l2[2]).get("Parc_des_Sports"))
b9_r = Arret("Place_des_Romains", dates2dic(slited_content_l2[2]).get("Place_des_Romains"))
b8_r = Arret("Courier", dates2dic(slited_content_l2[2]).get("Courier"))
b7_r = Arret("GARE", dates2dic(slited_content_l2[2]).get("GARE"))
b6_r = Arret("Bonlieu", dates2dic(slited_content_l2[2]).get("Bonlieu"))
b5_r = Arret("Préfecture_Pâquier", dates2dic(slited_content_l2[2]).get("Préfecture_Pâquier"))
b4_r = Arret("Impérial", dates2dic(slited_content_l2[2]).get("Impérial"))
b3_r = Arret("Pommaries", dates2dic(slited_content_l2[2]).get("Pommaries"))
b2_r = Arret("VIGNIÈRES", dates2dic(slited_content_l2[2]).get("VIGNIÈRES"))
b1_r = Arret("CAMPUS", dates2dic(slited_content_l2[2]).get("CAMPUS"))




# Création de la classe Ligne qui représente les différentes lignes (aller et retour)

class Ligne:
    
    def __init__(self, label, depart, arrets = [], trajets = []):
        
        self.label = label
        self.depart = depart
        self.arrets = arrets
        self.trajets = trajets
    
    def get_label(self):
            
        return self.label    
    
    def get_depart(self):
            
        return self.depart
    
    def get_arrets(self):
            
        return self.arrets
    
    def get_trajets(self):
            
        return self.trajets
    
    def trouve_trajet(self, arretD, arretA, horaire): #Fonction qui affiche les arrêts par lesquels on passe ainsi que l'heure d'arrêt, elle prend en paramètre un arrêt de départ, un arrêt d'arrivé et une heure
        
        
        for arret in range(len(self.get_trajets())): #On test tous les arrêts du bus
            
            if self.get_trajets()[arret][0].prochain_depart_le_plus_proche(horaire) == "Il n'y a plus de bus aujourd'hui": 
                
                print("Il n'y a plus de bus aujourd'hui") #C'est qu'il n'y a plus de bus aujourd'hui
                break
            
            if self.get_trajets()[arret][0].prochain_depart_le_plus_proche(horaire) == '-': #Si le bus ne s'arrête pas à cet arrêt, il y a un '-' dans les données
                
                self.trouve_trajet(self.get_trajets()[arret][1], arretA, self.get_trajets()[arret][0].prochain_depart_le_plus_proche(horaire)) #On rapelle la fonction avec l'horaire d'arrêt suivant
            
            if self.get_trajets()[arret][0] == arretD: #Si l'arrêt de bus en question correspond à l'arrêt de départ (qui change à chaque appel)
                
                print("Arrêt : ", self.get_trajets()[arret][0].get_label()," Horaire : ", self.get_trajets()[arret][0].prochain_depart_le_plus_proche(horaire)) #On affiche son nom et l'heure à laquelle le bus passe
                
                if self.get_trajets()[arret][1] != arretA: #Si l'arrêt en question ne correspond pas à la destination
                    
                    self.trouve_trajet(self.get_trajets()[arret][1], arretA, self.get_trajets()[arret][0].prochain_depart_le_plus_proche(horaire)) #On rapelle la fonction avec l'arrêt suivant et avec un horaire d'arrêt plus tard que le précédent 
            
                else:
                    
                    print("Arrêt : ", self.get_trajets()[arret][1].get_label()," Horaire : ", self.get_trajets()[arret][1].prochain_depart_le_plus_proche(self.get_trajets()[arret][0].prochain_depart_le_plus_proche(horaire))) #Sinon, on affiche le nom de l'arrêt de destination et l'heure à laquelle on arrive
        
        
    
l1_a = Ligne("Ligne 1", a1, [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12], [(a1,a2), (a2,a3), (a3,a4), (a4,a5), (a5,a6), (a6,a7), (a7,a8), (a8,a9), (a9,a10), (a10,a11), (a11,a12)] )
l1_r = Ligne("Ligne 1", a1_r, [a1_r,a2_r,a3_r,a4_r,a5_r,a6_r,a7_r,a8_r,a9_r,a10_r,a11_r,a12_r], [(a1_r,a2_r), (a2_r,a3_r), (a3_r,a4_r), (a4_r,a5_r), (a5_r,a6_r), (a6_r,a7_r), (a7_r,a8_r), (a8_r,a9_r), (a9_r,a10_r), (a10_r,a11_r), (a11_r,a12_r)] )

l2_a = Ligne("Ligne 2", b1, [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12], [(b1,b2), (b2,b3), (b3,b4), (b4,b5), (b5,b6), (b6,b7), (b7,b8), (b8,b9), (b9,b10), (b10,b11), (b11,b12)] )
l2_r = Ligne("Ligne 2", b1_r, [b1_r,b2_r,b3_r,b4_r,b5_r,b6_r,b7_r,b8_r,b9_r,b10_r,b11_r,b12_r], [(b1_r,b2_r), (b2_r,b3_r), (b3_r,b4_r), (b4_r,b5_r), (b5_r,b6_r), (b6_r,b7_r), (b7_r,b8_r), (b8_r,b9_r), (b9_r,b10_r), (b10_r,b11_r), (b11_r,b12_r)] )



        

# Création de la classe Reseau qui met en relation les lignes
        
class Reseau:
    
    def __init__(self, lignes = []):
        
        self.lignes = lignes
        
    def get_lignes(self):
        
        return self.lignes
    
    def estDans2Lignes(self, arretD, arretA): #Fonction prenant en paramètre un arrêt de départ et un arrêt d'arrivée, retourne vrai si ils sont sur deux lignes différentes, faux sinon
        
        if arretD in l1_a.get_arrets() or arretD in l2_a.get_arrets(): #Testons le sens de l'allé
        
            if (arretD in l1_a.get_arrets()) == (arretA in l2_a.get_arrets()): #Si les arrêts ne sont pas sur la même ligne
            
                return True
        
            else: 
            
                return False #Alors c'est qu'ils sont sur la même
            
        if arretD in l1_r.get_arrets() or arretD in l2_r.get_arrets(): #Testons de sens retour
        
            if (arretD in l1_r.get_arrets()) == (arretA in l2_r.get_arrets()): #Si les arrêts ne sont pas sur la même ligne
            
                return True
        
            else:
            
                return False #Alors c'est qu'il sont sur la même
            
    def trouve_trajet_reseau(self, arretD, arretA, horaire): #Fontion qui devait remplir la fonctionnalité finale du programme mais qui ne marche pas
        
        if self.estDans2Lignes(arretD, arretA) == False: #Si les deux arrêts sont sur la même ligne, on utilise la fonction de la classe Ligne
            
            if arretD in l1_a.get_arrets():
                
                l1_a.trouve_trajet(arretD, arretA, horaire)
            
            elif arretD in l1_r.get_arrets():
                
                l1_r.trouve_trajet(arretD, arretA, horaire)
            
            elif arretD in l2_a.get_arrets():
                
                l2_a.trouve_trajet(arretD, arretA, horaire)
                
            elif arretD in l2_r.get_arrets():
                
                l2_r.trouve_trajet(arretD, arretA, horaire)
        
        else:
            
            for ligne in self.get_lignes():
                
                 for arret in range(len(ligne.get_trajets())):
            
                    if ligne.get_trajets()[arret][0] == arretD:
                        
                        ligne.trouve_trajet(arretD, arretA, horaire)

r1 = Reseau([l1_a, l1_r, l2_a, l2_r])

#print(r1.estDans2Lignes(l1_a.get_arrets()[1], l2_a.get_arrets()[9]))
#r1.trouve_trajet_reseau(l2_a.get_arrets()[1], l1_a.get_arrets()[9], "10:30")

#Partie fonctionnelle du programme (main) :

#On demande à l'utilisateur de saisir un arrêt de départ, un arrêt de destination et l'heure à laquelle on pense être à l'arrêt de départ.

print("Veuillez choisir la ligne que vous voulez emprunter : Ligne n°"),
ligne_saisie = input()

if ligne_saisie == '1':
    
    print("Vers Parc des Glaisins ou vers Lycée de Poisy ? ")
    sens = input()
    if sens == 'Parc des Glaisins':
        ligne = l1_a
    if sens == 'Lycée de Poisy':
        ligne = l1_r
        
if ligne_saisie == '2':
    
    print("Vers Campus ou vers Piscine Patinoire ? ")
    sens = input()
    if sens == 'Campus':
        ligne = l2_a
    if sens == 'Piscine Patinoire':
        ligne = l2_r

print("Veuillez saisir l'arrêt de bus d'où vous voulez partir :"),
arret_saisi = input()
for arret in ligne.get_arrets():
    
    if arret.get_label() == arret_saisi:
        
        arretD = arret


print("Veuillez saisir l'arrêt de bus où vous voulez aller :"),
arret_saisie = input()
for arret in ligne.get_arrets():
    
    if arret.get_label() == arret_saisie:
        arretA = arret

print("Veuillez saisir l'heure à laquelle vous serez à l'arrêt de départ :"),
horaire = input()

print("\n Trajet :")

ligne.trouve_trajet(arretD, arretA, horaire)

        
        
        
#Tests des différentes fonctions        
    

"""    
for arret in range(len(l1.get_trajets())):
    rint(l1.get_trajets()[arret][0].get_label(),l1.get_trajets()[arret][1].get_label())

print(l1.get_arrets()[4].get_heuresD())

l1_a.trouve_trajet(a1, a12, '10:30')
print('----------')
l1_r.trouve_trajet(a1_r, a9_r, '6:30')
print('----------')
l2_a.trouve_trajet(b1, b9, '6:30')
print('----------')
l2_r.trouve_trajet(b3_r, b9_r, '11:30')


date_time_str = dates2dic(slited_content[1]).get("Vernod")[1]
date_time_obj = datetime.datetime.strptime(date_time_str, '%H:%M')
print(date_time_obj)
date_time_str1 = '6:12'
date_time_obj1 = datetime.datetime.strptime(date_time_str1, '%H:%M')
print(date_time_obj1)
print(date_time_obj - date_time_obj1)

print((date_time_obj1 - date_time_obj) < (date_time_obj - date_time_obj1))

print((datetime.datetime.strptime('0:0', '%H:%M') - datetime.datetime.strptime('0:0', '%H:%M')))

    
heure = datetime.datetime.strptime(horaire, '%H:%M') #On transforme la chaine de caractères passée en paramètre en une date au format Heure:Minute
heureD = arretD.prochain_depart_le_plus_proche(horaire)

print(self.get_heuresD()[arret])
print(datetime.datetime.strptime(self.get_heuresD()[arret], '%H:%M'))        
        
compteur = 1
for trajet in range(len(regular_date_go.values())):
    
    for arret,heure in regular_date_go.items():
                  
            print(arret, heure[compteur])
            print('----------')
        
    compteur += 1
    print('TERMINUS\n')        
    
#Tests

#print(a2.get_label())
#print(dates2dic(slited_content[1]).get("Vernod")[0])
#print(a4.get_heuresD()[-2])
#print(a1.prochain_depart_le_plus_proche('17:40'))
"""      
        
        
        
        
        
