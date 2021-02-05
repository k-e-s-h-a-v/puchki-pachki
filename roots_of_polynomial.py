import numpy as np

# order of polynomial
order = int(input("Enter order of polynomial : ")) 
  
# Below line read inputs from user using map() function  
coeff = list(map(int,input("\nEnter the coefficients\n(only put space between numbers): ").strip().split()))[:order+1] 
 

p = np.poly1d(coeff, variable= 's')  
                                        
print(p)

rootsp = p.r

print("\nRoots of Polynomial are :", rootsp)


print("\nEvaluating polynomial at x=1:",p(1))#0.5

print("\nCo-efficient of polynomial:", p.c)
