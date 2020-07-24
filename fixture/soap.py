from suds.client import Client
from suds import WebFault
from model.company import Company
from model.employee import Employee


class SoapFixture:

    def __init__(self, url):
        self.url = url

    def get_company(self, id):
        client = Client(self.url, faults=True)

        try:
            response = client.service.GetCompany(id)
        except WebFault as e:
            return (False, None, e.fault)

        company = Company().update_from_soap(response)
        return (True, company, None)

    def add_company(self, name):
        client = Client(self.url, faults=True)

        try:
            response = client.service.AddCompany(name)
        except WebFault as e:
            return (False, None, e.fault)

        company = Company().update_from_soap(response)
        return (True, company, None)

    def add_employees_to_company(self, company_id, employees_id):
        client = Client(self.url, faults=True)

        try:
            response = client.service.AddEmployeesToCompany(company_id, employees_id)
        except WebFault as e:
            return (False, None, e.fault)

        company = Company().update_from_soap(response)
        return (True, company, None)

    def add_employee(self, first_name, last_name, middle_name):
        client = Client(self.url, faults=True)

        try:
            response = client.service.AddEmployee(first_name, last_name, middle_name)
        except WebFault as e:
            return (False, None, e.fault)

        employee = Employee().update_from_soap(response)
        return (True, employee, None)

    def update_employee(self, id, first_name, last_name, middle_name):
        client = Client(self.url, faults=True)

        try:
            response = client.service.UpdateEmployee(id, first_name, last_name, middle_name)
        except WebFault as e:
            return (False, None, e.fault)

        employee = Employee().update_from_soap(response)
        return (True, employee, None)
