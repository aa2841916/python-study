# class apple:
#     def __init__(self,w,c,h,l):
#         self.weight = w
#         self.color = c
#         self.high = h
#         self.long = l
#         print('cread')
#
# app1 = apple(10,'red','12cm','5cm')
# print(app1)

# import math
#
# class circle:
#     def __init__(self,r):
#         self.radius = r
#
#     def area(self):
#         return math.pi * self.radius ** 2
#
#
# cir1 = circle(3)
# print(cir1.area())
#
#
# class Triangle:
#     def __init__(self,l,h):
#         self.high = h
#         self.long = l
#
#     def area(self):
#         return self.high * self.long
#
#     def change_size(self,l,h):
#         self.high = h
#         self.long = l
#
#
# Tri = Triangle(10,20)
# Tri.change_size(20,30)
# area1 = Tri.area()
#
# print(area1)
#
#
# class Hexagon:
#     def __init__(self,r):
#         self.radiox = r
#
#     def cacculate_perimeter(self):
#         return self.radiox * 6
#
# hex = Hexagon(10)
# long = hex.cacculate_perimeter()
# print(long)

# class Shape:
#     def what_am_i(self):
#         print('I am s shape')
#
# class Rectangle(Shape):
#     def __init__(self,l,h):
#         self.long = l
#         self.hight = h
#
#     def calculate_perimeter(self):
#         return 2 * self.long + 2 * self.hight
#
# class Square(Rectangle):
#     def change_size(self,s):
#         st = self.long + s
#         sy = self.hight + s
#         return st,sy
#
#
# Rectangle(10, 3).what_am_i()
# print(Square(10,3).change_size(3))
# Square(10,3).what_am_i()


# class Horse():
#     def __init__(self,name,breed,owner):
#         self.name = name
#         self.breed = breed
#         self.owner = owner
#
# class Rider():
#     def __init__(self,name):
#         self.name = name
#
# mick = Rider('hudi')
# stan = Horse('yao','ming',mick)
# ddd = stan.owner.name
#
# print(ddd)


# class Square:
#     list = []
#
#     def __init__(self,c,d):
#         self.css = c
#         self.ddd = d
#         self.list.append((self.css,self.ddd))
#
#     def print_size(self):
#         print("{} by {} by {} by {}".format(self.css,self.ddd,self.css,self.ddd))
#
# cd = Square(10,12)
# dddd = Square(22,22)
#
# print(Square.list)
# Square(29,28).print_size()


# def f(x,y):
#     print(x is y)
#
# f(2,2)
