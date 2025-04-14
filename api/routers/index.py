from . import orders, order_details, PaymentInformation, promotions, RatingsAndReviews, customer, menu_item


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(PaymentInformation.router)
    app.include_router(promotions.router)
    app.include_router(RatingsAndReviews.router)
    app.include_router(customer.router)
    app.include_router(menu_item.router)
