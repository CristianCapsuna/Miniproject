import pymysql
import os
from dotenv import load_dotenv
from pymysql.err import Error, OperationalError
from typing import List

# Load environment variables from .env file
load_dotenv()
host_name = os.environ.get("mysql_host")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")
db_name = os.environ.get("mysql_db")

def create_connection():

    # Establish a database connection
    try:
        connection = pymysql.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        db = db_name
        )
    except OperationalError as e:
        if e.args[0] != 1049:
            print(e)
            exit()
        # general connection
        connection = pymysql.connect(
            host = host_name,
            user = user_name,
            password = user_password
            )
        #create database
        create_database = "CREATE DATABASE " + db_name
        execute_query(create_database, connection)
        #create initial connection
        connection = pymysql.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        db = db_name
        )
        #create database structure
        create_products_table = "CREATE TABLE products("\
                                "product_id INT NOT NULL AUTO_INCREMENT,"\
                                "name VARCHAR(100) NOT NULL,"\
                                "price DECIMAL(5,2) NOT NULL,"\
                                "PRIMARY KEY(product_id)"\
                                ");"
        execute_query(create_products_table, connection)

        create_couriers_table = "CREATE TABLE couriers("\
                                "courier_id INT NOT NULL AUTO_INCREMENT,"\
                                "name VARCHAR(100) NOT NULL,"\
                                "phone VARCHAR(15) NOT NULL,"\
                                "PRIMARY KEY(courier_id)"\
                                ");"
        execute_query(create_couriers_table, connection)

        create_orders_table = "CREATE TABLE orders("\
                                "order_id INT NOT NULL AUTO_INCREMENT,"\
                                "customer_name VARCHAR(100) NOT NULL,"\
                                "customer_address VARCHAR(100) NOT NULL,"\
                                "customer_phone VARCHAR(15) NOT NULL,"\
                                "courier INT NOT NULL,"\
                                "status VARCHAR(50) NOT NULL,"\
                                "PRIMARY KEY(order_id),"\
                                "FOREIGN KEY(courier) REFERENCES Couriers(courier_id)"\
                                ");"        
        execute_query(create_orders_table, connection)

        mapping_table_for_orders_and_product = "CREATE TABLE orders_map("\
                                "order_id INT NOT NULL,"\
                                "product_id INT NOT NULL,"\
                                "FOREIGN KEY(order_id) REFERENCES Orders(order_id),"\
                                "FOREIGN KEY(product_id) REFERENCES Products(product_id)"\
                                ");"        
        execute_query(mapping_table_for_orders_and_product, connection)

    return connection

def execute_query(query, connection = None):
    flag = 0
    # Establish the connection
    if connection == None:
        connection = create_connection()
        flat = 1

    # A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
    cursor = connection.cursor()
    
    # Execute query
    cursor.execute(query)

    # Commit query
    connection.commit()

    # Close cursor
    cursor.close()

    # Close connection
    if flag == 1:
        connection.close()

def write_products(content: List):
    pass

def get_all_content( table_name: str ):
    connection = create_connection()

    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM {table_name}")
        sql_content = cursor.fetchall()
        cursor.execute(f"SHOW COLUMNS FROM {table_name};")
        column_names_initial = cursor.fetchall()
        column_names = []
        for idx in range( len( column_names_initial) ):
            column_names.append(column_names_initial[idx][0])
        content = []
        for line in sql_content:
            data_dict = {}
            for idx in range(len(line)):
                key = column_names[idx]
                value = line[idx]
                data_dict[key] = value
            content.append(data_dict)
    
    return content

def clear_table_and_reset_index( table_name: str ):
    execute_query(f"DELETE FROM {table_name}")
    execute_query(f"ALTER TABLE {table_name} AUTO_INCREMENT = 1")

def get_index_of_last_entry( table_name: str ):
    connection = create_connection()

    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM {table_name} ORDER BY {table_name[:-1] + '_id'} DESC LIMIT 1")
        index_of_last = cursor.fetchall()[0][0]
    
    return index_of_last