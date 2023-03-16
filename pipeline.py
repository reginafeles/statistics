import pymorphy2
import re


class Pipeline:

    def __init__(self, text):
        self.text = text
        self.person1 = ['person1', '1per']
        self.person2 = ['person2', '2per']
        self.comparative = ['comparative', 'COMP']
        self.superlative = ['superlative', 'Supr']
        self.tags_dict = {'person1': 0, 'person2': 0, 'comparative': 0, 'superlative': 0, 'numbers': 0}
        self.aims = [self.person1, self.person2, self.comparative, self.superlative]

    def get_cleaned(self):

        text = re.sub(r'[.,:;«»()!—?\'\"]', '', self.text)
        self.text = text.split(' ')

        return self.text

    def get_tags(self):

        morph = pymorphy2.MorphAnalyzer()
        for word in self.text:
            for aim in self.aims:
                for i in aim:
                    try:
                        if i in morph.parse(word)[0].tag:
                            self.tags_dict[aim[0]] += 1
                    except:
                        continue
                    if re.search('[0-9]+', word):
                        self.tags_dict['numbers'] += 1

        return self.tags_dict
