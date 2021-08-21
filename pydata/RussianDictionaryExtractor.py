import csv
import json

# SHARED Constants
BARE = 0
ACCENTED = 1
ENGLISH = 2
GERMAN = 3

# NOUN Constants
GENDER = 4
PARTNER = 5
ANIMATE = 6
INDECLINABLE = 7
SINGULAR_ONLY = 8
PLURAL_ONLY = 9
SG_NOM = 10
SG_GEN = 11
SG_DAT = 12
SG_ACC = 13
SG_INST = 14
SG_PREP = 15
PL_NOM = 16
PL_GEN = 17
PL_DAT = 18
PL_ACC = 19
PL_INST = 20
PL_PREP = 21

COMPARATIVE = 4
SUPERLATIVE = 5
SHORT_M = 6
SHORT_F = 7
SHORT_N = 8
SHORT_PL = 9
DECL_M_NOM = 10
DECL_M_GEN = 11
DECL_M_DAT = 12
DECL_M_ACC = 13
DECL_M_INST = 14
DECL_M_PREP = 15
DECL_F_NOM = 16
DECL_F_GEN = 17
DECL_F_DAT = 18
DECL_F_ACC = 19
DECL_F_INST = 20
DECL_F_PREP = 21
DECL_N_NOM = 22
DECL_N_GEN = 23
DECL_N_DAT = 24
DECL_N_ACC = 25
DECL_N_INST = 26
DECL_N_PREP = 27
DECL_PL_NOM = 28
DECL_PL_GEN = 29
DECL_PL_DAT = 30
DECL_PL_ACC = 31
DECL_PL_INST = 32
DECL_PL_PREP = 33


def check_if_exists(row, index):
    if index >= len(row):
        return ''
    return row[index]


def extract_adjectives():
    def extract_from_row(item):
        return {
            check_if_exists(item, ENGLISH): {
                'bare': check_if_exists(item, BARE),
                'accented': check_if_exists(item, ACCENTED),
                'comparative': check_if_exists(item, COMPARATIVE),
                'superlative': check_if_exists(item, SUPERLATIVE),
                'short': {
                    'masculine': check_if_exists(item, SHORT_M),
                    'feminine': check_if_exists(item, SHORT_F),
                    'neuter': check_if_exists(item, SHORT_N),
                    'plural': check_if_exists(item, SHORT_PL),
                },
                'singular': {
                    'masculine': {
                        'nominative': check_if_exists(item, DECL_M_NOM),
                        'genitive': check_if_exists(item, DECL_M_GEN),
                        'dative': check_if_exists(item, DECL_M_DAT),
                        'accusative': check_if_exists(item, DECL_M_ACC),
                        'instrumental': check_if_exists(item, DECL_M_INST),
                        'prepositional': check_if_exists(item, DECL_M_PREP)
                    },
                    'feminine': {
                        'nominative': check_if_exists(item, DECL_F_NOM),
                        'genitive': check_if_exists(item, DECL_F_GEN),
                        'dative': check_if_exists(item, DECL_F_DAT),
                        'accusative': check_if_exists(item, DECL_F_ACC),
                        'instrumental': check_if_exists(item, DECL_F_INST),
                        'prepositional': check_if_exists(item, DECL_F_PREP)
                    },
                    'neuter': {
                        'nominative': check_if_exists(item, DECL_N_NOM),
                        'genitive': check_if_exists(item, DECL_N_GEN),
                        'dative': check_if_exists(item, DECL_N_DAT),
                        'accusative': check_if_exists(item, DECL_N_ACC),
                        'instrumental': check_if_exists(item, DECL_N_INST),
                        'prepositional': check_if_exists(item, DECL_N_PREP)
                    },
                },
                'plural': {
                    'nominative': check_if_exists(item, DECL_PL_NOM),
                    'genitive': check_if_exists(item, DECL_PL_GEN),
                    'dative': check_if_exists(item, DECL_PL_DAT),
                    'accusative': check_if_exists(item, DECL_PL_ACC),
                    'instrumental': check_if_exists(item, DECL_PL_INST),
                    'prepositional': check_if_exists(item, DECL_PL_PREP),
                }
            }
        }

    json_to_write = []

    with open('russian-dictionary/adjectives.csv', newline='', encoding='utf-8') as adjectives:
        reader_adjectives = csv.reader(adjectives, delimiter=';', quotechar='\'')
        headers_adjectives = next(reader_adjectives)
        print(headers_adjectives)

        # Here, the magic happens
        for row in reader_adjectives:
            print("Extracting Noun {0} from file".format(row[BARE]))
            json_to_write.append(extract_from_row(row))

    with open('data/adjectives.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(json_to_write, jsonfile, indent=2, ensure_ascii=False)


def extract_nouns():
    def extract_from_row(item):
        return {
            check_if_exists(item, ENGLISH): {
                'bare': check_if_exists(item, BARE),
                'accented': check_if_exists(item, ACCENTED),
                'gender': check_if_exists(item, GENDER),
                'partner': check_if_exists(item, PARTNER),
                'accented': check_if_exists(item, ACCENTED),
                'animate': 'yes' if check_if_exists(item, ANIMATE) == '0' else 'no',
                'indeclinable': 'yes' if check_if_exists(item, INDECLINABLE) else 'no',
                'singular': {
                    'nominative': check_if_exists(item, SG_NOM),
                    'genitive': check_if_exists(item, SG_GEN),
                    'dative': check_if_exists(item, SG_DAT),
                    'accusative': check_if_exists(item, SG_ACC),
                    'instrumental': check_if_exists(item, SG_INST),
                    'prepositional': check_if_exists(item, SG_PREP),
                },
                'plural': {
                    'nominative': check_if_exists(item, PL_NOM),
                    'genitive': check_if_exists(item, PL_GEN),
                    'dative': check_if_exists(item, PL_DAT),
                    'accusative': check_if_exists(item, PL_ACC),
                    'instrumental': check_if_exists(item, PL_INST),
                    'prepositional': check_if_exists(item, PL_PREP),
                }
            }
        }

    json_to_write = []

    with open('russian-dictionary/nouns.csv', newline='', encoding='utf-8') as nouns:
        reader_nouns = csv.reader(nouns, delimiter=';')
        headers_nouns = next(reader_nouns)
        print(headers_nouns)

        # Here, the magic happens
        for row in reader_nouns:
            print("Extracting Noun {0} from file".format(row[BARE]))
            json_to_write.append(extract_from_row(row))

    with open('data/nouns.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(json_to_write, jsonfile, indent=2, ensure_ascii=False)