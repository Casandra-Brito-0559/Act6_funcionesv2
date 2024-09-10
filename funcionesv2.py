print("Mas sobre funciones")
# aqui se escriben las funciones
def suma_ab(a,b):
    s=a+b
    return s

def resta_ab(a,b):
    s=a-b
    return s

def Mul_ab(a,b):
    s=a*b
    return s

def Div_ab(a,b):
    s=a/b
    return s
#Llamar a las funciones
print("---Calculando suma---")
n1=int(input("Ingresa el primer numero "))
n2=int(input("Ingresa el segundo numero "))
suma=suma_ab(n1,n2)
print(f"El resultado de {n1} + {n2} es {suma}")

print("---Calculando resta---")

r1=int(input("Ingresa el primer numero "))
r2=int(input("Ingresa el segundo numero "))
res=resta_ab(r1,r2)
print(f"El resultado de {r1} - {r2} es {res}")

print("---Calculando Multiplicacion---")

m1=int(input("Ingresa el primer numero "))
m2=int(input("Ingresa el segundo numero "))
mul=Mul_ab(m1,m2)
print(f"El resultado de {m1} x {m2} es {mul}")

print("---Calculando Division---")

d1=int(input("Ingresa el primer numero "))
d2=int(input("Ingresa el segundo numero "))
div=Div_ab(d1,d2)
print(f"El resultado de {d1} / {d2} es {div}")