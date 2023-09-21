calcular_subtotal = lambda precio,cantidad : precio*cantidad
calcular_descuento = lambda cantidad, subtotal: .10 * subtotal if cantidad > 10 else 0
calcular_iva= lambda subtotal: 0.19 * subtotal
calcular_total = lambda subtotal,descuento,iva: subtotal-descuento+iva

producto = input("Digite nombre de producto: ")
precio = int(input("Digite el precio por unidad: "))
cantidad = int(input("Digite la cantidad a comprar: "))

subtotal = calcular_subtotal(precio,cantidad)
descuento = calcular_descuento(cantidad,subtotal)
iva= calcular_iva(subtotal)
total = calcular_total(subtotal,descuento,iva)

print(f"producto: {producto}")
print(f"Subtotal: {subtotal}")
print(f"Descuento: {descuento}")
print(f"Iva: {iva}")
print(f"Total a pagar {total}")











