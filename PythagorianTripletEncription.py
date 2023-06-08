import random
def encrypt(a, n):
    if a%2==1:
        b=(a*a-1)/2
        c=b+1
    else:
        b=(a*a-4)/4
        c=b+2
    print("a=",a,"b=",int(b),"c=",int(c))
    print(a,"^2+",b,"^2=",int((a*a)+(b*b)))
    print(c,"^2=",int(c*c))
    print("cyphertext=", int(c**n))

def decrypt(cypher, n):
    c=cypher**(1/n)
    a1=(c**2-(c-1)**2)**(1/2)
    a2=(c**2-(c-2)**2)**(1/2)
    print("a1=",a1, "a2=",a2)
a=int(input("Enter plaintext:"))
n=int(input("Enter private key n:"))
encrypt(a, n)
cypher=int(input("Enter cyphertext:"))
n1=int(input("Enter private key n:"))
decrypt(cypher, n1)
index=int(input("Random generate some plains and cypers, how many would you like?"))
max=int(input("what is the max integer for the plain text (and key)?"))
for i in range (index):
  a= random.randint(3, max)
  n = random.randint(3, max)
  print("Plaintext:", a, " Key (n):", n)
  encrypt(a, n)


