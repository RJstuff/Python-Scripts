"""
def reverse(s):
    r = ''
    for i in s:
        r = i+r

    return r
print(reverse("abcdefgh"))
"""

def find_missing(full_set,partial_set):
    missing = set(full_set) - set(partial_set)
    return list(missing)

print(find_missing([12,13,14,15],[12,13,14,16]))

      
