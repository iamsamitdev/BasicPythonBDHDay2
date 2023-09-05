# การสร้างฟังก์ชันแบบไม่มีการรับค่า
def hello():
    print("Hello Python")


# เรียกใช้งานฟังก์ชัน
hello()


# การสร้างฟังก์ชันแบบมีการรับค่า
def area(width=0, height=0):
    total = width * height
    print("Area is ", total)


# เรียกใช้งานฟังก์ชัน
area(5, 3)
area()
