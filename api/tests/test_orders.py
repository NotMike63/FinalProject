from fastapi.testclient import TestClient
from ..controllers import orders as controller
from ..main import app
import pytest
from ..models import orders as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_order(db_session):
    # Create a sample order
    order_data = {
        "customer": "John Doe",
        "order_status": True,
        "total_price": 21.99,
        "promotion_code": None
    }

    order_object = model.Order(**order_data)

    # Call the create function
    created_order = controller.create(db_session, order_object)

    # Assertions
    assert created_order is not None
    assert created_order.customer == "John Doe"
    assert created_order.order_status is True
    assert created_order.total_price == 21.99
    assert created_order.promotion_code is None
