

class Description:
    __code_medicine = ""
    __amount = 0
    __value_unit = 0

    def __init__(self,code_medicine,amount,value_unit) :
        self.__code_medicine = ""
        self.__amount = 0
        self.__value_unit = 0

    def get_code_medicine(self):
        return self.__code_medicine
    
    def get_amount(self):
        return self.__amount
    
    def get_value_unit(self):
        return self.__value_unit