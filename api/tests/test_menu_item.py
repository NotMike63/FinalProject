import pytest
from api.controllers.menu_item import create_menu_item, get_all_menu_items, get_menu_item_by_id, update_menu_item, delete_menu_item
from api.schemas.menu_item import MenuItemCreate, MenuItemUpdate
from api.models.menu_item import MenuItem

@pytest.fixture
def db_session(mocker):
    return mocker.Mock()

def test_create_menu_item(db_session):
    data = {
        "name": "Burger",
        "price": 5.55,
        "calories": 550,
        "category": "Test"
    }
    schema = MenuItemCreate(**data)
    created = create_menu_item(db_session, schema)

    assert created is not None
    assert created.name == "Burger"
    assert created.price == 5.55
    assert created.calories == 550
    assert created.category == "Test"

def test_get_all_menu_items(db_session):
    db_session.query.return_value.all.return_value = []
    items = get_all_menu_items(db_session)

    assert items is not None

def test_get_menu_item_by_id(db_session):
    item = MenuItem(**{
        "name": "Test Item",
        "price": 1.23,
        "calories": 123,
        "category": "Test"
    })
    db_session.query.return_value.get.return_value = item

    result = get_menu_item_by_id(db_session, 1)
    assert result is not None
    assert result.name == "Test Item"
    assert result.price == 1.23
    assert result.calories == 123
    assert result.category == "Test"

def test_delete_menu_item(db_session):
    db_session.query.return_value.filter.return_value.first.return_value = None

