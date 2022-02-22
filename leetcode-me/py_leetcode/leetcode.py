#  coding=utf-8


def minWindow(s, t):
    need = {}
    window = {}
    for a in t:need[a] = need.get(a,0)+1
    print("need")
    print(need)
    valid = 0
    start,left,right,l=0,0,0,100001
    while right < len(s):
        c = s[right]
        right=right+1
        if need.__contains__(c):
            window[c] = window.get(c,0)+1
            if window[c] == need[c]:
                valid=valid+1
        # print(right)
        while valid == len(need):
            if right-left < l:
                start = left
                l = right-left
            d = s[left]
            left=left+1
            if need.__contains__(d):
                if window[d] == need[d]:
                    valid = valid-1
                window[d] = window[d]-1
    
    print(l)
    print(start)
    if l == 100001:return ""
    else: return s[start:start+l]


res = minWindow("ADOBECODEBANC","ABC")
print(res)


class Dog(): 

    """一次模拟小狗的简单尝试"""  
    def __init__(self, name, age): 

        """初始化属性name和age"""
        self.name = name 
        self.age = age 
    def sit(self): 
        """模拟小狗被命令时蹲下""" 
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚""" 
        print(self.name.title() + " rolled over!")


class BigDog(Dog):
    def __init__(self,name,age,sex):
        Dog.__init__(self,name,age)
        self.sex = sex
    
    def print_sex(self):
        """模拟小狗被命令时打滚""" 
        print(self.sex + " rolled over!")


myDog = BigDog('abc',12,"a")


myDog.roll_over()

myDog.print_sex()
