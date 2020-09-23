import random, re
scope = 7
knowns = 0
entered_numbers = 0
splitter = ''
known_list = []
possible_list = []
ndate_options = []
tdate_options = []
mdate_options = []
fullDate_options = []
alph = {'a' : '2','b' : '2','c' : '2','d' : '3','e' : '3','f' : '3','g' : '4','h' : '4',\
			'i' : '4','j' : '5','k' : '5','l' : '5','m' : '6','n' : '6','o' : '6','p' : '7',\
            'q' : '7','r' : '7','s' : '7','t' : '8','u' : '8','v' : '8','w' : '9','x' : '9',\
            'y' : '9','z' : '9'}
number_list = []
doorName = raw_input('Enter the name of the door you wish to open for naming purposes. ')
exactNamer = doorName+'_ExactMatches.txt'
allMatcher = doorName+'_AllMatches.txt'
allMatches = open(allMatcher, 'w')
exactDictionaryMatches = open(exactNamer, 'w')
def nameLister():
	names = '.'
	name_list = []
	print("Enter any names/abbreviations that might be used as a combination. Enter to quit and begin entering keypad findings.")
	while names is not '':
		names = raw_input("-> ")
		name_list.append(names.lower())
	for item in name_list:
		numberString = ''
		for letter in item:
			numberString = numberString + alph[letter]
		number_list.append(numberString)
		if item is not '':
			print('Will convert %s to %s' % (item, numberString))
			
def numberGenerator():
	global scope, knowns, entered_numbers, splitter
	finalNumber = ''
	KeyPadOptions = []
	bestOptions = []
	while scope > 6:
		scope = int(raw_input('How many digits will open the lock?\n'))
		digits = raw_input('Enter the known digits\n')
		knowns = len(digits)		
	max_repeats = (scope - knowns)
	magic_number = (knowns +max_repeats)
	print('Will compute all possible %s digit combinations not exceeding %s repetitions of a single digit.' % (magic_number, max_repeats))
	for number in digits:
		finalNumber = (finalNumber + '*' + number)
	stripper = finalNumber.strip(' ')
	splitter = stripper.split('*')
	fails = 0
	randomCombo = ''
	print('Calculating all the possible permutations')
	while fails < 1000000:
		newDigit = str(randomGenerator())
		randomCombo = randomCombo + newDigit
		if len(randomCombo) == scope:
			total = 0
			for digit in digits:
				if digit not in randomCombo:
					randomCombo = ''
					fails+=1
					continue
					if randomCombo.count(digit) > max_repeats:
						fails+=1
						continue
					else:
						total = total + randomCombo.count(digit)
			if randomCombo == '':
				continue
			else:
				#print('\nThe final combo is %s \nThe magic number is %s\n'%(randomCombo, total))	
				if randomCombo not in possible_list:
					possible_list.append(randomCombo)
			randomCombo = ''	
		else:
			fails+=1
	print("There were %s permutations calculated." % len(possible_list))
	
	
	
	
def comboPrinter():
	exactDictionaryMatches = open(exactNamer, 'w')
	for possible in possible_list:
		dictionaryChecker(possible)
		if possible in number_list:
			print('\n\n*$*$*Special Alert*$*$*\nThis combination was identified during fingerprinting!!!\n%s\n*$*$*Special Alert*$*$*\n'% possible)
		if re.search('[\d][123][01]\d{2}', possible):
			fullDate = possible + '     Full date found'	
			fullDate_options.append(fullDate)		
		if re.search('19[\d]{2}', possible):
			ndate = possible + '     1900-1999 found'
			ndate_options.append(ndate)
			continue
		if re.search('200\d', possible):
			tdate = possible + '     2000-2009 found'
			tdate_options.append(tdate)
			continue
		if re.search('20[12]\d', possible):
			ttdate = possible + '     2010-2029 found'
			tdate_options.append(ttdate)			
			continue
		if re.search('[01][012][123][\d]', possible):
			mdate = possible + '     Month and date found'
			mdate_options.append(mdate)	
			continue	
		if '2580' in possible or '5683' in possible:
			print('************************************\nMost common combo! try %s\n************************************\n' % possible)			
		#work
		if '9675' in possible or '9075' in possible:
			print('************************************\nWork! Special instance try %s\n************************************\n' % possible)			
		#boss
		if '2677' in possible or '2077' in possible:
			print('************************************\nBoss! Special instance try %s\n************************************\n' % possible)			
		#door
		if '3007' in possible or '3667' in possible:
			print('************************************\nDoor! Special instance try %s\n************************************\n' % possible)			
		#open
		if '0736' in possible or '6736' in possible:
			print('************************************\nOpen! Special instance try %s\n************************************\n' % possible)			
		#lock
		if '5625' in possible or '5025' in possible:
			print('************************************\nLock! Special instance try %s\n************************************\n' % possible)			
		#store
		if '78673' in possible or '78073' in possible:
			print('************************************\nStore! Special instance try %s\n************************************\n' % possible)			
		#access
		if '222377' in possible or '422355' in possible or '422377' in possible:
			print('************************************\nAccess! Special instance try %s\n************************************\n' % possible)			
		#unlock
		if '865625' in possible or '865025' in possible:
			print('************************************\nUnlock! Special instance try %s\n************************************\n' % possible)			
		#secure
		if '865625' in possible or '865025' in possible:
			print('************************************\nSecure! Special instance try %s\n************************************\n' % possible)			
		#keypad
		if '539723' in possible or '539743' in possible:
			print('************************************\nKeypad! Special instance try %s\n************************************\n' % possible)			
		#entry
		if '36879' in possible:
			print('************************************\nEntry! Special instance try %s\n************************************\n' % possible)			
		#exit
		if '3948' in possible or '3918' in possible:
			print('************************************\nExit! Special instance try %s\n************************************\n' % possible)			
		#admin
		if '23646' in possible or '43646' in possible:
			print('************************************\nAdmin! Special instance try %s\n************************************\n' % possible)			
		#staff
		if '78233' in possible or '58455' in possible:
			print('************************************\nStaff! Special instance try %s\n************************************\n' % possible)			
		#nurse
		if '68773' in possible:
			print('************************************\nNurse! Special instance try %s\n************************************\n' % possible)			
		#manage
		if '626243' in possible or '646443' in possible:
			print('************************************\nManage! Special instance try %s\n************************************\n' % possible)			
		#enter
		if '36837' in possible:
			print('************************************\nEnter! Special instance try %s\n************************************\n' % possible)			
	print('************Full Date Options************')
	for fulldates in fullDate_options:
		print(fulldates)
	print('******************************************')	
	print('************20th Century Date Options************')
	for ndates in ndate_options:
		print(ndates)
	print('******************************************')
	print('************21st Century Date Options************')
	for tdates in tdate_options:
		print(tdates)
	print('******************************************')	
	print('************Other Options Below************')
	for best in mdate_options:
		print(best)
	print('******************************************')
	allMatches.write('************All combos follow ************\n\n')
	for all in possible_list:
		allMatches.write(all+'\n')
	allMatches.write('******************************************')
		
def randomGenerator():
	global splitter, knowns
	randomDigit = splitter[random.randint(0, knowns)]
	return str(randomDigit)

def dictionaryChecker(possible):
	exactDictionaryMatches = open(exactNamer, 'a')
	telDic = open('TelDictionary.txt', 'r')
	short = possible[:(len(possible)-1)]
	for line in telDic:
		cracked = line.split('=')
		if int(possible) == int(cracked[0]):
			print(line.strip('\n'))
			exactDictionaryMatches.write(line.strip('\n')+'\n')
	telDic.close()
	
nameLister()
numberGenerator()
comboPrinter()

	

