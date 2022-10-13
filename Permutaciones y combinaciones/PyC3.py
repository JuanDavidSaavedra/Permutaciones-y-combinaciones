import math

def main():
    n = int(input("Introducir numero de elementos del conjunto 'n': "))
    r = int(input("Introducir numero de agrupaciones 'r': "))
    modo = input("combinacion o permutacion: ")

    if modo.lower().startswith('c'):
        modo = "combinacion"
    elif modo.lower().startswith('p'):
        modo = "permutacion"

    cides = abcde(r, n, modo)
    if modo == "combinacion":
        print("La combinacion es :", cides)
    elif modo == "permutacion":
        print("La permutacion es:", cides)

    def abcde(r,n,modo):
        if modo == "combinacion":
            cides= (math.factorial (n)) // (math.factorial (n-r) * math.factorial (r))
        elif modo == "permutacion":
            cides= (math.factorial (n)) // (math.factorial (n-r))
        return cides

    if __name__ == '__main__':
        main()
        input()