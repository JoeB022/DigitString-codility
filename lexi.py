def my_solution(S):
    s = list(S)
    i = 0 # initializing a pointer

    while i < len(s) -1:
        if int(s[i]) + int(s[i+1]) <= 9:
            total = int(s[i]) + int(s[i+1]) # sum of the two digits
            s[i] = str(total) # replace the two digits with their sum
            del s[i+1] # delete the next digit
            
            # move back to check if the new digit can be summed with the previous one
            if i > 0:
                i -= 1

        else:
            i += 1
    return ''.join(s)
# te
print (my_solution("32581"))
print (my_solution("2353"))
print (my_solution("43422"))
print (my_solution("226226"))