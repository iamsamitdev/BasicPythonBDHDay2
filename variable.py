# สร้างตัวแปรเก็บข้อมูลชนิดต่างๆ
a = 10
b = 3.14
c = "Hello"

# แสดงผลลัพธ์
print(a)
print(b)
print(c)

# แสดงชนิดข้อมูล
print(type(a))
print(type(b))
print(type(c))

# การสร้างตัวแปรแบบพิเศษ
# สร้างตัวแปรเก็บค่าเดียว
x = y = z = 10

# สร้างตัวแปรเก็บค่าหลายค่า
j,k,l = 10, 20, 30

# แสดงผลลัพธ์
print(x, y, z)
print(j, k, l)

# ตัวแปรแบบ boolean
status = True
msg = False

# แสดงผลลัพธ์
print(status)
print(msg)

print(status==1)
print(msg==0)

# การแสดงผลตัวแปรร่วมกับข้อความ
price = 200.50
qty = 5

# แบบที่ 1
print("ราคาสินค้า", "{:.2f}".format(price), "บาท จำนวน", qty, "ชิ้น")

# แบบที่ 2
print("ราคาสินค้า %.2f บาท จำนวน %d ชิ้น" % (price,qty))

# แบบที่ 3
print(f"ราคาสินค้า {price:.2f} บาท จำนวน {qty} ชิ้น")