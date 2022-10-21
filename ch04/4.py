# 자료형
# type() 함수를 사용하여 쉽게 자료형을 확인할 수 있다.

# 숫자에는 정수(int), 소수점(float), 복소수(complex)가 있다.
print(type(100000))
print(type(2.8))
print(type(3+4j))

# 시퀀스에는 문자열(str), 리스트(list), 튜플(tuple)이 있다.
# for문에서 사용할 수 있는것들이 시퀀스다.
print(type("Love"))
print(type(["love","enemy","fault"]))
print(type(("love","enemy","fault")))

# 매핑에는 딕셔너리(dict)가 있고 키와 값의 짝으로 이루어져있다.
print(type({"one":1, "two":2,"three":3}))

# 참, 거짓을 표현하는 불(bool)도 있다.
print(type(False))
print(type(3 >= 1))

# 집합을 표현하는 세트(set)도 있다.
fruits = {"apple", "banana"}
print(type(fruits))