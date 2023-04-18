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

# Month.keys()
for i in Month.keys() : #[1,2,3,4....,12]
    print(Month[i])

print("================")

# Month.values()
for i in Month.values() : #['1월','2월'....,'12월']
    print(i)

print("================")

# 1. Month.items()
for item in Month.items() : #[1,'1월']
    #print(item)
    print(item[1])

print("================")

# 2. Month.items()
for k,v in Month.items() : #[1,'1월'] = [k, v]
    #print(item)
    print(v)

# Month = {1:'1월', 2:'2월', 3:'3월', 4:'4월', 5:'5월', 6:'6월', 7:'7월', 8:'8월', 9:'9월', 10:'10월', 11:'11월', 12:'12월'}
for i in Month : #Month.keys()
    print(i) #처음은 keys값이 나온다.



print("Month.pop(10) : ", Month.pop(10))
print(Month)
print("Month.popitem() : ", Month.popitem())
print(Month)

print(Month.update({3:'March'}))
print(Month)
print(Month.update({13:'13월'}))
print(Month)
print(Month.update({3:'300'})) #추가X, 계속 값만 바뀜
print(Month)