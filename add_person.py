import pymysql
from module import connectmysql as con

# สร้างฟังก์ชันสำหรับเพิ่มข้อมูลลงในตาราง person
def addperson():
    connection = con.connectdb()
    cursor = connection.cursor()

    # SQL สำหรับสร้างตารางใหม่
    sql = """
        INSERT INTO person(fullname, email, age) 
        VALUES('Somkid','somkid@email.com','30')
    """

    try:
        cursor.execute(sql)
        connection.commit()
        print("Add person success")
    except pymysql.error:
        print(pymsql.error)

# เรียกใช้งานฟังก์ชัน
addperson()