a = [1,2,3]
b = [4,5,6]

#pasa los elementos del arreglo a a b
print("Valores originales")
print(f"a {a}")
print(f"b {b}")
#de esta forma se crea un nuevo objeto
c = a[:]
a = b[:]
b = c[:]
print("Valores Intercambiados")
print(f"a {a}")
print(f"b {b}")