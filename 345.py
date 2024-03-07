class Solution:
    def reverseVowels(self, s: str) -> str:
        seq = []
        letter = []
        s=list(s)
        for i in range(0,len(s)):
            if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u' or s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U':
                seq.append(i)
                letter.append(s[i])
        letter.reverse()
        for i in range(0,len(seq)):
            s[seq[i]]=letter[i]
        s=''.join(s)
        return s

            
        
