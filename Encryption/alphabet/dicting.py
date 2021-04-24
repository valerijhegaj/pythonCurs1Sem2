class dicting:
    def create(alph):
        ans = dict()
        for i in range(len(alph)):
            ans[i] = alph[i]
            ans[alph[i]] = i
        return ans
