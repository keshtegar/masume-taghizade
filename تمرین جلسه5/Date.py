class Date:
    def __init__(self,y,m,d):
        self.y=y
        self.m=m
        self.d=d
    def show(self):
       print(self.y,"/",self.m,"/",self.d)
    def add(self,t2):
        result=Date(None,None,None)
        result.y=self.y+t2.y
        result.m=self.m+t2.m
        result.d=self.d+t2.d
        if result.d >= 30:
            result.d-=30
            result.m+=1
        if result.m >= 12:
            result.m-=12
            result.y+=1 
        return result
    def sub(self,t2):
        result=Date(None,None,None)
        result.y=self.y-t2.y
        result.m=self.m-t2.m
        result.d=self.d-t2.d 
        if result.d<0:
            result.d+=30
            result.m-=1
        if result.m<0:
            result.m+=12
            result.y-=1
        return result
tarikh1=Date(2020,8,18)
tarikh2=Date(1983,9,29)
a=tarikh1.add(tarikh2)
a.show()
s=tarikh1.sub(tarikh2)
s.show()