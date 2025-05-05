import pytest
from api.controllers.resource_managements import create, read_all, read_one, update, delete
from api.schemas.resource_managements import ResourceManagementCreate, ResourceManagementUpdate
from api.models.resource_managements import ResourceManagement
from fastapi import status
from fastapi.responses import Response

@pytest.fixture
def db_session(mocker):
    return mocker.Mock()

def test_create_resource_management(db_session):
    data = {
        "items": "Bread",
        "amount": 100,
        "resource_management_id": 1
    }
    schema = ResourceManagementCreate(**data)
    created = create(db_session, schema)

    assert created is not None
    assert created.items == "Bread"
    assert created.amount == 100
    assert created.resource_management_id == 1

def test_read_all_resource_managements(db_session):
    result = read_all(db_session)

    assert result is not None

def test_read_one_resource_management(db_session):
    mock_item = ResourceManagement(
        items="Bread",
        amount=100,
        resource_management_id=1
    )
    db_session.query.return_value.filter.return_value.first.return_value = mock_item
    result = read_one(db_session, 1)

    assert result is not None
    assert result.items == "Bread"
    assert result.amount == 100
    assert result.resource_management_id == 1

def test_update_resource_management(db_session):
    existing = ResourceManagement(
        items="Bread",
        amount=100,
        resource_management_id=1
    )

    db_session.query.return_value.filter.return_value.first.return_value = existing

    update_data = ResourceManagementUpdate(
        items="Ham",
        amount=200,
        resource_management_id=1
    )

    result = update(db_session, 1, update_data)

    assert result is not None
    assert existing.items == "Ham"
    assert existing.amount == 200
    assert existing.resource_management_id == 1

def test_delete_resource_management(db_session):
    db_session.query.return_value.filter.return_value.first.return_value = ResourceManagement(
        items="Bread",
        amount=100,
        resource_management_id=1
    )

    response = delete(db_session, 1)
    assert isinstance(response, Response)
    assert response.status_code == status.HTTP_204_NO_CONTENT
