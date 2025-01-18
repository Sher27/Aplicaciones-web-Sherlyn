#variables

number_x = 70
number_y = 15

address_id_x = id(number_x)
address_id_y = id(number_y)

print("*** Antes de actualizar la vaiable X ***")
print(address_id_x)
print(address_id_y)

number_x = 20
address_id_x = id(number_x)
print("\n *** Despues de actualizar la variable X ***")
print(address_id_x)
print(address_id_y)