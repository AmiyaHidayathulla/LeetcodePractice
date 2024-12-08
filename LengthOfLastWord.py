class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str2=s.strip()
        str3=str2.split(" ")
        lword=str3[-1] if str3 else 0
        return len(lword)
        
