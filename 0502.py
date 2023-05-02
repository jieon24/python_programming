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

#지역변수, 전역변수
num = 100 #전역 변수 global variable
print("***num : ", num)

def addone() :
    num = 10
    print("addone()", num + 1)
    print("addone() num", num)
    num = num * 8  + 20
    return num

addone()
print("***num : ", num)

#변수를 수정하지 않으면 내부 function에서도 전역변수 사용 가능
num = 100 #전역 변수 global variable
print("***num : ", num)

def addone() :
    #내부 function 에서 num을 수정하지 않는다
    #print("addone()", num + 1)
    #print("addone() num", num)
    #num = num * 8  + 20
    return num

addone()
print("***num : ", num)

#내부 function에서 전역변수를 사용, 
# 수정도 사용,function이 끝나도 그 값이 반영이 되면 좋겠음
num = 100 #전역 변수 global variable
print("***num : ", num)

def addone() :
    global num 
    num = num + 1 #전역변수를 쓰겠다. 변수에 새로운 값 대입가능

addone()
print("***num : ", num)

#인자의 갯수가 여러개인 경우
print()
print(1,2,3,6,8,9,...,16)

print("=================================")
def hello2(*names) : #hello2 찍기
    for i in names:
        print("hello",i)

hello2("James", "Tom", "Pane", "Jennie")

#합을 구하는 function
print("=================================")
def sum22(*numbers) :
    result2 = 0
    for num in numbers:
        result2 = result2 +num
    return result2

print("합은 :",sum22(1,2,1,2,1,2,4,6,4,3,74,9))
lis1 = [1,2,1,2,1,2,4,6,4,3,74,9]
print(sum22(*lis1))

#dictionary = {key:vlaue1, key2:vlaue2}
print("=================================")
coffee = {"americano":3300, "latte    ":3800, "tea      ":2500}

def printmenu(**keyvalue) :
    for key in keyvalue :
        print(key, keyvalue[key])

printmenu(**coffee)
print("=================================")
printmenu(americano=3300, latte=3800, tea=2500, hotdog=3500, sandwich=4500)

print("=================================")
def fun1(*num, **menu) :
    result = 0
    for n in num:
        result = result + n
    return result

    for key in menu :
        print(key, menu[key])

coffee = {"americano":3300, "latte    ":3800, "tea      ":2500}
fun1(1,2,4,6,8,2,3,4,3,21,2,2,1,1,1,americano=3300, latte=3800, tea=2500)
fun1(*lis1, **coffee)
print(fun1(1,2,4,6,8,2,3,4,3,21,2,2,1,1,1,**coffee))