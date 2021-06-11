#finished in 23m 30s
def removeInstanceOf(remove, string):
    for x in range(len(string)):
        if string[x] == remove:
            string = string.replace(string[x], "", 1)
            break
    return string

def find_anagrams(s, t):
    ans = []
    for x in range(len(s)):
        if s[x] in t:
            temp = removeInstanceOf(s[x], t)
            for y in range(len(t)):
                if x+y+1 >= len(s):
                    break
                if s[x + y + 1] in temp:
                    temp = removeInstanceOf(s[x + y + 1], temp)
                else:
                    break
            if temp == "":
                ans.append(x)
    return ans

print(find_anagrams('acdbacdacb', 'abc'))
# [3, 7]