''' find which two numbers from 'nums' list add to target value 17 '''

#nums = [1, 5, 8, 12]
#target = 17

# conceptually [brute force], you would cycle through the nums list until a number minus the target value is equal to another number in the list other than itself

'''pseudo'''
# for num in nums: 
#   if target - num == nums[i] and != num:   || OR MAYBE || # if target - num == num in nums  
#       value = target - num
#       answer = []
#       answer.append(value, num)
#   else:
#       return False

'''             hashmap attempt             '''
nums = [1, 5, 8, 12]
target = 17

h = {}

def find_solution():
    for num in nums:
        value = target - num
        if value in h and value != num:
            print("i tried")
            return(value, num)
        h[num] = True
    else:
        print("yikes")
        return False
    
    
print(find_solution())

# Time Complexity: O(n)
# Space Complexity: O(n)



'''             brute force attempt             '''
'''''
nums = [1, 5, 8, 12]
target = 17

answer = []

for num in nums: 
    print(num, "was a ↷")
    value = target - num
    if value in nums and value != num:
        answer.append(value)
        print(answer)
    else:
        print("     yikes")


# Time Complexity: O(n²)
# Space Complexity: O(n)

'''''
