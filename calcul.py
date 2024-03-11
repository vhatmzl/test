# 계산기 함수


#신혁님

#지안님
# 빼기 계산기 subtraction
def subtraction():
    숫자1 = float(input("첫 번째 숫자를 입력하세요: "))
    연산자 = input("연산자를 입력하세요 (-): ")
    숫자2 = float(input("두 번째 숫자를 입력하세요: "))

    if 연산자 == '-':
        결과 = 숫자1 - 숫자2
    else:
        print("올바른 연산자를 입력해주세요.")
        return

    print("결과:", 결과)

subtraction()



#태성님