from . import orders, order_details, recipes, sandwiches, resources, promotions

from ..dependencies.database import engine


def index():
    order_details.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)
    orders.Base.metadata.create_all(engine)

