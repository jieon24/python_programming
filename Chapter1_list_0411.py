# 0411.py
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
list1.append("C++")
print(list1)
print(list1[0])
# list1이랑 같은 값이 나옴 ,list2 = ['Java', 'C++']

print("======for 1======")
for i in range(len(list1)):
    print(list1[i])

print("======for 2======")
for i in list1:
    print(i)
  