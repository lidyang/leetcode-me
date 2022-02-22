#  coding=utf-8

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
