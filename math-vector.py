# import math


# class Vector:

#     def __init__(self, x = 0, y = 0 ):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return f'Vector {self.x!r}, {self.y!r}'

#     def __abs__(self):
#         return math.hypot(self.x, self.y)

#     def __bool__(self):
#         return bool(abs(self))

#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Vector(x + y)

#     def __mul__(self, scalar):
#         return Vector(self.x * scalar, self.y * scalar)
    
#     def __getitem__(self, index):
#         if index == 0:
#             return self.x
#         elif index == 1:
#             return self.y
#         else:
#             raise IndexError("Vector index out of range")
# vector1 = Vector(x = 3,y = 2)
# vector2 = Vector(x = 2,y = 3)
# result_vector = vector1.__add__(vector2)
# print(result_vector)

# vector = Vector(30,1)
# print("Vector: ", vector)
# print("First component: ", vector[0])


# symbols = '$¢£¥€¤'
# codes = []
# for symbol in symbols:
#     codes.append(ord(symbol))

# print(codes)    


colors = ['black', 'white']
sizes = ['S','M','L']

tshirt = []
for color in colors:
    for size in sizes:
        print(color,size)

print(tshirt)