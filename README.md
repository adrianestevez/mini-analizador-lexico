# Mini Analizador Lexico

## Explicación
La función **definir()** en el archivo lexico.h evalua el primer caracter de la cadena es una letra o guión bajo para mandarlo entonces al autómata de Identificadores o si es un numero para pasarlo al autómata de Reales. Para esto se hacen la funcion **es_Letra()** y la funcion **isReal()** donde mediante la comparación de los caracteres ascii se identifica si es un numero o una letra o guión bajo. Si no es uno de estos significa que es inválido.
[![Diagrama 1](https://github.com/adrianestevez/mini-analizador-lexico/blob/main/Diagrama%201.png)](https://github.com/adrianestevez/mini-analizador-lexico/blob/main/Diagrama%201.png)


Mientras tanto la función **automataId()** en el archivo lexico.h evalua si la cadena empieza por una letra o un guión bajo, ya después de esto acepta números y letras

[![Diagrama 2](https://github.com/adrianestevez/mini-analizador-lexico/blob/main/Diagrama%202.png)](https://github.com/adrianestevez/mini-analizador-lexico/blob/main/Diagrama%202.png)


Por último ,la función **automataReal()** en el archivo lexico.h evalua si la cadena empieza por un número, en caso de que así sea se permiten todos los demás números, en caso de que venga un punto se pasa al ultimo estado obligatoriamente, sino sería un error y ya en el último estado, o sea después del punto, se espera que todo sea números o igua sería inválido

[![Diagrama 3](https://github.com/adrianestevez/mini-analizador-lexico/blob/main/Diagrama%203.png)](https://github.com/adrianestevez/mini-analizador-lexico/blob/main/Diagrama%203.png)
