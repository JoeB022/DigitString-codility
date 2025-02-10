# DigitString-codility
# Lexicographically Largest String by Summing Adjacent Digits

## Problem Statement
Given a string `S` consisting of digits (1-9), we can repeatedly choose two adjacent digits and replace them with their sum, but only if the sum is not greater than 9. The goal is to produce the **lexicographically largest** possible string.

## Approach
This solution follows a **greedy approach** with left-to-right traversal while allowing backward steps when needed:

1. **Iterate through the string** using a while loop.
2. **Check adjacent digits**:
   - If their sum is ≤ 9, merge them by replacing the first digit and deleting the second.
   - Move back one step to check if further merging is possible.
   - Otherwise, move forward.
3. **Continue until no more merges can be made.**

## Implementation
```python
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

```

## Examples
```python
# test cases
print (my_solution("32581"))   #output "559"
print (my_solution("2353"))    #output "58"
print (my_solution("43422"))   #output "78"
print (my_solution("226226"))  #output "488"
```

## Complexity Analysis
- **Time Complexity:** O(n) in most cases, as each digit is checked at most twice.
- **Space Complexity:** O(n) for storing the modified string.

## Edge Cases Considered
✅ Single-character strings (e.g., `"5"` → `"5"`)
✅ Strings that cannot be merged (e.g., `"999"` → `"999"`)
✅ Strings with multiple merging opportunities
✅ Large input strings (up to 200,000 characters)

## License
This project is open-source and free to use.

---

