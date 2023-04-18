# Chapter5_tuple_0418.py

#수정이 불가한 항목들, 튜플
t1  = (1,2,3,4)
print(t1)

t2 = tuple()
print(t2)

t3 = 1,2,4,5,4,5,8,10,3
print(type(t3))
print(t3.index(3))
print(t3.count(3))

t4 = 1,2,3,3,5,6,7,8,10,3
t5 = 100,200,300
print("t4+t5 : ", t4+t5)
print("t4 : ", t4)
print("t5 : ", t5)

sorted(t4) #원본 안바뀜
print(sorted(t4))
print("t4 : ", t4)

#Lst.sort() 원본이 바뀜

#dictionary
#key:value
#1001:"홍길동", 1002:"김길동"
d1 = {1001:"홍길동", 1002:"김길동", 1003:"김지언"}
print(d1[1001])

#print(d1[key])
#d2={}
#강좌에 대한 dictionary
d2 = dict()
d2['class'] = 'Python'
d2['date'] = 'Thu'
d2['year'] = 2003
d2['name'] = ['Kim','Park','Lee']
print("d2 : ", d2)
#print(d2['student'])
print(len(d2))

#dictionary key:value 1:1월 2:2월 ~ 12:12월
#for문을 사용하여 각각의 value값을 찍어라.
Month = dict()
Month = {1:'1월', 2:'2월', 3:'3월', 4:'4월', 5:'5월', 6:'6월', 7:'7월', 8:'8월', 9:'9월', 10:'10월', 11:'11월', 12:'12월'}
for i in range(1,13) : 
    print(Month[i]) 

#dictionary method
print("Month.keys() : ", Month.keys())
print("Month.values() : ", Month.values())
print("Month.items() : ", Month.items())

for i in Month.keys() :
    print(Month[i])