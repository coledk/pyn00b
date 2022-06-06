s = input()
us = []
cnt = ''
for i in range(len(s)):
    if not ('0' <= s[i] <= '9'):
        us.append(s[i])
    elif ('0' <= s[i] <= '9'):
        cnt += s[i]

print(us)
print(cnt)
exit()
