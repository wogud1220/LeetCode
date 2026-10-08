n, k = map(int, input().split())

arr = list(range(1, n + 1))
idx = 0

while arr:
    idx += k - 1

    # 배열 끝을 넘어가면 처음으로 돌아오기
    idx %= len(arr)

    print(arr[idx], end=' ')
    arr.pop(idx)