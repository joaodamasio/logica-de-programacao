#Target = 9
#list = [11, 15, 2, 7]
#return the positional element

#Using hash
def twoSum(nums, target) -> list[int]:
    hasher = {}
    for idx, i in enumerate(nums):
        if hasher.get(i) is not None:
            return[hasher.get(i), idx]
        hasher[target-i] = idx
            
        
res = twoSum([11, 15, 2, 7], 9)

print(res)