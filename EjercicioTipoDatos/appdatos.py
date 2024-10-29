# La situación es esta: tú trabajas en una empresa donde los vendedores
# reciben comisiones del 13% por sus ventas totales, y tu jefe quiere que
# ayudes a los vendedores a calcular sus comisiones creando un
# programa que les pregunte su nombre y cuánto han vendido en este
# mes. Tu programa le va a responder con una frase que incluya su
# nombre y la cantidad que le corresponde por las comisiones.


nombre = input("¿Cuál es tu nombre? ")
venta = float(input("¿Cuánto has vendido este mes? "))
comisiones = (venta * 0.13)
print(f"{nombre}, tus comisiones son de €{comisiones:.2f}")