# Chapter4_0404.py

#제어문
#if문

'''
if 조건:
    실행문
else:
    실행문0   
'''

'''
#오전? 오후?
hour_str = input("현재 시간은?)
hour = int(hour_str)

if hour>12 :
    print("12시가 지났으니 오후 입니다!")
else :
    print("12시가 지나지 않았으니까 오전 입니다~")   

#오전? 오후? 저녁?
hour = 15
if hour < 12 :
    print("12시가 지나지 않았으니까 오전 입니다~")
elif hour < 18 :
    print("12시가 지나고 18시가 안지났으니 오후 입니다^^")    
else :
    print("18시가 지났으니 저녁 입니다!")   
'''

#장학금 
#score < 200 50만원 줌
#200 >= score < 400 100만원 줌
#400 >= score < 500 10000만원 줌

'''score_str = input("점수는? ")
score = int(score_str)

if score < 200 :
    print("50만원 획득")
elif score < 400 :
    print("100만원 획득")
else :
    print("10000만원 획득")
'''

#점심메뉴
answer = input("오늘 학식 먹을래?")
if answer == 'yes' :
    print("8호관 1층 ㄱㄱ")
else :
    again_answer = input("떡볶이?")
    if again_answer == 'yes' :
        print("5호관 3층")
    else :
        print("걍 아무것도 먹지마")