import pytest
import random
import string
from model.employee import Employee

err_map = {
    "invalid_repr": "invalid hexadecimal representation",
    "not_fount": "is not found",
    "no_error": ""
}


def gen_str(symbols, max_len):
    return "".join([random.choice(symbols) for _ in range(random.randrange(max_len))])


def random_string(prefix, max_len):
    symbols = string.ascii_letters + " "
    return prefix + gen_str(symbols, max_len)


test_data = [
    (Employee(id="5f17fe2949faca0001b68212", first_name=random_string("fn_", 50), last_name=random_string("ln_", 50),
              middle_name=random_string("mn_", 50)), err_map['no_error']),
    (Employee(id="5f17fe2949faca0001b68212", first_name=random_string("fn_", 50), last_name=random_string("ln_", 50), middle_name=""), err_map['no_error']),
    (Employee(id="5f17fe2949faca0001b68212", first_name=random_string("fn_", 50), last_name=random_string("ln_", 50), middle_name=None), err_map['no_error']),
    (Employee(id="5f17fe2949faca0001b68213", first_name=random_string("fn_", 50), last_name=random_string("ln_", 50), middle_name=""), err_map['not_fount'])
]


@pytest.mark.parametrize("data", test_data)
def test_update_employee(soap, data):
    (employee, err_msg) = data
    (found, response, fault) = soap.update_employee(employee.id, employee.first_name, employee.last_name, employee.middle_name)
    if found:
        print("%s" % response)
        assert response.last_name == employee.last_name
        assert err_msg == err_map['no_error']
        assert response.created_at != response.updated_at
        assert response.first_name == employee.first_name
    else:
        print(fault.faultstring)
        assert err_msg != err_map['no_error'] and err_msg in fault.faultstring
        assert fault.faultcode == 'SOAP-ENV:Server'
