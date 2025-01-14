def solution(A : list[int], B: list[int]) -> list[int]:

    # Intialize a set to store values we've seen
    seen = set()

    # Initialize a prefix array with length of A or B since they're the same I'll pick A
    prefix = [0] * len(A)

    # Initialize a counter varaible to keep track with whatever we've seen
    count = 0

    for i in range(len(A)):
        if A[i] in seen:
            count += 1

        seen.add(A[i])

        if B[i] in seen:
            count += 1

        seen.add(B[i])

        prefix[i] = count

    return prefix


# Testing
A = [1,3,2]
B = [2,1,3]

print(solution(A,B)) # [0,1,3]
