# Chapter1_list_0411.py
#리스트, 튜플, 딕셔너리, 집합
#김, 이, 박, 최,

#리스트
['김', '이', '박', '최']

#튜플
('김', '이', '박', '최')

#딕셔너리 -> 사전 {key:value, k1:v1, k2:v2,.....}
address = {'홍길동':'서울', '김길동':'부천', 'james':'미국'}
print(address['홍길동'])

#List
lst = [10, 12, 20, 45, 66] #[]안의 값 int,float string 모두 가능
str_list = ['하','호'] 
print(type(lst))
print(lst[0], " ", lst[1], " ", lst[len(lst)-2]) 
#lst[len(lst)-2]에서 66을 나오게 하고싶으면 "-1"

#빈 리스트 생성 -> 하나씩 원소를 추가
#빈리스트 예 1번 
list1 = []
#빈리스트 예 2번
list2 = list()

list1.append("Python")
list1.append("Java")
list1.append("Python")
list1.append("C++")
list1.append("Python")
list1.append("Python")

print(list1)
print(list1[0])
# list1이랑 같은 값이 나옴 ,list2 = ['Java', 'C++']

print("======for 1======")
for i in range(len(list1)):
    print(list1[i])

print("======for 2======")
for i in list1:
    print(i)

print(list1)
print("count : ", list1.count("Python"))
print("index : ", list1.index("Python"))
#"hahah".index("a") 

list1[0] = "AI"
list1[2] = "IoT"
print(list1) 

list1[0:3:1] #0부터 3개값을 1칸씩

print("==================================================")
list2 = list1[0:3:1] #['AI', 'Java', 'IoT']
print(list2)
list2 = list1[1:5:1] #['Java', 'IoT', 'C++', 'Python']
print(list2)
list2 = list1[1:len(list1):2] #['Java', 'C++', 'Python']
print(list2)
list2 = list1[2:6:3] #['IoT', 'Python']
print(list2)
list2 = list1[::-1] #['Python', 'Python', 'C++', 'IoT', 'Java', 'AI']
print(list2)

#수정 불가 -> append, insert, 값 변경 X
#[1,2,3,4]
#(1,2,3,4) t1+t2 => t3
#t1 +1 => t1

#print(list3)
#list1, list3
#list1의 일부를 list3에 대입

list2 = list1[2:6:3] #list2['IoT', 'Python']
print(list2)

list3 = [1,2,3,4,5,6,7,8]
list3[1:2] = list2
print(list3)


#list insert
menu = []
menu.append("짜장면")
menu.append("써브웨이")
menu.append("떡볶이")
print(menu)
menu.insert(0,"파스타")
print(menu)
menu.insert(2,"볶음밥")
print(menu)

menu.remove("써브웨이")
print(menu)

'''
print("menu.pop : " , menu.pop())
print(menu)
print("menu.pop : " , menu.pop())
print(menu)
print("menu.pop : " , menu.pop())
print(menu)
'''

#extend #추가
print("==========================================================================")
print(menu)
dessert = ["커피", "아이스크림", "케이크", "와플"]

menu_list = menu + dessert
print(menu_list)

menu.extend(dessert) #menu+dessert
print(menu)

#reverse #순서를 거꾸로 함
print("==========================================================================")
print(menu)
menu.reverse()
print(menu)

#menu.sort #a,b,c,d순으로 변경
print("==========================================================================")
l1 = [ "banana", "apple", "orange" , "mango"]
print(l1)
print("sorted(l1) : ", sorted(l1))
print("l1         : ", l1)

l1.sort()
print(l1)

#menu.clear()
#del menu
#print(menu)

#a = '1'
#print(type(a))
#print(int(a) + 5)
#print(type(a))