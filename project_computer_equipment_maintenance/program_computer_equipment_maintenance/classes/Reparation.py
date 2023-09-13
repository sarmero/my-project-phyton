from structures.List import List


class Reparation:

    list_equipment = List()

    date_repair = 0
    diagnostic = ""
    solution = ""
    cost = 0

    def __init__(self, date_repair, diagnostic, solution, cost):
        self.date_repair = date_repair
        self.diagnostic = diagnostic
        self.solution = solution
        self.cost = cost
