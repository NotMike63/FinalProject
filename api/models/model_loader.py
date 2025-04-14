from . import orders, PaymentInformation, order_details, RatingsAndReviews, promotions

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    PaymentInformation.Base.metadata.create_all(engine)
    RatingsAndReviews.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)