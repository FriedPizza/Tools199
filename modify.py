import graph
import Mutation
def checkCharge(x):
	x = str(x)
	if (x == '-1'):
		return '-'
	elif (x == '2'):
		return '0'
	elif (x == '1'):
		return '+'
	else:
		return 'x'

def showRules(PSNP):
	rulestart = 2+((neurons-1)*neurons)
	ruleCount = 1
	ruleStartList = []
	while (True):
		#print ("LoopCount = {}".format(loopCount))
		#print ("newrulestart = {}".format(newrulestart))
		spikeConsumedIndex = rulestart
		neuronContainedIndex = rulestart+1
		firingStatusIndex = rulestart+2
		chargeAcceptedIndex = rulestart+3
		chargeFiredIndex = rulestart+4
		numberOfAcceptingNeuronsIndex = rulestart+5
		#print("neuronContainedIndex: {}".format(neuronContainedIndex))
		currentNode = PSNP[neuronContainedIndex]

		if (rulestart == (len(PSNP)-(2*neurons))):
			break
		else:
			#print ("LenCheck = {}".format((len(PSNP))))
			chargeAccepted = checkCharge(PSNP[chargeAcceptedIndex])
			spikeConsumed = PSNP[spikeConsumedIndex]
			chargeFired = checkCharge(str(PSNP[chargeFiredIndex]))
			neuronContained = PSNP[neuronContainedIndex]
			numberOfAcceptingNeurons = PSNP[numberOfAcceptingNeuronsIndex]

			ruleForm = str(chargeAccepted)+"/a^"+str(spikeConsumed)+"-->a;" + str(chargeFired) + "\n"
			#ruleList[currentNode-1].append(ruleForm)
			ruleEnd = (len(PSNP)-(2*neurons))
			chargeFiredList = PSNP[ruleEnd : ruleEnd + neurons]
			print ("Rule {}: {}".format(ruleCount, ruleForm))
			#print ("\n")

			
			ruleCount+=1
			ruleStartList.append(rulestart)
			rulestart = rulestart + 6
			#loopCount+=1
	return (ruleStartList)




while True:
	try:
		fileName = input("Enter PSNP filename to modify: ")
		fileName = fileName+'.txt'
		File = open(fileName, "r+")
		PerfectPSNP = [int(string) for string in File.readline().replace('\n','').split(' ')]
		Mutation.PrintPSNP(PerfectPSNP)
		break
	except FileNotFoundError:
		print("Enter a valid filename...")


neurons = int(PerfectPSNP[0])
rules = int(PerfectPSNP[1])
rulestart = 2+((neurons-1)*neurons)
#print ("Neurons: {}".format(neurons))
#print ("Rules: {}".format(rules))
#print ("Rule Start: {}".format(rulestart))
loopCount = 1
ruleList = []

finRule = []
newRule = []
option = 0
#add rule: spikesconsumed neuroncontained -1ifnotfired chargeaccepted chargefired spikesfired
while (1):
	print("You choose option {}".format(option))
	#if (option == '1'):

	if (option == '1'):
		print ("Add rule")
		newRule = []
		spikesconsumed = input("Enter spikesconsumed: ")
		neuroncontained = input("Enter neuroncontained: ")
		firingOption = input("Enter firingOption: ")
		chargeaccepted = input("Enter chargeaccepted: ")
		chargefired = input("Enter chargefired: ")
		spikesfired = input("Enter spikesfired: ")
		newRule.append(spikesfired)
		newRule.append(chargefired)
		newRule.append(chargeaccepted)
		newRule.append(firingOption)
		newRule.append(neuroncontained)
		newRule.append(spikesconsumed)
		#print ("before", PerfectPSNP[1])
		PerfectPSNP[1] = str(int(PerfectPSNP[1])+1)

		#print ("after", PerfectPSNP[1])
		#+" "+neuroncontained+" "+firingOption+" "+chargeaccepted+" "+chargefired+" "+spikesfired
		print ("Your new rule is: {}".format(' '.join(newRule)))
		#PerfectPSNP.insert(rulestart,newRule)
		#print
		finRule.append(newRule)
		print ("FinRule: ", finRule)
	elif (option == '2'):
		print ("Remove Rule")
		print("Current Rules")
		ruleStartList = showRules(PerfectPSNP)
		print (ruleStartList)
		removeThis = int(input("Choose rule to remove: "))
		if (0<removeThis<=int(PerfectPSNP[1])):
		#print (PerfectPSNP[int(ruleStartList[removeThis-1]):int(ruleStartList[removeThis-1])+6])
			del PerfectPSNP[int(ruleStartList[removeThis-1]):int(ruleStartList[removeThis-1])+6]
		#print (PerfectPSNP)
		else:
			removeThis = int(input("Something is wrong...\nChoose rule to remove: "))
		PerfectPSNP[1] = str(int(PerfectPSNP[1])-1)
		#showRules(PerfectPSNP)
		print("Removed rule {}".format(removeThis))

	elif (option == '3'):
		if finRule:
			print ("FinRule: ", finRule)
			for x in finRule:
				print (x)
				for y in x:
					#print (y)
					PerfectPSNP.insert(rulestart,y)
			print ("Final PNSP ={}".format(PerfectPSNP))
			outputFile = input("Enter filename: ")
			out = open(outputFile+'.txt', 'w')
			out.write(' '.join(PerfectPSNP))
		else:
			print ("Nothing happened...")
		break
	elif (option == '4'):
		
	elif (option == '5'):
		print ("Graph PSNP")
		while True:
			try: 
				fileName = input("Enter filename: ")
				fileName = fileName+'.txt'
				File = open(fileName, "r")
				PerfectPSNP = [int(integer) for integer in File.readline().replace('\n','').split(' ')]
				print (PerfectPSNP)
				while True:
					try: 
						graph.graphPSNP(PerfectPSNP)
						break
					except Exception:
						print("Close PDF first...")
						enter = input("Press enter to continue...")
				File.close()
				break
			except FileNotFoundError: 
				print ("File not found")
	
	
	print ("#===================#\n# 1->Add Rule       #\n# 2->Remove Rule    #\n# 3->Save and Exit  #\n#===================#")
	option = input("Choose: ")



