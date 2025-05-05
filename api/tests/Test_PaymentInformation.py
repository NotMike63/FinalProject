import pytest
from api.controllers.PaymentInformation import create, read_all, read_one, update, delete
from api.schemas.PaymentInformation import PaymentInformation, PaymentInformationUpdate
from api.models.PaymentInformation import PaymentInformation as PaymentModel

@pytest.fixture
def db_session(mocker):
    return mocker.Mock()

def test_create_payment_info(db_session):
    data = {
        "card_info": "1234-5678-9012-3456",
        "transaction_status": True,
        "payment_type": "Credit",
        "order_id": 1
    }
    schema = PaymentInformation(**data)
    created = create(db_session, schema)

    assert created.card_info == "1234-5678-9012-3456"
    assert created.transaction_status == True
    assert created.payment_type == "Credit"
    assert created.order_id == 1

def test_read_all_payment_info(db_session):
    db_session.query.return_value.all.return_value = []
    result = read_all(db_session)

    assert result is not None

def test_read_one_payment_info_controller(db_session):
    sample = PaymentModel(
        card_info="1234-5678-9012-3456",
        transaction_status=True,
        payment_type="Credit",
        order_id=42
    )
    db_session.query.return_value.filter.return_value.first.return_value = sample
    result = read_one(db_session, 42)

    assert result.card_info == "1234-5678-9012-3456"
    assert result.transaction_status == True
    assert result.payment_type == "Credit"
    assert result.order_id == 42

def test_update_payment_info_controller(db_session):
    mock_query = db_session.query.return_value.filter.return_value
    mock_query.first.return_value = PaymentModel(
        card_info="1234-5678-9012-3456",
        transaction_status=False,
        payment_type="OldPay",
        order_id=101
    )
    db_session.query.return_value.filter.return_value = mock_query

    update_data = PaymentInformationUpdate(
        transaction_status=True,
        payment_type="UpdatedPay"
    )
    updated = update(db_session, 101, update_data)

    assert updated.payment_type == "UpdatedPay"
    assert updated.transaction_status == False
    assert updated.card_info == "1234-5678-9012-3456"

def test_delete_payment_info_controller(db_session):
    mock_query = db_session.query.return_value.filter.return_value
    mock_query.first.return_value = PaymentModel(
        card_info="1234-5678-9012-3456",
        transaction_status=True,
        payment_type="DeletePay",
        order_id=32
    )
    db_session.query.return_value.filter.return_value = mock_query
    response = delete(db_session, 32)

    assert response.status_code == 204
