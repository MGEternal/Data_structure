def group_of_no_1(island_list, point_no):
    # ตรวจสอบว่า point_no อยู่ในช่วงของรายการ island_list
    if point_no < 0 or point_no >= len(island_list):
        return 0  # ถ้า point_no ไม่อยู่ในช่วงของรายการให้คืนค่า 0
    
    # ตรวจสอบว่าค่าที่ point_no คือ 1
    if island_list[point_no] != 1:
        return 0  # ถ้าค่าที่ point_no ไม่ใช่ 1 ให้คืนค่า 0
    
    # นับจำนวนตัวเลข 1 ที่ติดกัน
    count = 1  # เริ่มนับที่ตัวเลขที่ point_no
    
    # นับตัวเลข 1 ทางด้านซ้ายของ point_no
    left = point_no - 1
    while left >= 0 and island_list[left] == 1:
        count += 1
        left -= 1

    # นับตัวเลข 1 ทางด้านขวาของ point_no
    right = point_no + 1
    while right < len(island_list) and island_list[right] == 1:
        count += 1
        right += 1
    
    return count

# ตัวอย่างการใช้งาน
island_list = [0,1,0,1,0,1,0,1,0,1]
point_no1 = 7


result1 = group_of_no_1(island_list, point_no1)


print(f"{result1}")

