palindrome = "hannah"
name = palindrome

def two_pointer(name):
    left = 0
    right = len(name) - 1
    while left <= right:
        if name[left] == name[right]:
            print(name[left])
            left = left + 1
            right = right - 1
        else:
            print(name[left])
            return False
    return True


#w's in the chat
print(two_pointer(palindrome))
         
        
