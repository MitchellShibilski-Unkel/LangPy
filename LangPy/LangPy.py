from nltk import pos_tag
from translate import Translator


class LangPy:
    def __init__(self, text: str, textLanguage: str):
        self.lang = textLanguage
        self.noun = []
        self.verb = []
        self.adj = []
        self.adv = []
        self.cc = []
        self.other = []
        self.text = text
        
        if self.lang == "en":
            pass
        elif self.lang == "pol":
            pass
        else:
            raise ValueError(f"Language is Not Supported '{self.lang}'")
        
    def getPartsOfSpeech(self, text: str):
        words = text.split(" ")
        tags = pos_tag(words)
        
        nouns, vers, conj, adj, adverb, other = [], [], [], [], [], []
        for t in tags:
            if t[1] == "NN" or t[1] == "NNS" or t[1] == "NNP" or t[1] == "NNPS":
                nouns.append(t[0])
            elif t[1] == "VB" or t[1] == "VBD" or t[1] == "VBG" or t[1] == "VBN" or t[1] == "VBP" or t[1] == "VBZ":
                vers.append(t[0])
            elif t[1] == "JJ" or t[1] == "JJR" or t[1] == "JJS":
                adj.append(t[0])
            elif t[1] == "RB" or t[1] == "RBR" or t[1] == "RBS":
                adverb.append(t[0])
            elif t[1] == "CC":
                conj.append(t[0])   
            else:
                other.append(t[0])
                
        self.noun.extend(nouns), self.verb.extend(vers), self.adj.extend(adj), self.adv.extend(adverb), self.cc.extend(conj), self.other.extend(other)
        
    def findPOS(self, POS: str):
        if POS == "Noun":
            return self.noun
        elif POS == "Verb":
            return self.verb
        elif POS == "Adjective":
            return self.adj
        elif POS == "Adverb":
            return self.adv
        elif POS == "Conjunction":
            return self.cc
        elif POS == "Other":
            return self.other
        else:
            raise ValueError(f"POS is Not Supported '{POS}'")
        
    def translate(self, langTo: str = "en"):
        if langTo == "en":
            english = Translator(from_lang=self.lang, to_lang="en")
            return english.translate(self.text)
        else:
            polski = Translator(from_lang=self.lang, to_lang="pl")
            return polski.translate(self.text)