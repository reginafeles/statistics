import pymorphy2
import re
from constants import tags, pronouns, adverbs


class Pipeline:

    def __init__(self, text):
        self.text = text
        self.tags_dict = {'pron1sg': 0, 'pron1pl': 0, 'pron2sg': 0, 'pron2pl': 0, 'comparative': 0, 'superlative': 0, 'numbers': 0, 'imperative': 0}
        self.adverbs_dict = {'comfortable': 0, 'real': 0, 'surely': 0, 'free': 0, 'profitably': 0, 'absolutely': 0, 'very': 0}
        self.tags = tags
        self.adverbs = adverbs

    def get_cleaned(self):

        text = re.sub(r'[.,:;«»()!—?\'\"]', '', self.text)
        self.text = text.split(' ')

        return self.text

    def get_numbers(self):

        for word in self.text:
            if re.search('[0-9]+', word):
                self.tags_dict['numbers'] += 1
    def get_pron(self):

        morph = pymorphy2.MorphAnalyzer()
        for word in self.text:
            parsed = morph.parse(word)[0].tag
            for pron in pronouns:
                if pron[1] in parsed and pron[2] in parsed and pron[3] in parsed:
                    self.tags_dict[pron[0]] += 1

    def get_tags(self):

        morph = pymorphy2.MorphAnalyzer()
        for word in self.text:
            for aim in self.tags:
                for tag in aim:
                    try:
                        if tag in morph.parse(word)[0].tag:
                            self.tags_dict[aim[0]] += 1
                    except:
                        continue
        self.get_pron()
        self.get_numbers()
        return self.tags_dict

    def get_adverbs(self):

        for word in self.text:
            for aim in self.adverbs:
                for adverb in aim:
                    if adverb in word:
                        self.adverbs_dict[aim[0]] += 1
        return self.adverbs_dict

    def get_freq(self):
        self.get_tags()
        self.get_adverbs()
