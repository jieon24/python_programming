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

#0~10까지의 숫자 제곱을 원소로 가지는 리스트 작성 
#And 짝수의 제곱만 
l1 = [] 
for i in range(10) :
    if (i % 2 == 0) :
        l1.append(i**2)
print(l1)

'''
방법2.
li = [i**2 for i in range(10) if i % 2 == 0]
print(l1)
'''

#shallow copy
food = ["apple","banana"]
wishlist = food
print("food :          ", food)
print("wishlist :      ", wishlist)

food.pop()
print("after food.pop()")
print("food :          ", food)
print("wishlist :      ", wishlist)

print(food is wishlist)

#deep copy
food2 = food[:]
food3 = list(food)


print("deep copy")
print("food :           ", food)
print("food2 :          ", food2)
print(food is food2)

food2.append("gimbab")
print("food :           ", food)
print("food2 :          ", food2)

food2.append("bibimbab")
print("food :           ", food)
print("wishlist :      ", wishlist)
print("food2 :          ", food2)
