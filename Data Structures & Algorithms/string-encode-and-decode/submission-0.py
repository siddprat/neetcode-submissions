class Solution:
    def __init__(self):
        self.crip = ""
        self.lengths = []

    def encode(self, strs: List[str]) -> str:
        x = len(strs)
        #or could do "".join(strs) ; if below dont work do this
        for word in range(x): ##could just do for word in strs
            self.lengths.append(len(strs[word]))
            self.crip += strs[word]
        return self.crip
        #now all words are added to a crip (together)
        #idt needs to return anything, just need variables

    def decode(self, s: str) -> List[str]:
        len_org = len(self.lengths)
        decrip = []
        crip = self.crip #so decoding doesnt wipe self
        for i in range(len_org):
            endpos = self.lengths[i] 
            word = crip[0:endpos]
            crip = crip[endpos: ]
            decrip.append(word)
        return decrip

