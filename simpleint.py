def si(P,T,R):
    res = (int(P) * int(T) * int(R) )/100
    res = int(res)
    return res
    
P = input()
T = input()
R = input()
print(si(P,T,R))