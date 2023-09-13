from controller.ListMaintenance import ListMaintenance
from structures.List import List
from data.StorageEquipment import StorageEquipment


class Maintenance:

    code = 0
    code_equipment = 0
    date_input = 0
    description_fail = ""

    def __init__(self, code, code_equipment, date_input, description_fail):
        self.code = code
        self.code_equipment = code_equipment
        self.date_input = date_input
        self.description_fail = description_fail
