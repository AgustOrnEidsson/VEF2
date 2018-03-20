from bokahilla import app

class bokin:
    def __init__(self,listi):
        self.bok = listi["bok"]
        self.utgef = listi["utgef"]
        self.ar = listi["ar"]
        self.hofundur = listi["hofundur"]
        self.URL=listi["URL"]
    def bok(self):
        return self.bok
    def URL(self):
        return self.URL
    def lysing(self):
        utskrift="Þetta er bókin "+self.bok+"\n"+" hún var gefin út árið "+self.ar+"\n"+", höfundur þessara bókar er "+self.hofundur+"\n"+" og útgáfu fyrirtækið er "+self.utgef
        return utskrift

class URLCheck:
    def __init__(self,listi,URL):
        self.listi=listi
        self.URL=URL
    def check(self):
        for x in self.listi:
            if self.URL==x.URL:
                return x
listi=[bokin({"bok":"The Hunger Games","utgef":"Scholastic Press","ar":"2008","hofundur":"Suzanne Collins","URL":"The-Hunger-Games"}),
       bokin({"bok":"Catching Fire","utgef":"Scholastic Press","ar":"2009","hofundur":"Suzanne Collins","URL":"Catching-Fire"}),
       bokin({"bok":"Mockingjay","utgef":"Scholastic Press","ar":"2010","hofundur":"Suzanne Collins","URL":"Mockingjay"})]