from datetime import datetime, timedelta

fecha_entrada = '08-02-2023 8:10'
fecha_salida = '10-02-2023 17:30'
fecha1 = datetime.strptime(fecha_entrada, '%d-%m-%Y %H:%M')
fecha2 = datetime.strptime(fecha_salida, '%d-%m-%Y %H:%M')

res = fecha2 - fecha1
# print("horas :",fecha2.hour,":",fecha2.minute)

time_minute = res/timedelta(seconds=60)
time_hours = res/timedelta(hours=1)
hour = int(time_hours)
minute= time_minute - (hour * 60)

print ("An pasado ",time_minute," minutos")
print ("An pasado ",hour," horas con ",int(minute)," minutos")
