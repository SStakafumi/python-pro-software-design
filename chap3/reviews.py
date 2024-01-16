import re

product_review = '''hoge hoge. hoge, hoge. hoge hoge.'''

sentence_pattern = re.compile(r'(.*?\.)(\s|$)', re.DOTALL)
matches = sentence_pattern.findall(product_review)

sentences = [match[0] for match in matches]

word_pattern = re.compile(r"([\w\-']+)([\s,.])?")  # <5>
for sentence in sentences:
    matches = word_pattern.findall(sentence)
    words = [match[0] for match in matches]  # <6>
    print(words)

# 修正--->

def get_matches_for_pattern(pattern, string):
    matches = pattern.findall(string)
    words = [match[0] for match in matches]
    return words

product_review = '''hoge hoge. hoge, hoge. hoge hoge.'''

sentence_pattern = re.compile(r'(.*?\.)(\s|$)', re.DOTALL)
sentences = get_matches_for_pattern(sentence_pattern, product_review) #<2>

word_pattern = re.compile(r"([\w\-']+)([\s,.])?")
for sentence in sentences:
    words = get_matches_for_pattern(word_pattern, sentence)
    print(words)
