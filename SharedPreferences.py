import shelve

import os
import sys
class SharedPrefrences():
    def __init__(self, Name, Developer_mode = False):
        os.makedirs(f'C:/{(((sys.argv[0]).split("/"))[-1]).replace(".py", "")}', exist_ok=True) # - > Created folder.
        self.Name = Name # - > We will need it later for creating.
        self.isDev = Developer_mode # - > We will need it later for conditioning.
        self.dir = f'C:/{(((sys.argv[0]).split("/"))[-1]).replace(".py", "")}'
    def AddKeyWithValue(self, key, value):
        with shelve.open(self.dir+'/'+self.Name) as pref:
            if key not in dict(pref): # - > IF doesn't exists.
                pref[key] = value     # - > Adding like dict
                if self.isDev == True:
                    print(f"log raise - >\n added key {key} with value {value} to preference {self.Name}, \n Preferences files in {self.dir} : {os.listdir(self.dir)}, \n Current data in {self.Name} => {dict(pref)}")
                else:
                    pass
            else:
                raise (f'Key {key} is already exists, try using EditKeyValue()') # - > Faliure msg.
    def EditKeyValue(self, key, value):
        if f'{self.Name}.dat' in os.listdir(self.dir):
            with shelve.open(self.dir+'/'+self.Name) as pref:
                if key in dict(pref):
                    pref[key] = value
                else:
                    raise "Key doesn't exists."
        else:
            raise f'Preference {self.Name} is not found in {dir}.'
    def DeletKey(self, key):
        if f'{self.Name}.dat' in os.listdir(self.dir):
            with shelve.open(self.dir+'/'+self.Name) as pref:
                if key in dict(pref):
                    del pref[key]
                else:
                    raise "Key doesn't exists."
        else:
            raise f'Preference {self.Name} is not found in {dir}.'
    def RetrieveValue(self, key):
        if f'{self.Name}.dat' in os.listdir(self.dir):
            with shelve.open(self.dir+'/'+self.Name) as pref:
                val = pref[key] if pref[key] in dict(pref) else None
                if val != None:
                    return val
                else:
                    raise 'Key not found.'
    def Cache(self):
        pass # Soon.








