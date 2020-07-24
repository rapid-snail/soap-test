import os

# url wsdl схемы стенда возьмем из переменной окружения
EMPLOYEE_WSDL_URL = os.environ.get("EMPLOYEE_WSDL_URL", "http://localhost/?wsdl")
