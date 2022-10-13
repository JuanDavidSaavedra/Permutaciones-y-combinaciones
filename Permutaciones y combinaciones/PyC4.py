import math

def main():
  n = int(input("Introducir número de elementos del conjunto: "))
  r = int(input("Introducir número de agrupaciones: "))
  if r>n:
    print("El número de agrupaciones no puede ser mayor que el número de elementos del conjunto")
    print(quit())
  
  modo = input("¿Vas a elegir combinacion o permutacion? Digite c en caso de combinación, sino p para permutación [c/p]: ")

  if modo.lower().startswith('c'):
    modo = "combinacion"

  elif modo.lower().startswith('p'):
    modo = "permutacion"

  cides = abcde(r, n, modo)
  if modo == "combinacion":
    print(("La combinacion es :", cides))
  elif modo == "permutacion":
    print(("La permutacion es :", cides))

def abcde(r,n,modo):
    if modo == "combinacion":
        cides= math.factorial (n) // (math.factorial (n-r) * math.factorial (r))
    elif modo == "permutacion":
        cides= math.factorial (n) // (math.factorial (n-r))
    return cides

if __name__ == '__main__':
    main()
    input()