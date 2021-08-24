class Lexico:
    cadena = ""

    def __init__(self, cadena):
        self.cadena = cadena

    def definir(self):
        i=0
        #evaluamos la primera letra
        c = self.cadena[i];
        if(c!=None and self.isReal(c)) :
            result = self.automataReal()
            if(result):
                return "Real"
            else:
                return "Invalido"
        elif(c!=None and self.es_Letra(c)):
            result = self.automataId()
            if (result):
                return "Cadena"
            else:
                return "Invalido"
        elif(c==None):
            print("La cadena que ha escrito es nula")
        else:
            return "Invalido"



    # comienzo de automata para numeros
    def automataReal(self):
        estado = 0
        continuar = True
        exito = True
        i = 0

        while (continuar and i < len(self.cadena)):
            c = self.cadena[i]
            if (estado == 0):
                if (c != None and self.isReal(c)):
                    estado = 1
                    i += 1
                else:
                    exito = False
                    continuar = False
            elif(estado == 1):
                #si es un punto pasamos al estado 2
                if(ord(c)== 46):
                   estado = 2
                   i += 1
                elif(self.isReal(c) != True):
                    exito = False
                    continuar = False
                else:
                    i += 1

            elif(estado == 2):
                if(self.isReal(c)):
                    estado = 3
                    i+=1
                else:
                    exito = False
                    continuar = False

            elif (estado == 3):
                if (self.isReal(c)):
                    i += 1
                else:
                    exito = False
                    continuar = False

        return exito



        #Si la cadena no es nula y está entre los caracteres ascii del 48 al 57 significa que entonces el primer caracter de la
        #cadena es un numero por tanto lo mandamos a la funcion que define los reales
    def isReal(self, c):
        if (ord(c) >= 48 and ord(c) <= 57):
            return True
        else:
            return False

        # Si la cadena no es nula y está entre los caracteres ascii del 65 al 90 (letras minusculas) o desde el 97 al 122 (letras mayusculas)
        #además admitimos el guion bajo "_"
    def es_Letra(self, c):
        if (((ord(c) >= 65 and ord(c) <= 90) or ord(c) == 95) or ((ord(c)>=97 and ord(c)<=122) or ord(c) == 95)):
            return True
        else:
            return False


    # comienzo del automata para Id
    def automataId(self):
        estado = 0
        continuar = True
        exito = True
        i = 0

        while (continuar and i < len(self.cadena)):
            c = self.cadena[i]
            if (estado == 0):
                if (c != None and self.es_Letra(c)):
                    estado = 1
                    i += 1
                else:
                    exito = False
                    continuar = False
            elif (estado == 1):
                # si es
                if ((c != None and self.es_Letra(c)) or (c != None and self.isReal(c))):
                    i += 1
                else:
                    exito = False
                    continuar = False

        return exito
