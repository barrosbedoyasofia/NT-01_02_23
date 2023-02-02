''' punto1
horaLlegada = 8
horaSalida = 13
precioHora = 4000
precioTotal = (horaSalida-horaLlegada)*precioHora
print ("El precio a pagar es:", precioTotal)
'''
'''
txt = "conceptos básicos de Python"
print (len(txt))
'''

'''
horaLlegada = int(input ("Ingrese la hora de llegada: "))
horaSalida = int(input ("Ingrese la hora de salida: "))
Nombre = input ("Escriba su nombre: ")
valorHora = 5000
totalHrs = horaSalida - horaLlegada
print (Nombre, "usted estuvo parqueado", totalHrs, "hrs,", "debe de pagar: ", (totalHrs*valorHora))
'''

numero1 = int(input("Ingrese el numero dividendo"))
numero2 = int(input("Ingrese el numero divisor"))
resultadoDivision = numero1 // numero2
residuoDivision = numero1 % numero2

print ("El dividendo es:", numero1 , ", El numero divisor es:", numero2, ", El resultado de su division es:", resultadoDivision, ", El residuo de su division es:", residuoDivision)