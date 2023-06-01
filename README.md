# IAConnect4

## Heuristica
Para construir la heurística final basándonos en los 4 papers mencionados arriba tomaremos en cuenta que el valor básico de colocar la ficha será de 3, es decir no importa la posición, fichas adyacentes, o cualquier circunstancia el valor intrínseco propio de la ficha será de 3. Además de esto se tomarán en cuenta los siguientes tres aspectos para tomar una decisión en la heurística

Valor de ficha propia adyacente: es decir que nivel de fila provoca provoca poner esa moneda, siendo que hay 5 niveles a pesar de que el nivel 5 tiene el mismo valor de victoria que el 4. para esto se asignara una variable n que tomará el valor de su nivel, es decir si la ficha que se colocará provocará que hayan 3 en fila el valor de n sera de 3, lo que provocará que el cambio del valor del movimiento a 3n
Valor defensivo: el valor defensivo es aquel que provocamos al detener un movimiento del rival, ya que es complicado determinar cuándo se provoca una parada adecuada, el valor defensivo tendrá un valor menor al de la adyacencia propia pues este algoritmo busca ser un poco más agresivo, para ello por cada ficha rival que se bloquee o a la que se vuelva adyacente al usar la ficha se multiplicará por 1.5, este valor será asignado a una variable arbitraria k, por lo que finalmente nuestro valor defensivo se sumara por la cantidad de fichas que sean adyacentes a nuestra ficha jugada por lo que tendremos que k crecerá conforme tenga más fichas rivales adyacentes, es decir 3*k
Valor estratégico posicional: El valor estratégico posicional hace referencia a la posición del “tablero”(matriz) en la que se coloca la ficha, ya que por simple probabilidad mientras más céntrico sea un movimiento, nos da más variedad de movimientos futuros, pero desde mi perspectiva este valor es el menos significativo, por lo que será una suma simple, siendo que la columna del todo central será un +7, las dos próximas un +5, las siguientes dos un +3 y la última un +1, en caso de ser 0, es que el tiro no es válido.


Por lo que nuestra operación final de la heurística quedará de la siguiente manera:

		T=Fn*k+p
		

	Donde:
	T es el valor total del tiro
	F es la ficha a tirar de valor base 3
	k el valor defensivo de la tirada
	p el valor estratégico posicional.




### Referencias:
Chaudhary, S., Pandey, S., & Khera, M. H. Alpha-Beta Pruning in Mini-Max Algorithm–An Optimized Approach for a Connect-4 Game.

Nasa, R., Didwania, R., Maji, S., & Kumar, V. (2018). Alpha-beta pruning in mini-max algorithm–an optimized approach for a connect-4 game. Int. Res. J. Eng. Technol, 1637-1641.

SHEORAN, K., DHAND, G., DABASZS, M., DAHIYA, N., & PUSHPARAJ, P. (2022). SOLVING CONNECT 4 USING OPTIMIZED MINIMAX AND MONTE CARLO TREE SEARCH.

Kang, X. , Wang, Y. and Hu, Y. (2019) Research on Different Heuristics for Minimax Algorithm Insight from Connect-4 Game. Journal of Intelligent Learning Systems and Applications, 11, 15-31. doi: 10.4236/jilsa.2019.112002.
