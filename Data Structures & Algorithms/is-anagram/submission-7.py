class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ob1,ob2 = {},{}

        if(len(s)!= len(t)):
            return False
        for e in s:
            if e in ob1:
                ob1[e] += 1
            else:
                ob1[e] =1
        for e in t:
            if e in ob2:
                ob2[e] += 1
            else:
                ob2[e] = 1
        if (ob1 == ob2):
            return True
        else: 
            return False

    
        