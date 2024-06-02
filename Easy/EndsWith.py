# Problem: Ends With

# Problem Description
# Complete the solution so that it returns true if the first argument (string) passed in ends with the second argument (also a string).

# Examples
# solution('abc', 'bc') # returns true
# solution('abc', 'd')  # returns false

def solution(text, ending):
    new_text = text[(len(text) - len(ending)):]
    if new_text == ending:
        result = True
    else:
        result = False
    return result
