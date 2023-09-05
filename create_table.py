import pymysql
from module import connectmysql as con

# สร้างฟังก์ชันสำหรับสร้างตารางใหม่
def createtable():
    connection = con.connectdb()
    cursor = connection.cursor()

    # SQL สำหรับสร้างตารางใหม่
    sql = """
        CREATE TABLE person(
            id int PRIMARY KEY AUTO_INCREMENT,
            fullname varchar(128),
            email varchar(64),
            age int
        )
    """

    try:
        cursor.execute(sql)
        connection.commit()
        print("Create table person success")
    except pymysql.error:
        print(pymsql.error)

# เรียกใช้งานฟังก์ชัน
createtable()