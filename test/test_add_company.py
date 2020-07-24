import random
import string
import pytest
from model.company import Company

err_map = {
    "invalid_repr": "invalid hexadecimal representation",
    "not_fount": "is not found",
    "no_error": ""
}


def gen_str(symbols, max_len):
    return "".join([random.choice(symbols) for _ in range(random.randrange(max_len))])


def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + gen_str(symbols, max_len)


test_data = [
    (Company(name=random_string("Moon_", 10)), err_map['no_error']),
    (Company(name=""), err_map["invalid_repr"])
]


@pytest.mark.parametrize("data", test_data)
def test_add_company(soap, data):
    (company, err_msg) = data
    (found, response, fault) = soap.add_company(company.name)
    if found:
        print("%s" % response)
        assert response.created_at == response.updated_at
        assert response.name == company.name
        assert err_msg == err_map['no_error']
    else:
        print(fault.faultstring)
        assert err_msg != err_map['no_error'] and err_msg in fault.faultstring
        assert fault.faultcode == 'SOAP-ENV:Server'
