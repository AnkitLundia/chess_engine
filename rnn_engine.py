from keras.preprocessing.text import Tokenizer
import nltk

def create_corpus(data):
    corpus = []
    t = Tokenizer(lower=False)
    t.fit_on_texts(data['pgn'])
    sequences = t.texts_to_sequences(data['pgn'])
    print(t.word_index)
    # for i in data['pgn']:
    #     corpus.append(nltk.tokenize.word_tokenize(i, language='english', preserve_line=False))
    # print(len(corpus))
    # print(corpus)
    print(sequences)