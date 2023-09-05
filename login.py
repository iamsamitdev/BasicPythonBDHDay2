print("Login System")

# รับค่าจากผู้ใช้งาน
username = input("Username:")
password = input("Password:")
# print(username)
# print(password)

# ตรวจสอบการ Login
if username == "admin" and password == "1234":
    print("Login Success")
else:
    print("Login Fail")