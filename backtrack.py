class permutation:
    def permutation ( self, str, perm):
        
        if (len (str) == 0):
            print (perm)
            return
        for i in range(len(str)):
            ch = str [i]
            newperm = perm + ch
            newstr= str [:i]+str[i+1:]
            self.permutation(newstr, newperm )

new_permutation = permutation ()
new_permutation.permutation ("ABC", "")
            
            