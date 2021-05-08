# importing modules
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

sentence = "Saya Bangga Jadi Warga Nahdlatul Ulama"
words = word_tokenize(sentence)

for w in words:
	print(w, " : ", ps.stem(w))