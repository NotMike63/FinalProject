import pytest
from api.controllers.promotions import create, read_all, read_one, update, delete
from api.schemas.promotions import PromotionBase, PromotionUpdate
from api.models.promotions import Promotion

@pytest.fixture
def db_session(mocker):
    return mocker.Mock()

def test_create_promotion(db_session):
    data = {
        "code": "SUMMER25",
        "expiration_date": "2025-08-01",
        "is_active": True,
        "discount_type": "percentage",
        "discount_value": 25.0
    }
    schema = PromotionBase(**data)

    created = create(db_session, schema)

    assert created is not None
    assert created.code == "SUMMER25"
    assert created.expiration_date == "2025-08-01"
    assert created.is_active is True
    assert created.discount_type == "percentage"
    assert float(created.discount_value) == 25.0

def test_read_all_promotions(db_session):
    result = read_all(db_session)

    assert result is not None

def test_read_one_promotion(db_session):
    promo = Promotion(
        id=1,
        code="SUMMER25",
        expiration_date="2025-08-01",
        is_active=True,
        discount_type="percentage",
        discount_value=25.0
    )

    db_session.query.return_value.filter.return_value.first.return_value = promo

    result = read_one(db_session, 1)

    assert result.id == 1
    assert result.code == "SUMMER25"

def test_update_promotion(db_session):
    promo = db_session.query.return_value.filter.return_value
    promo.first.return_value = Promotion(
        id=1,
        code="SUMMER25",
        expiration_date="2025-08-01",
        is_active=True,
        discount_type="percentage",
        discount_value=25.0
    )

    update_data = PromotionUpdate(
        code="WINTER10",
        discount_value=10.0
    )
    result = update(db_session, update_data, 1)

    assert result is not None
    assert result.code == "WINTER10"
    assert result.discount_value == 10.0

def test_delete_promotion(db_session):
    promo_mock = db_session.query.return_value.filter.return_value
    promo_mock.first.return_value = Promotion(
        id=1,
        code="SUMMER25",
        expiration_date="2025-08-01",
        is_active=True,
        discount_type="percentage",
        discount_value=25.0
    )

    result = delete(db_session, 1)

    assert result.status_code == 204
