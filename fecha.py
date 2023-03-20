
import datetime

fecha = input("Ingrese la fecha en formato dd/mm/aaaa: ")
dia, mes, anio = map(int, fecha.split('/'))

fecha_objeto = datetime.datetime(anio, mes, dia)
dias_semana = ('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo')
dia_semana = dias_semana[fecha_objeto.weekday()]

print("El día de la semana correspondiente a la fecha ingresada es:", dia_semana)

#todassonigualesokwswssdv commit v1