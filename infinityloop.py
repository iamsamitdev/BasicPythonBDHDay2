import time
num = 0
round = 1

while True:
    if round <= 20:
        if num == 0:
            print(num, "OFF")
            num = 1
        elif num == 1:
            print(num, "ON")
            num = 0
        # ครบ 1 รอบ หยุด 1 วินาที
        time.sleep(1)
    else:
        break
    round = round + 1