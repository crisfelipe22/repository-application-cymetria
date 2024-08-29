import pymysql

db_host = "$INSTANCIA_AWS"
db_user = "$USER"
db_password = "$PASSWORD"
db_database = "$NAME_DATABASE"

def conection_database():
    try:
        conection_sql = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_database,
        )
        print("Successfull satisfactory to database")
        return conection_sql
    except Exception as err:
        print("Error try contening to database", err)
        return None

def insert_register_database(id, name, lastname, birthday):
    insert_sql = f"""INSERT INTO users (id, name, lastname, birthday) VALUES ({id}, "{name}", "{lastname}", "{birthday}")"""
    print(insert_sql)
    conection_sql = conection_database()
    cursor = conection_sql.cursor()
    try:
        cursor.execute(insert_sql)
        conection_sql.commit()
        print("Insert to data")
    except Exception as err:
        print("Error inser to data", err)


def consult_user(ident):
    instruction = "SELECT * FROM users WHERE id =" + ident
    connection = conection_database()
    cursor = connection.cursor()
    try:
        cursor.execute(instruction)
        result_data = cursor.fetchall()
        return result_data
    except Exception as err:
        print("Error consulting the user", err)
        return False