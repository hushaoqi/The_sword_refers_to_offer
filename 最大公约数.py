
n = int(input().strip())
array = list(map(int, input().strip().split()))
# print(n, array)

def Gcd(a, b):
    if 0 == b:
        return a
    else:
        return Gcd(b, a % b)
# 求出报名人数的最大公约数
def GcdN(digits: 'List[int]',length:'int'):
    if 1 == length:
        return digits[0]
    else:
        return Gcd(digits[length - 1], GcdN(digits, length - 1))

student_num = GcdN(array, n)  # 每个班级的人数
print(student_num)
class_num = 0
for num in array:
    class_num += num // student_num   # 班级总数
print(class_num)
