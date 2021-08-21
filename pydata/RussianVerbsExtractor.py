import csv
import json

# Constants
RANK_GL = 0
RANK_RU = 1
LEVEL = 2
ENGLISH = 3
FRENCH = 4
INFINITIVE = 5
DETAILS = 6
COLLOQUIAL = 7
IRREGULAR = 8
GROUP = 9
CONJUGATION_SUFFIX = 10
PERFECTIVE = 11
COUPLED_ASPECT = 12
RETURNABLE = 13
VALID = 14
FIRST_PERSON_SINGULAR = 15
SECOND_PERSON_SINGULAR = 16
THIRD_PERSON_SINGULAR = 17
FIRST_PERSON_PLURAL = 18
SECOND_PERSON_PLURAL = 19
THIRD_PERSON_PLURAL = 20
IMPERATIVE_SINGULAR = 21
IMPERATIVE_PLURAL = 22
PRESENT_ADVERBIAL_PARTICIPLE = 23
PAST_ADVERBIAL_PARTICIPLE = 24
PRESENT_ACTIVE_PARTICIPLE = 25
PAST_ACTIVE_PARTICIPLE = 26
PRESENT_PASSIVE_PARTICIPLE = 27
PAST_PASSIVE_PARTICIPLE = 28
UNKNOWN_1 = 29
UNKNOWN_2 = 30

# For the second CSV to get the past tenses
VERBS_INFINITIVE = 0
PAST_M = 8
PAST_F = 9
PAST_N = 10
PAST_PL = 11


def extract():
    def extract_from_row(item):
        return {
            item[INFINITIVE]: {
                'infinitive': item[INFINITIVE],
                'english': item[ENGLISH],
                "coupled_aspect": item[COUPLED_ASPECT].replace(item[INFINITIVE], '').replace('/', ''),
                "perfective": 'perfective' if item[PERFECTIVE] == 'совер.' else 'imperfective',
                "group": item[GROUP],
                'imperative': {
                    'singular': item[IMPERATIVE_SINGULAR],
                    'plural': item[IMPERATIVE_PLURAL],
                },
                'participles': {
                    'present': {
                        'active': item[PRESENT_ACTIVE_PARTICIPLE],
                        'passive': item[PRESENT_PASSIVE_PARTICIPLE],
                        'adverbial': item[PRESENT_ADVERBIAL_PARTICIPLE],
                    },
                    'past': {
                        'active': item[PAST_ACTIVE_PARTICIPLE],
                        'passive': item[PAST_PASSIVE_PARTICIPLE],
                        'adverbial': item[PAST_ADVERBIAL_PARTICIPLE],
                    }
                },
                'present': {
                    'singular': {
                        'first': item[FIRST_PERSON_SINGULAR],
                        'second': item[SECOND_PERSON_SINGULAR],
                        'third': item[THIRD_PERSON_SINGULAR]
                    },
                    'plural': {
                        'first': item[FIRST_PERSON_PLURAL],
                        'second': item[SECOND_PERSON_PLURAL],
                        'third': item[THIRD_PERSON_PLURAL]
                    }
                },
                'past': {
                    'masculine': '',
                    'feminine': '',
                    'neuter': '',
                    'plural': '',
                }
            }
        }

    print("Running against RussianVerbs.csv...")

    json_to_write = {}

    # Initial Verbs
    with open('russian-dictionary/RussianVerbs.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')

        headers = next(reader)
        # Here, the magic happens
        for row in reader:
            print("Extracting Verb {0} from file".format(row[INFINITIVE]))
            data = extract_from_row(row)
            json_to_write[row[INFINITIVE]] = data[row[INFINITIVE]]

    # Inexplicably, the past tense is absent from the above CSV.
    # This concerns irregular verbs like 'идти' whose past tense is 'шёл', 'шла', 'шло', 'шли'.

    with open('russian-dictionary/verbs.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        headers = next(reader)

        # Here, the magic happens
        for row in reader:

            if row[VERBS_INFINITIVE] in json_to_write:
                print('Inserting past tense of {0}'.format(row[0]))
                json_to_write[row[0]]['past']['masculine'] = row[PAST_M] if len(row) - 1 > PAST_M else ''
                json_to_write[row[0]]['past']['feminine'] = row[PAST_F] if len(row) - 1 > PAST_F else ''
                json_to_write[row[0]]['past']['neuter'] = row[PAST_N] if len(row) - 1 > PAST_N else ''
                json_to_write[row[0]]['past']['plural'] = row[PAST_PL] if len(row) - 1 > PAST_PL else ''
            else:
                print('ERROR: {0} is missing from the list!'.format(row[0]))

    # Write to the JSON file
    with open('../data/verbs.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(json_to_write, jsonfile, indent=2, ensure_ascii=False)
