from pathlib import Path
from pipeline import Pipeline
from visualize import visualize


def process_all_texts():
    tags_stat_dict = {'pron1sg': 0, 'pron1pl': 0, 'pron2sg': 0, 'pron2pl': 0, 'comparative': 0, 'superlative': 0, 'numbers': 0, 'imperative': 0}
    adverbs_stat_dict = {'comfortable': 0, 'real': 0, 'surely': 0, 'free': 0, 'profitably': 0, 'absolutely': 0, 'very': 0}
    path = Path(__file__).parent / 'tmp'
    for file in path.glob('*'):
        with open(file, encoding="utf-8", errors='ignore') as f:
            text = f.read()
            text = Pipeline(text)
            text.get_cleaned()
            dict_tag = text.get_tags()
            adv_dict = text.get_adverbs()
            for i in dict_tag:
                if dict_tag[i] > 0:
                    tags_stat_dict[i] += 1
            for i in adv_dict:
                if adv_dict[i] > 0:
                    adverbs_stat_dict[i] += 1

    for i in tags_stat_dict:
        tags_stat_dict[i] = tags_stat_dict[i] / 100
    for i in adverbs_stat_dict:
        adverbs_stat_dict[i] = adverbs_stat_dict[i] / 100

    print(tags_stat_dict)
    print(adverbs_stat_dict)
    visualize(tags_stat_dict, path, 'statistics_tags.png')
    visualize(adverbs_stat_dict, path, 'statistics_adv.png')
