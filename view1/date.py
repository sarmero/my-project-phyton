
from datetime import datetime, timedelta

# entrada = ((9*24)*60)+(((2*30)*24)*60)+((((2023*12)*30)*24)*60)+(8*60)+10
# salida = ((10*24)*60)+(((2*30)*24)*60)+((((2023*12)*30)*24)*60)+(17*60)+30
# diferencia = salida - entrada
# print("An pasado ",diferencia," minutos")



fecha_entrada = '09-02-2023 8:10'
fecha_salida = '10-02-2023 17:30'
fecha1 = datetime.strptime(fecha_entrada, '%d-%m-%Y %H:%M')
fecha2 = datetime.strptime(fecha_salida, '%d-%m-%Y %H:%M')

res = fecha2 - fecha1
min = res/timedelta(seconds=60)
print ("An pasado ",min," minutos")
print("horas :",fecha2.hour,":",fecha2.minute)