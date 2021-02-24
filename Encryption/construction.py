def deconstruction(st):
    st.replace('\n', ' ')
    st = [list(i) for i in st.split()]
    return st

def construction(data):
    ans = ''
    for i in data:
        for j in i:
            ans += j
        ans += ' '
    return ans
