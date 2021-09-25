import sys

#문자열 입력받기
data=sys.stdin.readline().rstrip() #readline()을 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력되는데, 이 공백 문자를 제거하기 위해 rstrip()함수 사용
print(data)