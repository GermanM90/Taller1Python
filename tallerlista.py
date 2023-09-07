# Apellidos y Nombres:
# Monroy Rumay German Fernando
# Toro Garzón Yesid

Paises = ['Colombia', 'Peru', 'Chile', 'Venezuela']

opcion = 0
print('Seleccione la opción deseada: ')
print('\n 1. Agregar \n 2.Actualizar \n 3.Consultar \n 4.Eliminar')
opcion = int(input('Digite el valor: '))

while opcion == 1:
    # Logica de Agregar
    Paises.append('Brasil')
    print('Pais Agregado correctamente!')
    print(Paises)
    break
while opcion == 2:
    # Logica actualizar
    Paises[2] = 'Argentina'
    print(Paises)
    break
while opcion == 3:
    # Logica Consultar
    print('La cantidad de Paises en la lista es de: ', len(Paises))
    print('Los Paises en la lista son:', (Paises))
    break
while opcion == 4:
    # Logica Eliminar
    Paises.clear()
    print('Lista eliminada correctamente')
    break

otra_operacion = input('¿Desea realizar otra operación? (Sí/No): ')
while otra_operacion.lower() != 'si':
    break
# No nos alcanzó el tiempo para agregar la validacion de las opciones 
    
    
