import random
from datetime import datetime


def generate_student_id():
    # 获取当前年份作为4位数字
    current_year = datetime.now().year

    # 生成8位随机数字，确保首位不为0
    first_digit = random.randint(1, 9)  # 第一位1-9
    other_digits = [str(random.randint(0, 9)) for _ in range(7)]  # 后7位0-9
    random_part = str(first_digit) + ''.join(other_digits)

    # 组合年份和随机部分
    student_id = f"{current_year}{random_part}"

    return student_id


# # 示例：生成10个学号
# for _ in range(10):
#     print(generate_student_id())