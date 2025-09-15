import pymysql

def create_customer(connection, customer_data: dict) -> int:
    """
    New client in oc_customer table.
    return customer_id of new client.
    """
    cursor = connection.cursor()

    sql = """
        INSERT INTO oc_customer (
            customer_group_id, 
            store_id, 
            language_id, 
            firstname, 
            lastname, 
            email, 
            telephone, 
            password,
            newsletter, 
            address_id, 
            custom_field, 
            ip, 
            status, 
            safe, 
            token, 
            code, 
            date_added
        ) VALUES (
            %(customer_group_id)s, 
            %(store_id)s, 
            %(language_id)s, 
            %(firstname)s, 
            %(lastname)s, 
            %(email)s, 
            %(telephone)s,  
            '',
            0, 
            0, 
            '', 
            '127.0.0.1', 
            1, 
            0, 
            '', 
            '', 
            NOW()
        )
    """

    cursor.execute(sql, customer_data)
    customer_id = cursor.lastrowid
    cursor.close()
    return customer_id


def get_customer_by_id(connection, customer_id: int) -> dict:
    """
    Get client data by ID.
    Return data dictionary or None, if client is  not found  .
    """
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    sql = "SELECT * FROM oc_customer WHERE customer_id = %s"
    cursor.execute(sql, (customer_id,))
    customer = cursor.fetchone()
    cursor.close()
    return customer


def update_customer(connection, customer_id: int, update_data: dict) -> bool:
    """
    Update  client data by ID.
    return True, if updated at least 1 field, otherwise False.
    """
    cursor = connection.cursor()

    sql = """
        UPDATE oc_customer 
        SET firstname = %(firstname)s, 
            lastname = %(lastname)s, 
            email = %(email)s, 
            telephone = %(telephone)s 
        WHERE customer_id = %(customer_id)s
    """

    params = update_data.copy()
    params['customer_id'] = customer_id

    cursor.execute(sql, params)
    updated_rows = cursor.rowcount
    cursor.close()
    return updated_rows > 0


def delete_customer(connection, customer_id: int) -> bool:
    """
    delete client by ID.
    Returns True if at least 1 client was removed, otherwise False..
    """
    cursor = connection.cursor()

    sql = "DELETE FROM oc_customer WHERE customer_id = %s"
    cursor.execute(sql, (customer_id,))
    deleted_rows = cursor.rowcount
    cursor.close()
    return deleted_rows > 0