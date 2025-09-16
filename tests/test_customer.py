import pytest
from lib.db import create_customer, get_customer_by_id, update_customer, delete_customer


@pytest.fixture
def sample_customer_data():
    return {
        "customer_group_id": 1,
        "store_id": 0,
        "language_id": 1,
        "firstname": "John",
        "lastname": "Doe",
        "email": "john.doe@example.com",
        "telephone": "+1234567890",
    }


def test_create_customer(connection, sample_customer_data):
    # Создаём клиента
    customer_id = create_customer(connection, sample_customer_data)

    # Проверяем, что клиент появился в БД
    customer = get_customer_by_id(connection, customer_id)
    assert customer is not None, "Customer not found after creation"
    assert customer["firstname"] == sample_customer_data["firstname"]
    assert customer["lastname"] == sample_customer_data["lastname"]
    assert customer["email"] == sample_customer_data["email"]
    assert customer["telephone"] == sample_customer_data["telephone"]


def test_update_customer(connection, sample_customer_data):
    # Создаём клиента
    customer_id = create_customer(connection, sample_customer_data)

    # Подготавливаем новые данные
    updated_data = {
        "firstname": "Jane",
        "lastname": "Smith",
        "email": "jane.smith@example.com",
        "telephone": "+0987654321",
    }

    # Обновляем клиента
    result = update_customer(connection, customer_id, updated_data)
    assert result is True, "Customer was not updated"

    # Проверяем обновлённые данные
    customer = get_customer_by_id(connection, customer_id)
    assert customer["firstname"] == updated_data["firstname"]
    assert customer["lastname"] == updated_data["lastname"]
    assert customer["email"] == updated_data["email"]
    assert customer["telephone"] == updated_data["telephone"]


def test_update_nonexistent_customer(connection):
    # Пытаемся обновить несуществующего клиента
    updated_data = {
        "firstname": "Ghost",
        "lastname": "User",
        "email": "ghost@example.com",
        "telephone": "0000000000",
    }

    result = update_customer(connection, 999999999, updated_data)
    assert result is False, "Update should fail for nonexistent customer"


def test_delete_customer(connection, sample_customer_data):
    # Создаём клиента
    customer_id = create_customer(connection, sample_customer_data)

    # Удаляем клиента
    result = delete_customer(connection, customer_id)
    assert result is True, "Customer was not deleted"

    # Проверяем, что клиент удалён
    customer = get_customer_by_id(connection, customer_id)
    assert customer is None, "Customer still exists after deletion"


def test_delete_nonexistent_customer(connection):
    # Пытаемся удалить несуществующего клиента
    result = delete_customer(connection, 999999999)
    assert result is False, "Deletion should fail for nonexistent customer"