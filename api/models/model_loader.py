from . import orders, PaymentInformation, recipes, resources, order_details

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    PaymentInformation.Base.metadata.create_all(engine)
