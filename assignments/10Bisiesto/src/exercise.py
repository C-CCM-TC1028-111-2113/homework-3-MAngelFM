
def main():
    #escribe tu código abajo de esta línea
    def es_bisiesto(agnio):
    if agnio % 400 == 0:
        print("True")
    elif agnio % 100 == 0:
        print("False")
    elif agnio % 4 == 0:
        print("True")
    else:
        print("False")

agnio = int(input(""))

es_bisiesto(agnio)
    pass

if __name__=='__main__':
    main()
