import pytest
from fixture.soap import SoapFixture
import config

@pytest.fixture(scope="session")
def soap(request):
    soap_fixture = SoapFixture(url=config.EMPLOYEE_WSDL_URL)
    return soap_fixture
