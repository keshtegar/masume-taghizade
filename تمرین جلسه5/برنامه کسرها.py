class Fraction:
    def __init__(self,s,m):
        if m==0:
            raise ValueError("Denominator must not be zero.")  
        self.soorat=s
        self.makhraj=m
    def show(self):
       print(self.soorat,"/",self.makhraj)
    def sum(self,f1):
        result=Fraction(None,None)
        result.soorat=self.soorat*f1.makhraj+self.makhraj*f1.soorat
        result.makhraj=self.makhraj*f1.makhraj
        return result
    def sub(self,f1):
        result=Fraction(None,None)
        result.soorat=self.soorat*f1.makhraj-self.makhraj*f1.soorat
        result.makhraj=self.makhraj*f1.makhraj
        return result
    def divid(self,f1):
        result=Fraction(None,None)
        result.soorat=self.soorat*f1.makhraj 
        result.makhraj=self.makhraj*f1.soorat   
        return result
faraction1=Fraction(2,3)
faraction2=Fraction(3,4)
m=faraction1.sum(faraction2)
m.show()
su=faraction1.sub(faraction2)
su.show()
d=faraction1.divid(faraction2)
d.show()

