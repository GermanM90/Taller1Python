# funcion sin parametros y no devuelve nada

def Saludar():
    print("Bienvenidos A Las Funciones de Phyton 😎")


def SaludarName(nombre):
    print(f"Hola {nombre},como amaneces hoy?")


def Programa(nombre, nota):
    print(f"Hola {nombre}, tienes una nota de {nota}")


def ProgramaDefault(nombre, nota, programa="Nuevas Tecnologias"):
    print(f"Hola {nombre}, tienes una nota de {nota} en el modulo de {programa}")


def Operaciones(nro1, nro2):
    return (nro1 + nro2, nro1 * nro2)


# Llamar Funciones
if __name__ == "__main__":
    resultado = Operaciones(5, 10)
    nro1 = 5
    nro2 = 10
    print(resultado)
    print(f"{nro1} + {nro2} = {resultado[0]}")
    print(f"{nro1} * {nro2} = {resultado[1]}")
    # ProgramaDefault('Santiago',4.7)
    # ProgramaDefault('Yesid', 4.0,"Base De Datos")
 # Programa("Santiago", 4.5)
 # Programa(nota=5.7,nombre= "Santiago")

# Saludar()
#    SaludarName("Yesid!✔")
#    user = "Yesid Toro😉"
#    SaludarName(user)
#    SaludarName(123)
