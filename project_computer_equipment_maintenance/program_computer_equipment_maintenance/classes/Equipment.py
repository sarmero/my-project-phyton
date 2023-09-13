from controller.ListMaintenance import ListMaintenance


class Equipment:
    code = 0
    mark = ""
    model = ""
    description = ""
    owner = ""
    phone = ""
    email = ""

    def __init__(self, code, mark, model, description, owner, phone, email):
        self.code = code
        self.mark = mark
        self.model = model
        self.description = description
        self.owner = owner
        self.phone = phone
        self.email = email
