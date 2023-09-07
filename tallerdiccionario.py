# Apellidos y Nombres:
# Monroy Rumay German Fernando
# Toro Garzón Yesid

Paises = {'Pais':'Colombia','Capital':'Bogota','Poblacion':50000}

print(Paises)

opcion = 0
print('Seleccione la opción deseada: ')
print('\n 1. Eliminar \n 2.Actualizar \n 3.Consultar \n 4.Agregar')
opcion = int(input('Digite el valor: '))

while opcion == 1:
    # Logica de eliminar
    Paises.clear()
    print('El diccionario se elimino correctamente!')
    print(Paises)
    break
while opcion == 2:
    # Logica de actualizar
    print('Usted a seleccionado actualizar')
    Paises['Poblacion'] = int(input('Ingrese la poblacion actual del pais: '))
    print('Diccionario actualizado correctamente', Paises)
    break
while opcion == 3:
    # Logica de Consultar
    print('Usted a seleccionado Consultar')
    capital = Paises.get('Capital', 'No encontrada')
    print(f'La Capital de Colombia es siguiente: {capital}')
    break
while opcion == 4:
        # Logica de Agregar
    print('Usted a seleccionado Agregar')
    Paises['Pais'] = input('Ingrese su Pais: ')
    Paises['Capital'] = input('Ingrese la Capital: ')
    Paises['Poblacion'] = int(input('Ingrese la poblacion de su pais: '))
    print(Paises)
    break

otra_operacion = input('¿Desea realizar otra operación? (Sí/No): ')
while otra_operacion.lower() != 'si':
    break

# No nos alcanzó el tiempo para agregar la validacion de las opciones 
