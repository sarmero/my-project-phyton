

from datetime import datetime, timedelta


class ControlInputOutput():
    __code = ""
    __id = ""
    __user = ""
    __tuition = ""
    __date_input = None
    __time_input = None
    __date_output = None
    __time_output = None
    __service = True
    __cost = 0
    __time = 0

    def __init__(self, code, id, user, tuition, date_input, time_input):
        self.__code = code
        self.__id = id
        self.__user = user
        self.__tuition = tuition
        self.__date_input = date_input
        self.__time_input = time_input
        self.__service = True
        self.__cost = 0
        self.__time = 0

    def set_tarife(self, tarife):
        self.__tarife = tarife

    def get_date_input(self):
        return self.__date_input

    def get_time_input(self):
        return self.__time_input

    def get_date_output(self):
        return self.__date_output

    def get_time_output(self):
        return self.__time_output

    def get_user(self):
        return self.__user

    def get_tuition(self):
        return self.__tuition

    def get_code(self):
        return self.__code

    def get_id(self):
        return self.__id

    def is_service(self):
        return self.__service

    def set_service(self, service):
        self.__service = service

    def get_time(self):
        return self.__time
    
    def get_cost(self):
        return self.__cost

    def set_departure_date(self, date, time):
        self.__date_output = date
        self.__time_output = time

    def parking_cost(self):
        time = self.__time_()
        time_hours = time/timedelta(hours=1)  # Tiempo trascurrido en horas
        self.__cost = self.__tarife * time_hours

        return self.__cost

    def __time_(self):
        fecha_entrada = self.__date_input+" "+self.__time_input + ":00.0"
        fecha_salida = self.__date_output+" "+self.__time_output + ":00.0"
        print(fecha_entrada)
        print(fecha_salida)
        format = '%d-%m-%Y %H:%M:%S.%f'
        fecha1 = datetime.strptime(fecha_entrada, format)

        fecha2 = datetime.strptime(fecha_salida, format)
        time = fecha2 - fecha1

        return time

    def time(self):
        res = self.__time_()
        # tiempo trascurrido en minutos
        time_minute = res/timedelta(seconds=60)
        time_hours = res/timedelta(hours=1)  # Tiempo trascurrido en horas
        hour = int(time_hours)
        min = time_minute - (hour * 60)
        minute = int(min)
        

        if minute != 0:
            time = str(hour) + "h - " + str(minute) + "m"
        else:
            time = str(hour) + " horas"

        self.__time = time

        return time
