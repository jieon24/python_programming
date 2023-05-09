# Chapter4_0404.py

#반복문
#while문

'''
while 조건
    수행문
'''

'''
i = 10
while i > 5 :
    print(i," 는 5보다 크다.")
    i = i - 1
'''

#num=1부터 5까지 값을 나오게 함
#1 2 3 4 5
'''
i = 1
while i <= 5 :
    print(i,end=' ** ')
    i = i + 1
else :
    print("while문이 잘 끝났습니다!")
    print("현재 i의 값은 ",i,"입니다")
'''
'''
#놀이기구 탑승 (최대인원 4명, 키 150이상)
people = 0
while people < 4 :
    height = input("당신의 키는?")
    int_height = int(height) 
    if int_height > 150 :    
        people = people + 1
        print("한명 탑승")
        print("현재 인원 : ",people)
    else :
        print("키 150cm미만이라서 못타요!!")
else :
    print("정원 탑승 완료 출발합니다~!")
'''

#continue, break
#반복문 중간에 반보을 더 이상 하지 않고 실행을 종료
#반복문 안쪽에서 실행된다(주로 if문 안에서 사용)

#input으로 입력 받는데
#무한반복
#exit리는 값을 받으면 입력받는 것을 종료
'''
while True :
    str = input("단어를 넣으세요")
    if str == "exit" :
        print("넌 exit를 입력했다. 그래서 종료됩니다.")
        break
    else :
        if str == "apple":
            print("apple을 입력받았음")
            print("continue실행함")
            continue
        print("넌 이 단어를 입력했다. ", str)

    print(str, "저는 아직 while안에 있어요.")    
        
print("while이 종료됨")        
'''

#input으로 입력을 받는데 무한반복
#exit이라는 값을 받으면 입력받는것을 종료
#apple를 받으면 사과를 입력햤다 ""하고 다시 입력 받기
#그 외 단어 입력받으면 해당단어 3번 읽기

while True :
    str = input("단어를 넣으세요")
    if str == "exit" :
        print("넌 exit를 입력했다.")
        break
    else :
        if str == "apple":
            print("apple을 입력받았음")
            print("continue실행함")
            continue
        print("넌 이 단어를 입력했다. ", str)
    print("당신이 입력한 단어는 ", str)    
        
print("입력받기 종료됨")        