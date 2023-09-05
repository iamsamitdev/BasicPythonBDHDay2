import pymysql

# สร้างฟังก์ชันสำหรับเชื่อมต่อฐานข้อมูล
def connectdb():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        db='pythondatabase',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

# ทดสอบเรียกใช้งานฟังก์ชัน
# print(connectdb())