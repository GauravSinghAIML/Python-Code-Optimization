#Problem Statement: Read JSON data which is in text format
#                  and find the word and its count pair.
#===========================Beginner====================================
#It will have 6 variable- and alot of space for all
import json
from glob import glob
lsOfKPE=[]
mapWordFrequncy = {}
path = "C:/OCI_lang_services/results/save/Key_Phrase/"
kpeDoc = glob(path+"*.txt")
for txtdoc in kpeDoc:
    txtopen = open(txtdoc)
    txtdetails = txtopen.read()
    jdata=json.loads(txtdetails)
    kyph = jdata["key_phrases"]
    lsOfKPE.extend(kyph)
    

for w in lsOfKPE:
    wordfreq = lsOfKPE.count(w)
    mapWordFrequncy.update({w:wordfreq })
#==========================Intermediate=====================================
#Little bit optimized. It will have 3 variable- and less space as compare to above
import json
from glob import glob
lsOfKPE=[]
mapWordFrequncy = {}
for txtdoc in glob("C:/OCI_lang_services/results/save/Key_Phrase/"+"*.txt"):
    lsOfKPE.extend(json.loads(open(txtdoc).read())["key_phrases"])   

for w in lsOfKPE:
    mapWordFrequncy.update({w:lsOfKPE.count(w)})
#==========================Advance=====================================
#Little more optimized. It will have 3 variable- and less space as compare to above
# List comprehention instead of for-loop
import json
from glob import glob
lsOfKPE=[]
mapWordFrequncy = {}
[lsOfKPE.extend(json.loads(open(txtdoc).read())["key_phrases"]) for txtdoc in glob("C:/OCI_lang_services/results/save/Key_Phrase/"+"*.txt")]
def mapOfWordAndCount(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(list(zip(wordlist,wordfreq)))
mapWordFrequncy=wordListToFreqDict(lsOfKPE)
#==============================Profetionals===================================
#Most optimized. It will have 2 variable- and least space as compare to above
# List comprehention instead of for-loop
#Object Oriented prog. Initial handling of Input Exception
import json
from glob import glob
class WorldAndCount:
    def __init__(self,listOfW):
        self.listOfW = listOfW
    def wordListToFreqMap(self):
        wordfreq = [self.listOfW.count(p) for p in self.listOfW]
        return dict(list(zip(self.listOfW,wordfreq)))

if __name__=="__main__":
    lsOfKPE =[]
    #Simple try-Exception , Not advance as of Now
    try:
        [lsOfKPE.extend(json.loads(open(txtdoc).read())["key_phrases"]) for txtdoc in glob("C:/OCI_lang_services/results/save/Key_Phrase/"+"*.txt")]
        mapWordFrequncy = WorldAndCount(lsOfKPE).wordListToFreqMap()
    except:
        print("Something went wrong")

