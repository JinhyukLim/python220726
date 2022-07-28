# DemoRE.py
import re

# 매칭오브젝트
result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())

# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())

# search함수와 match함수의 차이
print(bool(re.search("apple", "this is apple")))
print(bool(re.match("apple", "this is apple")))
print(bool(re.search("\d{4}", "올해는 2022년")))
print(bool(re.search("\d{5}", "우리 동네는 52300")))

result = re.search("\d{5}", "우리 동네는 52300")
print(result.group())

