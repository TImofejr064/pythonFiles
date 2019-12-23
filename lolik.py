def accum(s):
    x = ''
    for i in range(0, len(s)):      
        if  i <= len(s)-1 and i != 0 :
            x += '-'

        x += s[i].upper()

        for j in range(0, i):
            x += s[i].lower()

    return x

        
        

print(accum('ZpglnRxqenU'))

