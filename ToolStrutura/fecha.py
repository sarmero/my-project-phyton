import datetime


def calcula_minutos(fecha_entrada, hora_entrada, fecha_salida, hora_salida):
        entrada = fecha_entrada+" "+hora_entrada 
        salida = fecha_salida+" "+hora_salida

        ent = datetime.datetime.strptime(entrada, '%d-%m-%Y %H:%M')
        sal = datetime.datetime.strptime(salida, '%d-%m-%Y %H:%M')

        tiempo_trascurrido = sal - ent
        minutos = tiempo_trascurrido/datetime.timedelta(minutes=1)

        return minutos

# ------- con esto sacamos la fecha y hora -------------
date = datetime.datetime.now() #captura la fecha de hoy
fecha = date.strftime('%d-%m-%Y') #la fecha
hora = date.strftime('%H:%M') #la hora

# ----- vamos a suponer que la salida es ---------------
fecha_salida = '22-02-2023' 
hora_salida = '17:00'

min = calcula_minutos(fecha, hora, fecha_salida, hora_salida)

print("la fecha es: ",fecha," ",hora," minutos")
print("an trascurrido: ",min)
