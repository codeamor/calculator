import os

operator = ["+", "-", "*", "/", "="]

def string_calculator(user_input, show_history=False):
    string_list = []
    lop = 0 # 마지막 연산자의 위치를 기억할 변수

    if user_input[-1] not in operator:
        user_input += "="

    # 10 뒤에 연산자가 없으니 for문이 돌지 않는다.
    for i, s in enumerate(user_input):
        if s in operator: # 현재 문자가 안에 있으면 / 연산자가 아닌 경우는 for문을 반복한다.
            if user_input[lop:i].strip() != "": # 첫 번째 연산자가 나오는 인덱스 3 / 0부터 3까지가 공백을 제외하고 아무 것도 없지 않으면
                string_list.append(user_input[lop:i]) # 0부터 3까지 잘라서 append 시킨다.
                string_list.append(s) # "+" 까지 append 시킨다.
                lop = i + 1 # i를 4로 만들고 for문을 돌린다.

    string_list = string_list[:-1]

    pos = 0
    while True:
        if pos + 1 > len(string_list): # len 이 1이면 탈출한다.
            break
        if len(string_list) > pos + 1 and string_list[pos] in operator:
            temp = string_list[pos-1] + string_list[pos] + string_list[pos+1]
            del string_list[0:3]
            string_list.insert(0, str(eval(temp)))
            pos = 0

            if show_history:
                print(string_list)
        pos += 1

    if len(string_list) > 0:
        result = float(string_list[0])

    return round(result, 4)

while True:
    user_input = input("계산식을 입력하세요> ")
    if user_input == "/exit":
        break
    result = string_calculator(user_input, show_history=True)
    print("결과: {}".format(result))