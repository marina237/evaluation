
def sup21(nombre):
    if nombre>=21 :
        print(nombre,"supérieur ou égal à 21")
    else : 
        print(nombre,"non supérieur ou égal à 21")
        
        

test_=sup21(1)



def pairs(liste):
   liste_paires = [ liste[i] for i in range(len(liste)) if liste[i]%2==0]
   return liste_paires


le=[1,2,4]

print(pairs(le))
        



def ajout4(liste):
    nouv=liste.copy()
    nouv.append(4)

    return  nouv
  
    
a=ajout4([])
       


    

    
    

def to_strings(dico):
    li=[]
    for k, v in dico.items(): 
        cote=''
        cote+=str(k)+':'+str(v)
        li.append(cote)
            
        # parcours des clés et valeurs
            
    return li
        
            
print(to_strings({1:2,3:4}))
    




def extremites(liste):
    f=[]
    f +=liste[:2] +liste[-2:]
    
    return f

print(extremites(['a', 'b', 'c', 'd', 'e']))


    

def extremites(liste):
    if len(liste)>4:
        res=[]
        res+=liste[:2]+liste[-2:]
        return res
    else:
        assert len(liste)==None
        return liste



class Mot:

    def __init__(self, mot):

        self.mot = mot
       
    
    def comptelettre(self):
        self.mot.count(self.mot)
        
        
mot = Mot('Bonjour')           





        



 

def tri_et_inverse(li):
    #liste_triee=sorted(li)
    li.sort(reverse=True)
    return li

maliste = [4,7,6]
tri_et_inverse(maliste)

    
    
    
    
    
ville_nom_pays = {'Paris': 'France',' Berlin': 'Allemagne','Madrid': 'Espagne' , 'Moscou': 'Russie'}    

  

