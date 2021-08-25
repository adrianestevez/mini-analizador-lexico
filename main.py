# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from lexico import Lexico

def procesar(array):

    print("Entrada\t\tTipo")
    for entrada in array:
        lex = Lexico(entrada)
        result = lex.definir()
        print(entrada + "\t\t" + result)

    print()


def main():

    entradas_validas_real = ['2','2.666','2.5895', '11999','988'] #arreglo de entradas validas reales
    entradas_validas_ident = ['adrian','_adrian','adrian_25', 'variable_nueva','variable123']#arreglo de entradas validas identificador
    entradas_invalidas_real = ['.2', '6.', '3e', '3ad', '22.65ff']#arreglo de entradas NO validas reales
    entradas_invalidas_ident = ['3adrian',' adrian','$', '(&$#%/)','123']#arreglo de entradas NO validas identificador

    procesar(entradas_validas_real)
    procesar(entradas_validas_ident)
    procesar(entradas_invalidas_real)
    procesar(entradas_invalidas_ident)


main()