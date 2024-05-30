class Common:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2
    def member(self):
        i = []
        for item in self.list1:
            if item in self.list2:
                i.append(item)
        print(i)
list1 = [1, 6, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
sum = Common(list1, list2)
sum.member()










