from pathlib import Path
from pipeline import Pipeline
from visualize import visualize


def process_all_texts():
    dict_full = {'person1': 0, 'person2': 0, 'comparative': 0, 'superlative': 0, 'numbers': 0}
    path = Path(__file__).parent / 'tmp'
    for file in path.glob('*'):
        with open(file, encoding="utf-8", errors='ignore') as f:
            text = f.read()
            text = Pipeline(text)
            text.get_cleaned()
            dict = text.get_tags()
            for i in dict:
                if dict[i] > 0:
                    dict_full[i] += 1
    for i in dict_full:
        dict_full[i] = dict_full[i] / 100
    visualize(dict_full, path)
    
