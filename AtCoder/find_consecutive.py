N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

# Merge A and B lists into a single sorted list C
C = A + B
C.sort()

result = "No"
for i in range(len(C) - 1):
    if C[i] in A and C[i+1] in A:
        result = "Yes"
        break

print(result)