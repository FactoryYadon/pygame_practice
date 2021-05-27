import re

# abcd , book , desk
# ca?e,
# care , cafe , case , cave
# 


p = re.compile("ca.e")           
# . (ca.e) : 하나의 문자 의미 > care , cafe , case | caffe
# ^ (^de)  : 문자열의 시작 > desk , destination | fade (X)
# $ (se$)  : 문자열의 끝 > case , base | face (x)


def print_match(a):

    if a:
        print(a.group())                    # 일치하는 문자열 반환
        print(a.string)                     # 입력받은 문자열
        print(a.start())                    # 일치하는 문자열의 시작 인덱스
        print(a.end())                      # 일치하는 문자열의 끝 인덱스
        print(a.span())
    else:
        print("매칭 되지 않음")

# m = p.match("goodcase")                 # 주어진 문자열의 청므부터 일치하는지 확인
# print_match(m)

# m = p.search("good care")               # 주어진 문자열 중에 일치 하는 지 확인
# print_match(m)

# lst = p.findall("good care cafe")
# print(lst)

 
# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") :  주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 

# 원하는 형태 : 정규식
# . (ca.e) : 하나의 문자 의미 > care , cafe , case | caffe
# ^ (^de)  : 문자열의 시작 > desk , destination | fade (X)
# $ (se$)  : 문자열의 끝 > case , base | face (x)