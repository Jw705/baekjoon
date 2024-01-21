# 이진 탐색 소스코드 반복문으로 구현
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        elif array[mid] < target:
            start = mid + 1
    return None


# n(원소의 개수), target(찾고자 하는 문자열)
n, target = map(int, input().split())
# 전체 원소
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print('원소가 없어요')
else:
    print(result + 1)

'''
10 7
1 3 5 7 9 11 13 15 17 19

10 7
1 3 5 9 11 13 15 17 19
'''
