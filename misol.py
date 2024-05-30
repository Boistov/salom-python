class Tuple:
    def __init__(self, my_tuple):
        self.my_tuple = my_tuple
    def check(self, element):
        return element in self.my_tuple

def main():
    my_tuple = input()
    checker = Tuple(my_tuple)
    element_to_check = 6
    
    
    if checker.check(element_to_check):
        print(element_to_check)
    else:
        print(element_to_check)
main()
