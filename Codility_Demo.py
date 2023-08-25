def solution(A):
    num_list = tuple(sorted(A))
    if num_list:
        first_num = num_list[0]
        end_num = num_list[-1]
        range_end = num_list[-1] + 2
        if end_num < 1 or first_num > 1:
            return 1
        else:
            for number in range(1, range_end):
                if number in num_list:
                    pass
                else:
                    return number
    else:
        return 1


A = [1, 3, 6, 4, 1, 2]
print('A: ', A)
print(solution(A))
assert solution(A) == 5
A = [1, 2, 3]
print('A: ', A)
print(solution(A))
assert solution(A) == 4
A = [-1, -3]
print('A: ', A)
print(solution(A))
assert solution(A) == 1



