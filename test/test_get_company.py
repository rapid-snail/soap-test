import pytest
from model.company import Company

err_map = {
    "invalid_repr": "invalid hexadecimal representation",
    "not_fount": "is not found",
    "no_error": ""
}


test_data = [
    (Company(id="5f146401a46d8d00012cbf7b", created_at="2020-07-19 15:17:21.660000",
            updated_at="2020-07-19 16:38:21.660000", name="Very Good Company 2020"), err_map['no_error']),
    (Company(id="5f158a7249faca0001b68205", created_at="2020-07-20 12:13:38.461000",
            updated_at="2020-07-20 12:13:38.461000", name="Moon1"), err_map['no_error']),
    (Company(id=""), err_map["invalid_repr"]),
    (Company(id="000000000000000000000000"), err_map["not_fount"])
]


@pytest.mark.parametrize("data", test_data)
def test_get_company(soap, data):
    (company, err_msg) = data
    (found, response, fault) = soap.get_company(company.id)
    if found:
        print("%s" % response)
        assert response.id == company.id
        assert response.created_at == company.created_at
        assert response.updated_at == company.updated_at
        assert response.name == company.name
        assert err_msg == err_map['no_error']
    else:
        print(fault.faultstring)
        assert err_msg != err_map['no_error'] and err_msg in fault.faultstring
        assert fault.faultcode == 'SOAP-ENV:Server'
