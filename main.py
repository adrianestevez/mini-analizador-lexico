# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from lexico import Lexico


def main():

    entradas_validas_real = ['2','2.666','2.5895', '11999','988']

    entradas_validas_ident = ['adrian','_adrian','adrian_25', 'variable_nueva','variable123']

    entradas_invalidas_real = ['.2', '6.', '3e', '3ad', '22.65ff']

    entradas_invalidas_ident = ['3adrian',' adrian','$', '(&$#%/)','123']

    reales = []
    identificadores = []

    print("Entrada\t\tTipo")
    for entrada in entradas_validas_real:
        lex = Lexico(entrada)
        result = lex.definir()
        print( entrada + "\t\t" + result)

    print("Entrada\t\tTipo")
    for entrada in entradas_validas_ident:
        lex = Lexico(entrada)
        result = lex.definir()
        print(entrada + "\t\t" + result)

    print("Entrada\t\tTipo")
    for entrada in entradas_invalidas_real:
        lex = Lexico(entrada)
        result = lex.definir()
        print(entrada + "\t\t" + str(result))

    print("Entrada\t\tTipo")
    for entrada in entradas_invalidas_ident:
        lex = Lexico(entrada)
        result = lex.definir()
        print(entrada + "\t\t" + str(result))



main()