class Smallest:
    def second(self, nums):
        if len(nums) < 2:
            return None
        nums.sort()
        return nums[1]
    
    
numbers = input("Enter->").split()
numbers = [int(num) for num in numbers]

a = Smallest()
b = a.second(numbers)

if b is not None:
    print(b)
else:
    print("Error")
















































