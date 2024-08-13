# class House:
#     numberOfHouse = 0
#     def __init__(self,id,name):
#         self.id = id
#         self.name = name
#         self.neighbour = None
#         House.numberOfHouse += 1
#     def changeNeighbour(self,a):
#         self.neighbour = a
#     def changName(self,name):
#         self.name = name
#     def print_house(self):
#         if self.neighbour != None:
#             print(self.name,self.id,self.neighbour.name)
#         else:
#             print(self.name,self.id)
# class Community:
#     def __init__(self):
#         self.start = None
#     def add_at_start(self,a):
#         a.changeNeighbour(self.start)
#         self.start = a
#     def print_community(self):
#         start = self.start
#         print("\nAll House of Community:")
#         while start != None:
#             start.print_house()
#             start = start.neighbour
#     def search(self,ide):
#         start = self.start
#         flag = True
#         while start != None:
#             if start.id == ide:
#                 print(f"\nThe house having id {ide} is {start.name} house.")
#                 flag = False
#             start = start.neighbour
#         if flag:
#             print("This House Does not Exist In Community.")
#     def midHouse(self):
#         mid = (House.numberOfHouse+1)//2
#         start = self.start
#         i = 1
#         while start != None:
#             if i == mid:
#                 print(f"\nThe mid House of community is {start.name} House.")
#             start = start.neighbour
#             i += 1
#
#     def addHouse(self,point,object):
#         if point > House.numberOfHouse:
#             print("\nThere is no such house at that point! Please Enter correct point.")
#         if point == 1:
#             return myCommunity.add_at_start(object)
#         start = self.start
#         i = 2
#         while start != None:
#             if i == point:
#                 object.neighbour = start.neighbour
#                 start.neighbour= object
#                 break
#             start = start.neighbour
#             i += 1
#
#
#
#
# myCommunity = Community()
#
# myCommunity.add_at_start(House(11,"ali"))
# myCommunity.add_at_start(House(21,"sajid"))
# myCommunity.add_at_start(House(13,"Naveed"))
# myCommunity.add_at_start(House(14,"Asgher"))
# myCommunity.add_at_start(House(25,"Sadaqat"))
# a = House(23,'salim')
# myCommunity.add_at_start(a)
#
# # myCommunity.print_community()
# # a.changName('raza')                             # change the name of a house
# myCommunity.search(25)                          # search the house by id in community and print its name
# myCommunity.midHouse()                          # print the mid house of community
# myCommunity.addHouse(7,House(12,"saqib"))       # add a new house at spcific point
#
# myCommunity.print_community()
l = [1,2,4,5,11,13,20,21,21,26,21,27,30]
st = 0
en = len(l)
mid = (st+en)/2
# while True:
for i in range(st,en):
    k = 21
    if l[mid] == k:
        print("yes")
        break
    if l[mid] > k:
        print(l[mid])
        en = mid
    if l[mid] < k:
        print("ll")
        st = mid
