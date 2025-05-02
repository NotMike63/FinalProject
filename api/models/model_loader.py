from . import orders, PaymentInformation, order_details, promotions, resource_managements, customer, menu_item, RatingsAndReviews

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    PaymentInformation.Base.metadata.create_all(engine)
    RatingsAndReviews.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)
    resource_managements.Base.metadata.create_all(engine)
    customer.Base.metadata.create_all(engine)
    menu_item.Base.metadata.create_all(engine)