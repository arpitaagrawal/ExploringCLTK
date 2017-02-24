from cltk.corpus.utils.importer import CorpusImporter
from cltk.tokenize.indian_tokenizer import indian_punctuation_tokenize_regex as i_word
from cltk.stem.sanskrit.indian_syllabifier import Syllabifier
import os
import numpy as np

__author__ = 'Arpita Agrawal'

corpus_importer = CorpusImporter('sanskrit')
print(corpus_importer.list_corpora)

root = os.path.expanduser('~')
hindi_corpus = os.path.join(root,'cltk_data/hindi/text/hindi_text_ltrc')
hindi_text_path = os.path.join(hindi_corpus, 'miscellaneous/gandhi/main.txt')
hindi_text = open(hindi_text_path,'r').read()


hindi_text_tokenize = i_word(hindi_text)

print("first 10 words : ", hindi_text_tokenize[0:20], "\n\n")
print("number of words in the text", len(hindi_text_tokenize))

# Lexical Diversity

lexical_diversity = len(np.unique(hindi_text_tokenize))/ len(hindi_text_tokenize)
print("Lexical Diversity of the text ::", lexical_diversity)


# Using indian_syllabifier

word = hindi_text_tokenize[3]
x = Syllabifier('hindi')
syllabified_output = x.orthographic_syllabify(word)


print(syllabified_output)
