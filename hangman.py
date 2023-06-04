import random
import sys

horca = [
    """
     ======+
          []
          []
          []
        ======
    """,
    """
     ======+
     0    []
          []
          []
        ======
    """,
    """
     ======+
     0    []
    /     []
          []
        ======
    """,
    """
     ======+
     0    []
    /|\   []
          []
        ======
    """,
    """
     ======+
     0    []
    /|\   []
    /     []
        ======
    """,
    """
     ======+
     0    []
    /|\   []
    / \   []
        ======
    You loose!!
    """,
]
with open("/home/rafael/python/projects/hangman/allWords.txt", "r") as archivo:
    todos_los_caracteres = archivo.read()
    todas_las_palabras = list(map(str, todos_los_caracteres.split()))
    palabra_clave = random.choice(todas_las_palabras).lower()


class Main:
    contador = 0

    def __init__(self, palabra_clave):
        self.palabra_clave = palabra_clave
        self.respuesta = ["_"] * len(self.palabra_clave)

        print(horca[self.contador])
        print("_ " * len(self.palabra_clave))

    def encontrar_letra(self, cadena, letra):
        return [i for i, l in enumerate(cadena) if l == letra]

    def letras(self, cadena):
        cadena.lower()
        if (
            cadena == self.palabra_clave
            or "".join(self.respuesta) == self.palabra_clave
        ):
            print(
                f"""
                ############################
                  Ganaste... La palabra era: {self.palabra_clave}
                ############################
                """
            )
            sys.exit()
        elif len(cadena) < 1 or len(cadena) > 30:
            print("Ingrese 1 letra como mínimo y 30 como máximo")
        elif not cadena.isalpha():
            print("Ingrese un caracter válido.")
        else:
            for i in cadena:
                self.letras_l = self.encontrar_letra(palabra_clave, i)
                if self.letras_l:
                    for x in self.letras_l:
                        self.respuesta[x] = i
                    print(horca[self.contador])
                else:
                    print(
                        f"""
                    El caracter '{i}' no se encuentra en la respuesta.
                    """
                    )
                    self.contador += 1
                    print(horca[self.contador])
                print(
                    f"""
                      {" ".join(self.respuesta)}"""
                )


if __name__ == "__main__":
    main = Main(palabra_clave)
    while "".join(main.respuesta) != palabra_clave:
        if main.contador <= 4:
            main.letras(input("Ingrese el texto: "))
        else:
            print(
                """
            Game over.
            """
            )
            print(
                f"""
                  La palabra era: '{palabra_clave}'
                  """
            )
            break
    else:
        print(
            """
          &&&&&&&&&&&&&&&
          &  You Win!!! &
          &&&&&&&&&&&&&&&
        """
        )
