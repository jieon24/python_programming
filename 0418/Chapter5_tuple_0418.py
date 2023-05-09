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