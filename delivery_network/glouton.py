#Question 18:
from graph import Graph, graph_from_file
routes="routes.01.in"
camions = "/home/onyxia/work/Projet-de-programmation-RAVELOMANANA-MORO/input/trucks.0.in"
g= graph_from_file("/home/onyxia/work/Projet-de-programmation-RAVELOMANANA-MORO/input/network.00.in")
print(g.cout_profit(1,2,6,camions))
'''Problème du sac à dos
On utilise un algorithme glouton qui va parcourir les trajets selon l'odre de leur rapport profit/cout et garder le maximum. Cela donne simplement une approximation du résultat voulu mais est plus rapide qu'une méthode exacte.
'''
class Trajet: 
    def __init__(self, cout, profit, indice): 
        """Cette fonction calcul le rapport profit/cout d'un objet de la classe Trajet"""
        self.indice = indice         
        self.cout = cout 
        self.profit = profit
        self.rapport = profit // cout 
  #Fonction pour la comparaison entre deux Trajets
  #On compare le rapport calculé pour les trier
    def __lt__(self, other): 
        """Cette fonction compare le rapport profit/cout de l'objet de la classe Trajet avec celui d'un autre Trajet"""
        return self.rapport < other.rapport 
  






    '''La fonction suivante getProfitMax prend en paramètres les couts et profits des trajets ainsi que le budget et renvoie le profit maximum réalisable, les trajets effectués et les camions achetés pour le réaliser
    
    Paramètres:
    
    couts : list of int
    profits : list of int
    budget : int    
    
    Return:
    
    (compteurValeur,Trajets,Camions)=(int,list,list)
    '''


    def getProfitMax(couts, profits, budget):
            Trajets=[]
            Camions=[]
            tableauTrie = [] 
            for i in range(len(couts)): 
                tableauTrie.append(Trajet(couts[i], profits[i], i)) 
    
            #Trier les trajets par leur rapport
            tableauTrie.sort(reverse = True) 
    
            compteurValeur = 0
            for trajet in tableauTrie: 
                coutCourant = int(trajet.cout) 
                profitCourant = int(trajet.profit) 
                if budget - coutCourant >= 0: 
                    #on ajoute le trajet dans l'ensemble des trajets à effectuer
                    #On soustrait le budget
                    budget -= coutCourant 
                    compteurValeur += profitCourant
                    #On ajoute le profit du trajet
                    Trajets.append(trajet)
                    #On ajoute le trajet dans la liste
                    #On va maintenant chercher le camion correspondant au coût du trajet:
                    catalogue= open(camions, "r")
                    lines=[list(map(int,catalogue.readline().split(' ')))]
                    camion= [l for l in lines if l[1]==trajet.cout and l[0]==max([h[0] for h in lines])]
                    camion=camion[0]
                    Camions.append(camion)
                    
                    
            return compteurValeur,Trajets,Camions 


    print(getProfitMax([900000, 200000], [100000, 100000], 1200000))
