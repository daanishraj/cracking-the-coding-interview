##1.7

data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]

data1 = [([1,2,3,4,5],
		  [6,7,8,9,10],
		  [11,12,13,14,15],
		  [16,17,18,19,20],
		  [21,22,23,24,25])]    



# print(type(data1)) 
# print(len(data1)) 
# print(data1)

# matrix = [[0] * 5 for i in range(5)]
# print(matrix)
# print(len(matrix))
# print(type(matrix))

matrix = [[0 for x in range(7)] for y in range(5)]
#print(matrix)

x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
print(*zipped)
x2, y2 = zip(*zip(x, y))

print(x2, y2)

# for a in zip(x):
# 	print(a)

