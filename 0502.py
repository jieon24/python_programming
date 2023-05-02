# 0502.py
#함수 input을 주면 output이 나오는것.

'''
input - 숫자 - num1
output = 숫자 - output_num
이런 기능을 하는 function - multi
'''

#함수 정의
#3을 곱하는 함수
def multi(num1) :
    output_num = num1 * 3
    print("여기는 multi 함수 안입니다.")
    return output_num

#정의한 함수 호출
print(multi(10)) #결과 return값 30

print("=================================")
# function - hello
# parameter, input - 사람이름 두개 입력
#            output - 안녕 1번사람, 안녕 2번사람

def hello(p1, p2) :
#def hello(p1="김", p2="이") : 직접 지정도 가능 -기본값
    print("안녕, ", p1)
    print("안녕, ", p2)
    
hello("홍길동","김길동") # -사용자값

print("=================================")
#두개의 숫자를 입력받아, 두개의 합을 함수 내에서 출력하시오.

def mysum(num1, num2) :
    print("두 수의 합은 : ", num1 + num2)
    
mysum(100,1000)

def mysum2(num1, num2) :
    return(num1 + num2)

result = mysum2(100,2000)
print(result)