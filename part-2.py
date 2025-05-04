# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if len(array) == 0:
        return False
    
    if array[0] == query:
        return True
    
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if len(text) == 1 or len(text) == 0:
        return True
    
    if text[0] != text[-1]:
        return False
        
    return is_palindrome(text[1:-1])
        


# digit_match
def digit_match(int1, int2):  
    count = 0
    # base case when we compare just one digit with last digit of a longer number
    # this is where our recursion will stop
    if int1 // 10 == 0 or int2 // 10 == 0:
        if int1%10 == int2%10:
            return 1
        else:
            return 0
        
    # recursive case    
    if int1%10 == int2%10:
        count = 1
 
    return (count + digit_match(int1//10, int2//10))

