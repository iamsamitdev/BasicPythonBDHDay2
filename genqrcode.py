import qrcode
# import time
# import calendar
from datetime import datetime

print("QR Code Generator Program")
print("Please type 'quit' to exit")

while True:
    data = input("Please enter your qrcode data: ")
    if data == 'quit':
        break
    else:
        img = qrcode.make(f'{data}')
        type(img)
        # img.save(f'qrcodeimg/{calendar.timegm(time.gmtime())}.png')
        img.save(f"qrcodeimg/{datetime.today().strftime('%Y%m%d%H%M%S')}.png")
        print("QR Code Generated Successfully")