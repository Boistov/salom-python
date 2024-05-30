class Tuple:
    def __init__(self):
        pass
    def find_index(self, my_text, harf):
        try:
            index = my_text.index(harf)
            return index
        except Error:
            return harf

my_text = input().split()
harf = input()
finder = Tuple()
result = finder.find_index(my_text, harf)
print(result)
print(harf)
