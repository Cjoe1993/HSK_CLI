import sys
from colorama import Fore, Back, Style
import itertools
import os

options = (
		'一级',
		'二级',
		'三级',
		'四级',
		'五级',
		'六级')


results = []

hsk1 = []
hsk2 = []
hsk3 = []
hsk4 = []
hsk5 = []
hsk6 = []

lists = hsk1,hsk2,hsk3,hsk4,hsk5,hsk6

list1 = hsk1,hsk2


def populate():
	global one,two,three,four,five,six
	
	for line in results:

		try:
			if options[0] in line:
				one = line.replace('（一级）', '')
				hsk1.append(one)

			elif options[1] in line:
				two = line.replace('（二级）', '')
				hsk2.append(two)

			elif options[2] in line:
				three = line.replace('（三级）', '')
				hsk3.append(three)

			elif options[3] in line:
				four = line.replace('（四级）', '')
				hsk4.append(four)

			elif options[4] in line:
				five = line.replace('（五级）', '')
				hsk5.append(five)

			elif options[5] in line:
				six = line.replace('（六级）', '')
				hsk6.append(six)

			else:
				pass


		except:
			pass


def check_character(x):

	with open('hsk/hsk1-6_sorted.txt', 'r') as f:
		lines = f.readlines()

		for line in lines:
			if x in line:
				for option in options:
					if option in line:
						string = (f'{line}'.rstrip())
						results.append(string)
						

						
		
	populate()
	print_algo()





def print_algo():

	print(f'\n\t{Fore.GREEN}{Style.BRIGHT}HSK  1{Style.RESET_ALL}      {Fore.GREEN}{Style.BRIGHT}HSK  2{Style.RESET_ALL}')

	for (a, b) in itertools.zip_longest(hsk1, hsk2, fillvalue=''):
		if len(a) == 0:
			a += "      "
		elif len(a) == 1:
			a += "    "
		elif len(a) == 2:
			a += "  "
		else:
			pass
		print(f'\t{a}      {b}')
	


	print(f'\n\t{Fore.YELLOW}{Style.BRIGHT}HSK  3{Style.RESET_ALL}      {Fore.YELLOW}{Style.BRIGHT}HSK  4{Style.RESET_ALL}')

	for (a, b) in itertools.zip_longest(hsk3, hsk4, fillvalue=''):
		if len(a) == 0:
			a += "      "
		elif len(a) == 1:
			a += "    "
		elif len(a) == 2:
			a += "  "
		else:
			pass
		print(f'\t{a}      {b}')



	print(f'\n\t{Fore.RED}HSK  5{Style.RESET_ALL}      {Fore.RED}{Style.BRIGHT}HSK  6{Style.RESET_ALL}')

	for (a, b) in itertools.zip_longest(hsk5, hsk6, fillvalue=''):
		if len(a) == 0:
			a += "      "
		elif len(a) == 1:
			a += "    "
		elif len(a) == 2:
			a += "  "
		else:
			pass
		print(f'\t{a}      {b}')
		


while True:

	check = input('\nEnter a character, or enter 1 to quit: ')
	check_character(check)
	results = []
	hsk1 = []
	hsk2 = []
	hsk3 = []
	hsk4 = []
	hsk5 = []
	hsk6 = []

	print(f'\n\n\t{Fore.BLUE}{Style.BRIGHT}DEFINITIONS\n\n{Style.RESET_ALL}')

	with open('dictionary/hsk1-6_definitions.txt') as f:
		def_line = f.readlines()
		for line in def_line:
			length_to_check = line[0:5]
			if check in length_to_check:	
				print("\t" + line)

	print(f'\n\n\t{Fore.BLUE}{Style.BRIGHT}------------\n\n{Style.RESET_ALL}')
			
	
	if check == '1':
		break

os.system('clear')
print(Fore.GREEN + '\n再见！')
print(Style.RESET_ALL)
sys.exit()



