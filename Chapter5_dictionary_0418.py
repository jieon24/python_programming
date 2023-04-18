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

coffee = ['Espresso','Americano','Latte']
coffee = tuple(coffee)
print(coffee)
print(type(coffee))
print(list(enumerate(coffee)))
print(dict(enumerate(coffee)))





#zip
# list, tuple 가 여러개 -> 하나의 tuple의 조합으로 된 리스트
li =['class1','class2','class3']
YA = ['Hong', 'Kim', 'Lee']
YB = ['Gang', 'Park', 'James']

z = zip(li,YA,YB)
print(type(z))
print(z)
print(list(z))
print(tuple(zip(li,YA,YB)))

food = ['한식','양식','중식','일식','분식']
f1 = ['비빔밥','파스타','짜장면','스시','떡볶이']
f2 = ['불고기','피자','탕수육','우동','라면']
print(list(zip(food,f1,f2)))

print("================")

for i in range(5) : 
    print(food[i] ,":" ,f1[i],f2[i])

print("================")

lfood = list(zip(food,f1,f2))
for i in lfood :
    print(i[0],i[1],i[2])

subject = ['Python','C','Java','AI','Iot']
room = ['101','213','315','210','314']
s = dict(zip(subject,room))

while True :
    c = input("What's your subject name? : ")
    if c == "quit" :
        print("quit을 입력했습니다. 종료합니다")
        break
    else :
        if c in s.keys() : 
            print(s[c])
        else : 
            continue

