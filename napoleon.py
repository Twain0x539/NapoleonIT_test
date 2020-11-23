class Solution():
    def romanToInt(self,s):
        definitions = {'I' : 1, 'V':5, 'X':10,'L':50,'C': 100, 'D':500, 'M':1000}
        numeric = 0
        cur_pos = 0
        while(cur_pos + 1 != len(s)):
            char = s[cur_pos]
            next_char = s[cur_pos + 1]
            if definitions[char] >= definitions[next_char]:
                numeric += definitions[char]
            else:
                numeric -= definitions[char]
            cur_pos += 1
        numeric += definitions[s[cur_pos]]

        return numeric
