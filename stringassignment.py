ini_str = "ababababa"
sub_str = 'aba'
 
res = sum(1 for i in range(len(ini_str))
        if ini_str.startswith("aba", i))

print("Number of substrings", res)