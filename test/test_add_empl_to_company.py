import pytest

err_map = {
    "invalid_repr": "invalid hexadecimal representation",
    "not_fount": "is not found",
    "no_error": ""
}


# employee_id  5f17d00049faca0001b6820f 5f17e86a49faca0001b68210
test_data = [
    ("5f146401a46d8d00012cbf7b", ["5f159eeb49faca0001b68206",
                                  "5f159f9da46d8d00012cbf7c"
                                  "5f15a084a46d8d00012cbf7d",
                                  "5f1712eba46d8d00012cbf89"
                                 ], err_map['no_error']),
    ("000000000000000000000000", ["5f159eeb49faca0001b68206"], err_map['not_fount']),
    ("5f146401a46d8d00012cbf7b", ["000000000000000000000000"], err_map['not_fount']),
    ("", [""], err_map['invalid_repr']),
    # в схеме указано, что может не быть EmployeeId
    ("5f146401a46d8d00012cbf7b", [], err_map['no_error'])
]


@pytest.mark.parametrize("data", test_data)
def test_add_empl_to_company(soap, data):
    (company_id, employees_ids, err_msg) = data
    (found, response, fault) = soap.add_employees_to_company(company_id, employees_ids)

    if found:
        print(response)
        assert company_id == response.id
        assert len(response.employees) == len(employees_ids)
        assert err_msg == err_map['no_error']
    else:
        print(fault.faultstring)
        assert err_msg != err_map['no_error'] and err_msg in fault.faultstring
        assert fault.faultcode == 'SOAP-ENV:Server'
