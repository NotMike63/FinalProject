import pytest
from api.controllers.customer import create_customer, get_all_customers, get_customer, delete_customer
from api.schemas.customer import CustomerCreate
from api.models.customer import Customer

@pytest.fixture
def db_session(mocker):
    return mocker.Mock()

def test_create_customer(db_session):
    data = {
        "name": "John Doe",
        "email": "JohnDoe@example.com",
        "phone": "123-456-7890",
        "address": "123 Wall St"
    }
    schema = CustomerCreate(**data)

    created = create_customer(db_session, schema)

    assert created is not None
    assert created.name == "John Doe"
    assert created.email == "JohnDoe@example.com"
    assert created.phone == "123-456-7890"
    assert created.address == "123 Wall St"

def test_get_all_customers(db_session):
    customers = get_all_customers(db_session)

    assert customers is not None

def test_get_customer(db_session):
    customer = Customer(**{
        "name": "John Doe",
        "email": "JohnDoe@example.com",
        "phone": "123-456-7890",
        "address": "123 Wall St"
    })
    db_session.query.return_value.filter.return_value.first.return_value = customer

    result = get_customer(db_session, 1)
    assert result is not None
    assert result.name == "John Doe"
    assert result.email == "JohnDoe@example.com"
    assert result.phone == "123-456-7890"
    assert result.address == "123 Wall St"

def test_delete_customer(db_session):
    db_session.query.return_value.filter.return_value.first.return_value = None

