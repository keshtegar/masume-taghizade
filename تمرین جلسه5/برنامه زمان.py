class Time:
    def __init__(self,h,m,s):
        self.h=h
        self.m=m
        self.s=s
    def show(self):
        print(self.h,":",self.m,":",self.s)
    def sum(self,t2):
        result=Time(None,None,None)
        result.h=self.h+t2.h
        result.m=self.m+t2.m
        result.s=self.s+t2.s
        if result.s >= 60:
           result.s-=60
           result.m+=1
        if result.m >= 60:
           result.m-=60
           result.h+=1    
        return result

    def sub(self,t2):
        result=Time(None,None,None)
        result.h=self.h-t2.h
        result.m=self.m-t2.m
        result.s=self.s-t2.s  
        if result.s<0:
            result.s+=60
            result.m-=1
        if result.m<0:
            result.m+=60
            result.h-=1
        return result
    def conv(self):
        convert=self.h*3600+self.m*60+self.s
        return convert
def conv1(self):     
    hour=int(self/3600)  
    min=int((self-hour*3600)/60)
    second=int((self-hour*3600-min*60))
    return [hour,min,second] 
time1=Time(10,20,25)
time2=Time(8,30,40)
second2=1565
s=time1.sum(time2)
s.show()
s1=time1.sub(time2)
s1.show()
second1=time1.conv()
print(second1)
time=conv1(second2)
print(time[0],time[1],time[2])