from RussianVerbsExtractor import extract
from RussianDictionaryExtractor import extract_nouns, extract_adjectives

# Run all - comment out stuff you don't need
if __name__ == '__main__':
    extract_nouns()
    extract_adjectives()
    extract()

