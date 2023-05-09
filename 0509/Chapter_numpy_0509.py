# 0509.py
import sys
#print(sys.builtin_module_names)

import numpy # as np -> 쓰기 너무 길어서 짧게 별명처럼
# 다운로드 방법1 -> pip install numpy
# 다운로드 방법2 ctrl + shift + p -> python: Select Insterpreter 선택-> base~ 선택
arrA = numpy.array([1,2,3,4,5])
arrB = numpy.array([6,7,8,9,10])
#lst = [1,2,3,4,5]
print(arrA + arrB) # 답 [7 9 11 13 15]
print(arrA - arrB) # 답 [-5 -5 -5 -5 -5]
print(arrA * arrB) # [ 6 14 24 36 50]
print(arrA / arrB) # [0.16666667 0.28571429 0.375 0.44444444 0.5]

print(type(numpy.array([1,2,3,4,5])))

import math
#from math import gcd -> print(gcd(10,20))로 사용 가능
print(math.fsum([1,2,3]))
print(math.gcd(10,20))

import hello_0509 as h

print("=================")
h.helloworld()
