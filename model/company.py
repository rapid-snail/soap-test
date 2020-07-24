from model.employee import Employee


class Company:

    def __init__(self, id=None, created_at=None, updated_at=None, name=None, employees=None):
        if employees is None:
            employees = []

        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.name = name
        self.employees = employees

    def update_from_soap(self, obj):
        self.id = str(obj.Id)
        self.created_at = obj.CreatedAt
        self.updated_at = obj.UpdatedAt
        self.name = obj.Name
        if hasattr(obj, "employees"):
            self.employees = [Employee().update_from_soap(x) for x in obj.employees]
        return self

    def __repr__(self):
        s = "Company{id=%s created=%s updated=%s name=%s employees=%s}" % (self.id,
                                                                           self.created_at,
                                                                           self.updated_at,
                                                                           self.name,
                                                                           self.employees)
        return s
