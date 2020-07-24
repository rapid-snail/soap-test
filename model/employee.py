class Employee:

    def __init__(self, id=None, created_at=None, updated_at=None, first_name=None, last_name=None, middle_name=None):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name

    def update_from_soap(self, obj):
        self.id = str(obj.Id)
        self.created_at = obj.CreatedAt
        self.updated_at = obj.UpdatedAt
        self.first_name = obj.FirstName
        self.last_name = obj.LastName
        self.middle_name = obj.MiddleName
        return self

    def __repr__(self):
        return "Employee{id=%s И=%s Ф=%s О=%s Ct=%s Ut=%s}" % (self.id, self.first_name, self.last_name,
                                                               self.middle_name, self.created_at, self.updated_at)

