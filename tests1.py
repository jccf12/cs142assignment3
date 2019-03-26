import threading 
from Parser1 import Parser1
from TranslatorTelugu import TranslatorTelugu
import random

print('\n______Testing Parser1 and Translator______\n')

terminals = ['<play>', '<jump>', '<eat>', '<kick>','<tell>','<cool>','<tall>','<blue>', '<tough>', '<ugly>', '<guy>', '<rabbit>', '<Wes>', '<table>', '<pen>',
                 '<bike>', '<door>', '<drink>', '<football>', '<riding>', '<I>', '<you>', '<he>', '<she>', '<they>', '<it>']

verbs = ['<play>', '<jump>', '<eat>', '<kick>','<tell>']
adjs = ['<cool>','<tall>','<blue>', '<tough>', '<ugly>','']
nouns = ['<guy>', '<rabbit>', '<Wes>', '<table>', '<pen>',
                 '<bike>', '<door>', '<drink>', '<football>', '<riding>']
pronouns = ['<I>', '<you>', '<he>', '<she>', '<they>', '<it>']

print("Strings that are part of the language:")
print('')

for x in range(5):
	a1 = random.choice(adjs)
	a2 = random.choice(adjs)
	n1 = random.choice(nouns)
	n2 = random.choice(nouns)
	p1 = random.choice(pronouns)
	p2 = random.choice(pronouns)
	v = random.choice(verbs)
	s = a1+random.choice([n1,p1])+v+a2+random.choice([n2,p2])
	TranslatorTelugu(s)
	print('')

print("Strings that are NOT part of the language:")
print('')

for s in ['<play><blue><football>','<I<kick><tall><riding>','<it><cool><eat><riding>','I><play><drink>','<she>']:
	TranslatorTelugu(s)

