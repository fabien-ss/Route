
def permute(mot, stri, depart, n):
    if(depart == len(stri) or depart > len(stri)):
        return mot
    #mot.append(stri[depart])
    i = len(mot)+1
    #while(i < len(stri)):
    mot.append(stri[depart])
    i +=1
    return permute(mot, stri, depart+1, n-1)

def permutaion(stri, n):
    if n == len(stri) - 1:
        print("here")
        return [stri.copy()]
    r = []
    for i in range(n, len(stri)):
        stri[n], stri[i] = stri[i], stri[n]
        sub = permutaion(stri, n+1)
        r.extend(sub)
        stri[n], stri[i] = stri[i], stri[n]
    return r    
stri = ["a","b"]
n = 0
valiny = []
rep = permutaion(stri,  0)
print(rep)
        
    
        
            
    
    
    
    
    
    
    
    
    
    