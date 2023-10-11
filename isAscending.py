def isAscending(list_of_integer):
    # Base case: ถ้ารายการมีหน้าไม่เกิน 1 ตัวหรือเป็นรายการว่าง จะถือว่าเรียงลำดับแล้ว
    if len(list_of_integer) <= 1:
        return True

    # ตรวจสอบว่าตัวแรกมากกว่าหรือเท่ากับตัวถัดไป
    if list_of_integer[0] > list_of_integer[1]:
        return False

    # ลดขนาดของรายการแล้วเรียกฟังก์ชันตัวเอง
    return isAscending(list_of_integer[1:])

# ตัวอย่างการใช้งาน
list_of_integer1 = [6,7,8,9,10,11,12]
list_of_integer2 = [6,3,8,7,9,2,3,1,5]

if isAscending(list_of_integer1):
    print("รายการ 1 เรียงลำดับจากน้อยไปหามาก")
else:
    print("รายการ 1 ไม่เรียงลำดับจากน้อยไปหามาก")

if isAscending(list_of_integer2):
    print("รายการ 2 เรียงลำดับจากน้อยไปหามาก")
else:
    print("รายการ 2 ไม่เรียงลำดับจากน้อยไปหามาก")
