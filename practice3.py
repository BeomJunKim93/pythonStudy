# if 5 in [1,2,3,4]:
#     print("4가 있습니다")
# else:
#     print("아무것도 없음")
#
#
# a = 1
# b = 3
# a+b
# print(a+b)
#
# for a in [1,2,3]:
#     print(a)
#
# i = 0
# while i<3:
#     print(i)
#     i = i+1
#     print(i)
#
# def add(a,b):
#     return a+b
#
# fu = add(3,4)
# print(fu)


def rho(T):
    a = 101325/(287.058*(T+273.15))
    return a

te = rho(25)
print(te)