
def main():
    #escribe tu código abajo de esta línea
    def pliego(x,y):
    uno = x * 12
    dos = y * 35

    if uno < dos:
        print("El número maxiomo de tarjetas que se pueden hacer es: ",uno)
    else:
        print("El número maximo de tarjetas que se pueden hacer es: ",dos)


    pli = int(input("Dame la cantidad de pliegos de papel albanene: "))
    plu = int(input("Dame la cantidad de plumones: "))

    pliego(pli,plu)

    pass

if __name__=='__main__':
    main()
