import pymysql
from module import connectmysql as con

# สร้างฟังก์ชันสำหรับแก้ไขข้อมูลในตาราง person
def editperson():
    connection = con.connectdb()
    cursor = connection.cursor()

    # SQL สำหรับแก้ไขข้อมูลในตาราง person
    sql = """
        UPDATE person SET fullname='Somsri', email='somsri@email.com' 
        WHERE id='3'
    """

    try:
        cursor.execute(sql)
        connection.commit()
        print("Edit person success")
    except pymysql.error:
        print(pymsql.error)

# เรียกใช้งานฟังก์ชัน
editperson()