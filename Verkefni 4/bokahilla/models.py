from bokahilla import app

class bokin:
    def __init__(self,listi):
        self.bok = listi["bok"]
        self.utgef = listi["utgef"]
        self.mynd = listi["mynd"]
        self.hofundur = listi["hofundur"]
        self.URL=listi["URL"]
    def bok(self):
        return self.bok
    def URL(self):
        return self.URL

class URLCheck:
    def __init__(self,listi,URL):
        self.listi=listi
        self.URL=URL
    def check(self):
        for x in self.listi:
            if self.URL==x.URL:
                return x
listi=[bokin({"bok":"Christian Bale","utgef":"Scholastic Press","mynd":"../static/man.jpg","hofundur":"Suzanne Collins","URL":"bale"}),
       bokin({"bok":"Heath Ledger","utgef":"Scholastic Press","mynd":"../static/man.jpg","hofundur":"Suzanne Collins","URL":"ledger"}),
       bokin({"bok":"Heath Ledger","utgef":"Scholastic Press","mynd":"../static/man.jpg","hofundur":"Suzanne Collins","URL":"Catching-Fire"}),
       bokin({"bok":"annar leikara","utgef":"Scholastic Press","mynd":"../static/man.jpg","hofundur":"Suzanne Collins","URL":"hafdusamband"})]
