''' Program to transpose a matrix using list comprehension'''

X = [
    [1,2, 3],
    [4 ,5, 6]
    ]

result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
result = [r[::-1] for r in result]

for r in result:
   print(r)
