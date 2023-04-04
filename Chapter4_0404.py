# Chapter4_0404.py

#제어문
#if문

'''
if 조건:
    실행문
else:
    실행문0   
'''
#오전? 오후?
hour = 3
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