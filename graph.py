from graphviz import Digraph
import traceback
import unicodedata

graphNum = 1

def checkCharge(x):
	x = str(x)
	if (x == '-1'):
		return '-'
	elif (x == '2'):
		return '0'
	elif (x == '1'):
		return '+'
	else:
		return x



def graphPSNP (PSNP, graphLabel, graphDirectory):
	global graphNum
	global chargeFiredList
	graphName = 'psnp'+ str(graphNum)
	ps = Digraph(name=graphName, filename=graphLabel, format='png', engine='dot', encoding='utf-8', directory=graphDirectory)
	ps.attr('node',shape='circle')
	f = PSNP
	neurons = int(f[0])
	rules = int(f[1])
	rulestart = 2+((neurons-1)*neurons)
	newrulestart = rulestart
	loopCount = 1
	ruleList = []
	for x in range (0,neurons):
		ruleList.append([])
	rulenumber = 1

	

	while (True):
		spikeConsumedIndex = newrulestart
		neuronContainedIndex = newrulestart+1
		firingStatusIndex = newrulestart+2
		chargeAcceptedIndex = newrulestart+3
		chargeFiredIndex = newrulestart+4
		numberOfAcceptingNeuronsIndex = newrulestart+5
		currentNode = f[neuronContainedIndex]
		nextNodeIndex = neuronContainedIndex+6

		if (newrulestart == (len(f)-(2*neurons))):
			break
		else:
			#print ("LenCheck = {}".format((len(f))))
			chargeAccepted = checkCharge(f[chargeAcceptedIndex])
			spikeConsumed = f[spikeConsumedIndex]
			chargeFired = checkCharge(str(f[chargeFiredIndex]))
			neuronContained = f[neuronContainedIndex]
			numberOfAcceptingNeurons = f[numberOfAcceptingNeuronsIndex]
			#if (spikeConsumed==neurons):
			#	ruleForm = 'RuleRemoved'
			#else:	
			if (str(numberOfAcceptingNeurons)=='1'):
				spikeOut = 'a'
			else:
				spikeOut = unicodedata.lookup("GREEK SMALL LETTER LAMDA")
			ruleForm = str(chargeAccepted)+"/a^"+str(spikeConsumed)+"-->"+spikeOut+';' + str(chargeFired) + "\n"
			ruleList[currentNode-1].append(ruleForm)
			ruleEnd = (len(f)-(2*neurons))
			chargeFiredList = f[ruleEnd : ruleEnd + neurons]


			rulenumber+=1
			#prevNode = currentNode
			#prevRule=ruleForm
			newrulestart = newrulestart + 6
			loopCount+=1

	rulestart = 2+((rules-1)*neurons)
	newrulestart = rulestart

	for x in range (0,neurons-1):
		try:
 			ps.node(str(x+1),''.join(ruleList[x]), xlabel=str(x+1)+','+checkCharge(str(chargeFiredList[x])))
		except Exception:
			error_msg = traceback.format_exc()
			print (error_msg)
			print ("chargeFiredList: ", chargeFiredList)
			input("Something happened...")

 	################
	readStart = 2
	nodeNumber = 1
	while (nodeNumber<neurons):
		for i in range (0, neurons):
			if (f[readStart+i]==1):
				if (i+1==neurons):
					ps.edge(str(nodeNumber), 'out')
				else:	
					ps.edge(str(nodeNumber), str(i+1))
		readStart = readStart+neurons
		nodeNumber += 1

	inputIndex = (len(f)-(neurons))
	for i in range(0,neurons):
		if (f[inputIndex]!=0):
			ps.node('int'+str(i),'input')
			ps.edge('int'+str(i),str(f[inputIndex]))
			inputIndex+=1

	###############

	ps.render(cleanup=True)
