import pymysql
from module import connectmysql as con
from tabulate import tabulate

# สร้างฟังก์ชันสำหรับอ่านข้อมูลจากตาราง person
def readperson():
    connection = con.connectdb()
    cursor = connection.cursor()

    # SQL สำหรับอ่านจากตาราง person
    sql = """
        SELECT * FROM person
    """

    try:
        cursor.execute(sql)
        connection.commit()
        
        # ดึงข้อมูลทั้งหมด
        print(tabulate(cursor))

    except pymysql.error:
        print(pymsql.error)

# เรียกใช้งานฟังก์ชัน
readperson()