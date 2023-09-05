import pymysql
from module import connectmysql as con

# สร้างฟังก์ชันสำหรับลบข้อมูลในตาราง person
def deleteperson():
    connection = con.connectdb()
    cursor = connection.cursor()

    # SQL สำหรับลบข้อมูลในตาราง person
    sql = """
        DELETE FROM person WHERE id='3'
    """

    try:
        cursor.execute(sql)
        connection.commit()
        print("Delete person success")
    except pymysql.error:
        print(pymsql.error)

# เรียกใช้งานฟังก์ชัน
deleteperson()