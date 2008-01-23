import re
import time
import os,sys
import glob

class Player:
    def __init__(self,name):
        self.values = {"name":None,"ws_count":0,"ws_high":0,
                       "crit_count":0,"evades":0,"parries":0,
                       "hits":0,"misses":0,"swings":0,
                       "spells":0,"ttlspelldmg":0,"heals":0,
                       "ttlheals":0,"hprec":0,"ttldmg":0,
                       "addeffects":0,"addeffectdmg":0,"dmgtaken":0,
                       "magicbursts":0,"mb_high":0,"rngattks":0,
                       "rnghits":0,"rngmisses":0,"rngdmg":0,"wsdmg":0,
                       "mobswings":0
                       }
        self.values["name"] = name
    
    def SetValue(self,item,increment):
        if item in self.values:
            self.values[item] = self.values[item] + increment
            return True
        else:
            return False
    
    def GetValue(self,item):
        if item in self.values:
            return self.values[item]
        else:
            return False

class Parser:
    def __init__(self,PathToLogs):
        self.PathToLogs = PathToLogs
        self.ttlfights = 0
        self.CurrentLine = 0
        self.contLine = False
        self.contPlayer = ""
        self.lastHit = ""
        self.contType = ""
        self.Players = {}
        
    def GetCurrentLine(self):
        self.CurrentLog = os.path.join(self.PathToLogs,self.GetLatestFile())
        f = open(self.CurrentLog,"rb")
        log = f.read()
        f.close()
        
        chatlogarr = log[100:].split('\x00')
        for x in chatlogarr:
            self.CurrentLine = self.CurrentLine + 1
        
    def ParseLog(self):
        f = open(self.CurrentLog,"rb")
        log = f.read()
        f.close()
        
        chatlogarr = log[100:].split('\x00')
        newarr = chatlogarr[self.CurrentLine:]
        
        for x in newarr:
            self.ParseLine(x)
            self.CurrentLine = self.CurrentLine + 1
        
        if self.CurrentLine > 50: 
            match = re.search("[0-9]+.log",self.CurrentLog)
            if int(match.group().split(".")[0]) == 19:
                nextLog = os.path.join(self.PathToLogs,"0.log")
            else:
                nextLog = os.path.join(self.PathToLogs,str(int(match.group().split(".")[0]) + 1) \
                                  + "." + self.CurrentLog.split(".")[1])
            if os.stat(nextLog)[8] > os.stat(self.CurrentLog)[8]:
                self.CurrentLog = nextLog
                self.CurrentLine = 0
                
    def ParseLine(self,string):
        """Player causes an additional effect"""
        if re.search("Additional effect",string) and self.contPlayer != "":
            obj = self.Players[self.contPlayer]
            if re.search("\:\s[0-9]+\s",string):
                match = re.search("\:\s[0-9]+\s",string)
                dmg = int(re.sub("[\W]","",match.group()))
                obj.SetValue("ttldmg",dmg)
                obj.SetValue("addeffects",1)
                obj.SetValue("addeffectdmg",dmg)
                self.Players[self.contPlayer] = obj
            self.contPlayer = ""
        
        """Mob causes an additional effect"""
        if re.search("Additional effect",string) and self.lastHit != "":
            obj = self.Players[self.lastHit]
            if re.search("\:\s[0-9]+\s",string):
                match = re.search("\:\s[0-9]+\s",string)
                dmg = int(re.sub("[\W]","",match.group()))
                obj.SetValue("dmgtaken",dmg)
                self.Players[self.lastHit] = obj
                self.lastHit = ""
        
        """Line continues from last line because of WS or something"""
        if self.contLine and self.contPlayer != "":
            obj = self.Players[self.contPlayer]
            dmg = int(re.sub("\s.+","",re.sub(".+takes\s","",string)))
            obj.SetValue("ttldmg",dmg)
            if self.contType == "ws" and dmg > obj.GetValue("ws_high"):
                obj.SetValue("ws_high",dmg)
                obj.SetValue("wsdmg",dmg)
            elif self.contType == "ws":
                obj.SetValue("wsdmg",dmg)
            self.Players[self.contPlayer] = obj
            self.contLine = False
            self.contPlayer = ""
        
        if self.contLine and self.contPlayer == "":
            if self.contType == "mobws":
                match = re.search("\x1E\x01[A-Z][a-z]+\s",string)
                name = re.sub("[\W]","",match.group())
                if re.search("takes.+",string):
                    dmg = int(re.sub("[^0-9]","",re.search("takes.+",string)))
                    obj = self.Players[name]
                    obj.SetValue("dmgtaken",dmg)
                    obj.SetValue("mobswings",1)
                    self.Players[name] = obj
                else:
                    obj = self.Players[name]
                    obj.SetValue("mobswings",1)
                    obj.SetValue("evades",1)
                    self.Players[name] = obj
            if self.contType == "mobcrit":
                match = re.search("\x1E\x01[A-Z][a-z]+\s",string)
                name = re.sub("[\W]","",match.group())
                dmg = int(re.sub("[^0-9]","",re.search("takes.+",string)))
                obj = self.Players[name]
                obj.SetValue("mobswings",1)
                obj.SetValue("dmgtaken",dmg)
                self.Players[name] = obj
                self.contLine = False
                self.contType = ""
        """Player scores a critical hit"""
        if re.match("\x31\x34.+critical hit!",string) or re.match("\x31\x39.+critical hit!",string):
            name = re.sub("\s.+","",re.sub("^.+\x1E\x01","",string))
            if name not in self.Players:
                newplayer = Player(name)
                self.Players[name] = newplayer
            
            obj = self.Players[name]
            obj.SetValue("hits",1)
            obj.SetValue("swings",1)
            obj.SetValue("crit_count",1)
            self.Players[name] = obj
            self.contLine = True
            self.contPlayer = name
        
        """Player hits mob"""
        if re.match("\x31\x34.+hits",string) or re.match("\x31\x39.+hits",string):
            name = re.sub("\s.+","",re.sub("^.+\x1E\x01","",string))
            if name not in self.Players:
                newplayer = Player(name)
                self.Players[name] = newplayer
            
            obj = self.Players[name]
            obj.SetValue("hits",1)
            obj.SetValue("swings",1)
            obj.SetValue("ttldmg",int(re.sub("\s.+","",re.sub(".+for\s","",string))))
            self.Players[name] = obj
            """Setting this value so we can check the next line
            for an additional effect."""
            self.contPlayer = name
            
        """TODO: Find Example in logs"""
        """Assuming \x31\x34 and \x31\x39"""
        """Player makes a ranged hit"""
        if re.match("\x31\x34.+ranged attack hits",string) or re.match("\x31\x39.+ranged attack hits", string):
            name = re.sub("\s.+","",re.sub("^.+\x1E\x01","",string))
            if name not in self.Players:
                newplayer = Player(name)
                self.Players[name] = newplayer
            obj = self.Players[name]
            obj.SetValue("rnghits",1)
            obj.SetValue("rngattks",1)
            obj.SetValue("ttldmg",int(re.sub("\s.+","",re.sub(".+for\s","",string))))
            self.Players[name] = obj
            """Setting this value so we can check the next line
            for an additional effect."""
            self.contPlayer = name
            
        """Player uses Weaponskill"""
        if re.match("\x31\x34.+uses",string) or re.match("\x32\x39.+uses",string):
            name = re.sub("\s.+","",re.sub("^.+\x1E\x01","",string))
            if name not in self.Players:
                newplayer = Player(name)
                self.Players[name] = newplayer
                
            obj = self.Players[name]
            obj.SetValue("ws_count",1)
            self.Players[name] = obj
            self.contLine = True
            self.contPlayer = name
            self.contType = "ws"
            
        """Player misses mob"""
        if re.match("\x31\x35.+misses",string) or re.match("\x31\x61.+misses",string):
            name = re.sub("\s.+","",re.sub("^.+\x1E\x01","",string))
            if name not in self.Players:
                newplayer = Player(name)
                self.Players[name] = newplayer
            
            obj = self.Players[name]
            obj.SetValue("swings",1)
            obj.SetValue("misses",1)
            self.Players[name] = obj
        
        """Player evades mob"""
        if re.match("\x31\x64.+misses",string) or re.match("\x32\x31.+misses",string):
            match = re.search("\s[A-Z][a-z]+\.",string)
            name = re.sub("[\W]","",match.group())
            if name not in self.Players:
                newplayer = Player(name)
                self.Players[name] = newplayer
                
            obj = self.Players[name]
            obj.SetValue("evades",1)
            obj.SetValue("mobswings",1)
            self.Players[name] = obj
               
        """Player defeats mob"""
        if re.match("\x32\x34.+defeats",string) or re.match("\x32\x35.+defeats",string):
            self.ttlfights = self.ttlfights + 1
        elif re.match("\x32\x34.+falls to the ground",string) or re.match("\x32\x35.+falls to the ground",string):
            if re.sub("\s.+","",re.sub("^.+\x1E\x01","",string)) not in self.Players:
                self.ttlfights = self.ttlfights + 1
                
        """Mob hits Player"""
        if re.match("\x31\x63.+hits",string) or re.match("\x32\x30.+hits",string):
            match = re.search("\shits\s[A-Z][a-z]+\s",string)
            name = re.sub("[\W]","",re.sub("\shits\s","",match.group()))
            if name not in self.Players:
                newplayer = Player(name)
                self.Players[name] = newplayer
            obj = self.Players[name]
            obj.SetValue("dmgtaken",int(re.sub("\s.+","",re.sub(".+for\s","",string))))
            obj.SetValue("mobswings",1)
            self.Players[name] = obj
            self.lastHit = name
        
        """Mob hits Player with WS"""
        if re.match("\x36\x66.+uses",string):
            self.contLine = True
            self.contType = "mobws"
        
        """Mob hits player with crit"""
        if re.match("\x31\x63.+critical hit!",string) or re.match("\x32\x30.+critical hit!",string):
            self.contLine = True
            self.contType = "mobcrit"
            
    def GetLatestFile(self):
        filelist = os.listdir(self.PathToLogs)
        date_file_list = []
        for file in filelist:
            stats = os.stat(os.path.join(self.PathToLogs,file))
            lastmod_date = time.localtime(stats[8])
            date_file_tuple = lastmod_date, file
            date_file_list.append(date_file_tuple)
        date_file_list.sort()
        date_file_list.reverse()
        
        return date_file_list[0][1]
           
    def MainLoop(self):
        while 1:
            self.ParseLog()
            self.Output()
            time.sleep(5.0)
            
    def GetValues(self):
        return self.Players
        
    def GetCurrentLog(self):
        return self.CurrentLog