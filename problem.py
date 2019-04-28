class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        # one pass: go from left to right, accumulate the number of
        # ( and ), when they are equal: that's a break point,
        # then concat output and reset the accumulated variables.
        num_left = 0
        num_right = 0
        break_point = 0
        output = ''
        for i in range(len(S)):
            if S[i] == '(':
                num_left +=1  
            else: # works only if S only contains parentheses
                num_right += 1
            if num_left == num_right:
                output += S[break_point+1:i] # remove first and last char
                break_point = i + 1
                num_left = num_right = 0
        return output
