""" EL ABECEDARIO DE J BALVIN
Después del éxito del álbum Colores, donde cada canción era el nombre de un
color, el conocido cantante J Balvin anuncia un nuevo álbum llamado Abecedario.
Al enterarse de la noticia, Mario y Arturo, discuten si este nuevo álbum tendrá
una canción por cada letra del abecedario, pero llegan a la conclusión de que
es poco probable que esto suceda debido a la gran cantidad de letras.
Por lo tanto hacen una apuesta y cada uno hace una lista con las canciones que
creen que aparecerán en el disco. Después de estrenarse el álbum, los dos
amigos te piden el favor de crear un programa que lea cada canción del albúm y
les diga quién va ganando la apuesta. Si Arturo (A), Mario (M) o nadie (N).
Nota: Una misma canción puede aparecer dos veces en el álbum, y debe sumar
puntos.
- Entrada: La entrada consta de tres listas, la primera línea son las
predicciones de Arturo, la segunda las de Mario y la tercera es el listado de
las canciones que salieron en el álbum.
- Salida: Una lista de caracteres (A, M o N) indicando quién va ganando la
apuesta después de leer cada canción del albúm. """


def win(arturo, mario, album):
    res = ''
    rounds_A = 0
    rounds_M = 0
    for song in album:
        if song in arturo:
            rounds_A += 1
        if song in mario:
            rounds_M += 1
        if rounds_A > rounds_M:
            res += 'A'
        elif rounds_M > rounds_A:
            res += 'M'
        else:
            res += 'N'
    print(res)


win('PSJFT', 'BKPAS', 'ZGCFCETLNVESQCTK')  # NNNAAAAAAAAAAAAA
win('SRNMAO', 'XJGLAQ', 'SHKBVOHILFBPMXSMLKSTN')  # AAAAAAAAAAAAAAAAAAAAA
win('CUH', 'MSZ', 'ERIMINSNCBNHHCU')  # NNNMMMMMMMMNAAA
