#Code

E = EllipticCurve().minimal_model()
A =  1.000*prod((E.Np(p)/p)

for p in prime_range(E.conductor)):
    BSDlist=[[0,0]]
    p = E.conductor().next_prime()

for j in range(1,10000):
    
    for k in range(1,1000):
        A = (A*(E.Np(p)/p))
        p = next_prime(p)
    BSDlist = BSDlist + [[log(log(p), log(A)]]

print(BSDlist)

