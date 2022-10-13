from itertools import combinations 

r = int(input("Digite el número a combinar 'r' : "))
comb = combinations([1, 2, 3, 4, 5, 6], r) 
  
for i in list(comb): 
    print (i) 