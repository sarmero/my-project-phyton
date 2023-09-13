import datetime


class ControlInOut:
    code:int
    registration_number:str
    date_in:str
    time_in:str
    date_out:str
    time_out:str
    minutes:int
    cost:int
    fee:int
    service:bool

    def __init__(self, code:int, registration_number:str, date_in:str, time_in:str):
        self.code = code
        self.registration_number = registration_number
        self.date_in = date_in
        self.time_in = time_in
        self.date_out = 0
        self.time_out = 0
        self.minutes = 0
        self.cost = 0
        self.service = True
        self.fee = 10 #tarifa fija a 10 peso por minuto

    def calculate_minutes(self):
        date_in = self.date_in+" "+self.time_in
        date_out = self.date_out+" "+self.time_out

        inn = datetime.datetime.strptime(date_in, '%d-%m-%Y %H:%M')
        out = datetime.datetime.strptime(date_out, '%d-%m-%Y %H:%M')

        time_elapsed = out - inn
        self.minutes = time_elapsed/datetime.timedelta(minutes=1)


    def calculate_cost(self):
        self.cost = self.minutes * self.fee