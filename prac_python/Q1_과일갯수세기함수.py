# Q1. 과일 갯수 세기 함수 만들기

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

count = 0
for fruit in fruits:
	if fruit == '사과':
		count += 1

print(f"과일 전체 갯수: {count}")   #과일 전체 갯수

# 사과의 갯수를 세어 보여줍니다.

def count_fruits(target):
	count = 0
	for fruit in fruits:
		if fruit == target:
			count += 1
	return count

subak_count = count_fruits('수박')
print(f"수박의 갯수: {subak_count}") #수박의 갯수

gam_count = count_fruits('감')
print(f"감의 갯수: {gam_count}") #감의 갯수