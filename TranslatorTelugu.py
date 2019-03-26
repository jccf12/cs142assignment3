import threading
from Parser1 import Parser1
from googletrans import Translator

translator = Translator()
def translateword(sentence):
	return translator.translate(sentence,dest='te').text

def TranslatorTelugu(w):
	if Parser1(w):
		words = w.split('<')
		words = words[1:]
		sentence = ''
		for word in words:
			sentence+=word[:-1]+' '
		print('Original sentence:', sentence)
		print('Translation to Telugu:', translateword(sentence))


	