# 비만도 계산기

level = ["저체중", "정상", "과체중", "경도비만", "중증도 비만", "고도 비만"]

height = (float)(input("키를 입력하세요.(m): "))
weight = (float)(input("몸무게를 입력하세요.(kg): "))

BMI = abs(weight / (height ** 2))

if BMI < 18.5:
    level = level[0]
elif BMI < 23:
    level = level[1]
elif BMI < 25:
    level = level[2]
elif BMI < 30:
    level = level[3]
elif BMI < 35:
    level = level[4]
else:
    level = level[5]

print("당신의 체질량 지수는 {0}이고 {1} 입니다. ".format(round(BMI, 2) ,level))