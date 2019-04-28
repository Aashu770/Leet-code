class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        num_left = 0
        num_right = 0
        first_outer_p = 0
        output = ''
        for i in range(len(S)):
            if S[i] == '(':
                num_left +=1  
            else: # works only if S only contains parentheses
                num_right += 1
            if num_left == num_right:    #When the number are equal it means now we need to remove the outer most brackets and get rest what is inside
                output += S[first_outer_p+1:i] # remove outer most parantheses {first_outer_p: '(' and i would be the last } Slicing is used
                first_outer_p = i + 1 #for next it will be the begining of the first outermost parentheses.
                num_left = num_right = 0
        return output
