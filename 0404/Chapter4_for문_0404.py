# Chapter4_0404.py

#반복문
#for문

'''for i in 1,3,4,6,8 :
    print(i)

for i in range(0,101,1) : #1~100까지 1칸씩
    print(i)    
'''

#같은 값 다른 방법
'''print("range1")
for i in range(0,11,1) :
    print(i)

print("range2")
for i in range(11) :
    print(i)
'''

#1부터 10까지의 합
sum = 0
for i in range(11) :
    sum = sum + i
    print(i,"번째 sum은 ", sum)
else : 
    print("for문의 조건이 더이상 만족하지 않습니다.")
    print("i가 range(11)에서 벗어남. ")
    print("for문이 break니 continue로 종료된게 아니라 정상 종료시에만 실행")

print("sum : ",sum)