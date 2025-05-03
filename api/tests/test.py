import pytest
from ..controllers import orders as order_controller
from ..controllers import order_details as order_details_controller
from ..controllers import RatingsAndReviews as ratings_reviews_controller
from ..models import orders as order_model
from ..models import order_details as order_details_model
from ..models import RatingsAndReviews as ratings_reviews_model
from ..dependencies.database import get_db
import datetime


@pytest.fixture
def db():
    session = next(get_db())
    yield session
    session.close()


def test_create_order(db):
    order = order_model.Order(
        order_status=False,
        order_date=datetime.datetime.now(),
        total_price=20.00,
        customer="Snow Caps"
    )
    result = order_controller.create(db, order)
    assert result.customer == "Snow Caps"


def test_read_order(db):
    order = order_model.Order(
        order_status=False,
        order_date=datetime.datetime.now(),
        total_price=25.00,
        customer="Ready von Ready"
    )
    created = order_controller.create(db, order)
    result = order_controller.read_one(db, created.order_id)
    assert result.total_price == 25.00


def test_delete_order(db):
    order = order_model.Order(
        order_status=False,
        order_date=datetime.datetime.now(),
        total_price=30.00,
        customer="Heidi Ho"
    )
    created = order_controller.create(db, order)
    response = order_controller.delete(db, created.order_id)
    assert response.status_code == 204


def test_create_order_detail(db):
    order = order_model.Order(
        order_status=False,
        order_date=datetime.datetime.now(),
        total_price=10.00,
        customer="Susie Sheep"
    )
    created_order = order_controller.create(db, order)

    detail = order_details_model.OrderDetail(
        order_id=created_order.order_id,
        amount=12
    )
    result = order_details_controller.create(db, detail)
    assert result.amount == 12


def test_create_review(db):
    order = order_model.Order(
        order_status=False,
        order_date=datetime.datetime.now(),
        total_price=15.00,
        customer="Peppa Pig"
    )
    created_order = order_controller.create(db, order)

    review = ratings_reviews_model.RatingsAndReviews(
        order_id=created_order.order_id,
        review_text="Awesome",
        review_score=5.0,
        customer_name="Peppa Pig"
    )
    result = ratings_reviews_controller.create(db, review)
    assert result.review_score == 5.0
    assert result.customer_name == "Peppa Pig"
