# Entrada de datos mediante la consola INPUT

name = input('¿Cuál es tu nombre? ')
age = int(input('¿Cuál es tu edad? '))
salary =float(input('¿Cual es tu salario?'))
total_pets = eval(input('¿Cuántas mascotas tienes? '))
university = input('¿Cuál es el nombre de tu universidad? ')

print(f'Hola, me llamo {name}, mi edad es {age} años, tengo {total_pets} mascotas y mi universidad es la {university}.')
print(type(name))
print(type(age))
print(type(salary))
print(type(total_pets))
