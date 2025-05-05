import pytest
from api.controllers.RatingsAndReviews import create, read_all, read_one, update, delete
from api.schemas.RatingsAndReviews import RatingsAndReviews, RatingsAndReviewsUpdate
from api.models.RatingsAndReviews import RatingsAndReviews as RatingsAndReviewsModel
from api.models.orders import Order
from fastapi.responses import Response
from fastapi import status


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_ratings_and_reviews(db_session):

    data = RatingsAndReviews(
        order_id=1,
        review_text="Amazing service!",
        review_score=4.5,
        customer_name="John Doe"
    )

    created = create(db_session, data)

    assert created is not None
    assert created.order_id == 1
    assert created.review_text == "Amazing service!"
    assert created.review_score == 4.5
    assert created.customer_name == "John Doe"


def test_read_all_ratings_and_reviews(db_session):
    result = read_all(db_session)

    assert result is not None


def test_read_one_ratings_and_reviews(db_session):
    review = RatingsAndReviews(
        order_id=1,
        review_text="Great experience!",
        review_score=5.0,
        customer_name="Jane Doe"
    )
    db_session.query.return_value.filter.return_value.first.return_value = review

    result = read_one(db_session, 1)
    assert result is not None
    assert result.order_id == 1
    assert result.review_score == 5.0


def test_update_ratings_and_reviews(db_session):
    existing = RatingsAndReviews(
        order_id=1,
        review_text="Absolute Donkey. An idiot Sandwich!",
        review_score=1.0,
        customer_name="Gordon Ramsey"
    )

    review_mock = db_session.query.return_value.filter.return_value
    review_mock.first.return_value = existing

    update_data = RatingsAndReviewsUpdate(
        review_text="Much better now. Thank Heavens!",
        review_score=4.0
    )

    result = update(db_session, 1, update_data)

    assert result is not None
    assert existing.review_text == "Much better now. Thank Heavens!"
    assert existing.review_score == 4.0


def test_delete_ratings_and_reviews(db_session):
    db_session.query.return_value.filter.return_value.first.return_value = RatingsAndReviews(
        order_id=1,
        review_text="Terrible",
        review_score=1.0,
        customer_name="Karen"
    )

    result = delete(db_session, 1)

    assert result is not None
    assert result.status_code == status.HTTP_204_NO_CONTENT
