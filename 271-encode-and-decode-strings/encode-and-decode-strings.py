class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # length#str#length#char
        strs = [ str(len(s))+"#"+s for s in strs]
        res = "".join(strs)
        # print(res)
        return res
        
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            st = s[j+1:j+1+length]
            # print(st)
            res.append(st)
            i = j + 1 + length 
        return res            
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))