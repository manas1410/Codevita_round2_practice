# cook your dish here

'''
Input:
2
1 10
7 10
Output:
4
None
'''
limits = []
max_nos = 0
t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    limits.append([a,b])
    max_nos = max(b,max_nos)
    
cp = [0]*(max_nos+1)
prime_cou = [0]*(max_nos+1)
sieve = [True]*(max_nos +1)
sieve[0] = sieve[1] = False


for factor in range(2,len(sieve)):
    if sieve[factor] == True:
        cp[factor] = cp[factor-1]+1 
    else:
        cp[factor] = cp[factor-1]
        
    if sieve[cp[factor]]:
        prime_cou[factor] = prime_cou[factor-1]+1  
    else:
        prime_cou[factor] = prime_cou[factor-1]
        
    for j in range(factor*factor,len(sieve),factor):
        sieve[j] = False
        
#print(limits)
for case in limits:
    #print(case)
    ans = (prime_cou[case[1]]-prime_cou[max(0,case[0]-1)])
    if ans ==0:
        print(None)
    else:
        print(ans)
#print(cp)
#print(prime_cou)

    
