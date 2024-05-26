# S = input()
# T = input()

# correct_positions = []
# i, j = 0, 0

# while i < len(S) and j < len(T):
#     if S[i] == T[j]:
#         correct_positions.append(j + 1)  # Add 1 to convert from 0-indexed to 1-indexed position
#         i += 1
#     j += 1

# print(*correct_positions)

# Note :  asterisk * operator is used to unpack an iterable (such as a list, tuple, or set) into individual elements.

# or 

# s = input()
# t = input()
# min_index = 1
# for i in s:
#     if i in t:
#         d=i.index()
#     print(d)

# s=input()
# t=input()
# i=2
# for i in s:
#     if i in t:
#         print(t.index(i)+1)


A=list(map(int,input().split()))
c=0
for i in range(len(A)):
  if (i>0):
    c+=1
    if (i<0):
      break
  print(c)

