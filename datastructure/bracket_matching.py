"""
Input Format. => Input contains one string 𝑆 which consists of big and small latin letters, digits, punctuation marks and brackets from the set []{}().
Constraints. => The length of 𝑆 is at least 1 and at most 105.
Output Format. => If the code in 𝑆 uses brackets correctly, output “Success" (without the quotes). Otherwise, output the 1-based index of the first unmatched closing bracket, and if there are no unmatched closing brackets, output the 1-based index of the first unmatched opening bracket.
"""
from collections import namedtuple, deque

Bracket = namedtuple('Bracket', "ind char")
# create an helper function to determing if char is bracket
is_opening = lambda x: x in "([{<"
is_closing = lambda x: x in ")]}>"
# create a helper function that return true if two given bracket matches
are_matched = lambda x,y: x.char+y.char in ['()','{}','<>','[]']
# use namedtuple to namespace brackets in the string keep track refrencing the bracket char and it index

def find_mismatch(s):
    stack = deque([])
    for i in range(len(s)):
        if is_opening(s[i]):
            stack.append(Bracket(i+1, s[i]))
            continue
        elif is_closing(s[i]):
            bracket = Bracket(i+1, s[i])
            if len(stack) == 0:
                return bracket
            prev_bracket = stack.pop()
            if not are_matched(prev_bracket,bracket):
                return bracket
    #if any opening bracket left return the earliest one
    if len(stack)>0:
        return stack.popleft()
    return None

def main(text):
    mismatch = find_mismatch(text)
    if not mismatch:
        print('Success')
        # return('Success')
    else:
        print(mismatch.ind)
        # return(mismatch.ind)

if __name__ == "__main__":
    text = input()
    main(text)
