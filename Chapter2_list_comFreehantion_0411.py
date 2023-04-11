# Chapter2_listcomFreehantion_0411.py

#리스트컴프리헨션

#1번
list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1)

#2번
list1 = []
for i in range(11) :
    list1.append(i)
print(list1)

#3번 
#리스트 변수명 = [i for i in range()]
list1 = [i for i in range(11)] #[0,1,2,3,.....10]
print(list1)

#0~10까지의 숫자 제곱을 원소로 가지는 리스트 작성 
#i**2 제곱
#[0,1,4,9,16,.......64,81,100]
list1 = [i**2 for i in range(11)] #[0,1,2,3,.....10]
print(list1)

#0~10까지의 숫자의 3배를 원소로 가지는 리스트 작성
#i*3 곱하기
list1 = [i*3 for i in range(11)] #[0,1,2,3,.....10]
print(list1)

#hello를 10가 가지는 리스트 작성
list1 = ["hello" for i in range(10)] #[0,1,2,3,.....10]
print(list1)