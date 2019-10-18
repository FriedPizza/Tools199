import random
#import graph


def ObtainRuleIndex (PSNP, Rule): #Jules made this function but forgot what he was supposed to use it for

	#print("Initialize ObtainRuleIndex function.")

	neurons = PSNP[0]
	rules = PSNP[1]

	index = 2 + neurons
	for j in range(1, Rule):
		index = index + 5
		index = index + PSNP[index] + 1

	return index

	#print("Terminate ObtainRuleIndex function.\n")



def PrintPSNP (PSNP): #Prints the PSNP in a neat format

	#print("")

	neurons = PSNP[0]
	rules = PSNP[1]

	#print("Neurons: {}".format(neurons))
	#print("Rules: {}".format(rules))

	for x in range(0, neurons - 1): #Prints the synapses of each neuron
		print("Synapse {}: {}".format(x + 1, PSNP[2 + (x * neurons) : 2 + ((x + 1) * neurons)]))

	index = 2 + ((neurons - 1) * neurons)
	for y in range(0, rules): #Prints each rule
		#print("Rule {}: {}".format(y, PSNP[index : index + 6]))
		index = index + 6

	#print("ChargeVector: {}".format(PSNP[-neurons - neurons : -neurons]))
	#print("InputNode: {}".format(PSNP[-neurons : ]))
	#print("\n")



def SynapseExist (PSNP, node1, node2): #Checks if a synapse from one node to another exists

	neurons = PSNP[0]
	rules = PSNP[1]

	#print("Nodes are {} and {}".format(node1, node2))

	index = 2
	for x in range(1, node1): #Traverses the PSNP to the first node
		index = index + neurons
	index = index + node2 - 1 #Finds the index of the second node
	if(PSNP[index] == 1): #Check if the synapse exist between the two nodes
		#print("Synapse exists from node {} to node {}".format(node1, node2))
		return True

	#print("Synapse doesn't exist from node {} to node {}".format(node1, node2))
	return False



def AllSynapseExist (PSNP): #Checks if all possible synapses exist already

	#print("Initialize AllSynapseExist function.")

	neurons = PSNP[0]
	rules = PSNP[1]

	for x in range(1, rules): #Check all possible combination of neurons if there is a synapse between them
		for y in range(1, rules):
			if (x != y): #Except when the source and the destination of the synapse is the same
				if (SynapseExist(PSNP, x, y) == False):
					#print("Terminate AllSynapseExist function.\n")
					return False #A synapse doesn't exist, so not all synapses exist

	#print("Terminate AllSynapseExist function.\n")
	return True




def SynapseCheck (PSNP, node): #Returns a list of nodes that the given node is connected to (not connected with)

	#print("Initialize SynapseCheck function.")

	neurons = PSNP[0]
	rules = PSNP[1]
	Synapses = []

	index = 2
	for x in range(1, node): #Traverse the PSNP to the indicated node
		index = index + neurons 
	for y in range(1, neurons + 1): #Gets the synapses configuration from all the nodes and put it in the Synapses list
		if(PSNP[index] == 1):
			Synapses.append(y)
		index = index + 1

	#print("Terminate SynapseCheck function.\n")

	return Synapses



def SynapseEdit (PSNP, node1, node2, Edit): #Adds or Removes a synapse

	#print("Initialize SynapseEdit function.")

	neurons = PSNP[0]
	rules = PSNP[1]

	index = 2
	for x in range(1, node1): #Traverses the PSNP to the first node
		index = index + neurons
	for y in range(1, node2): #Traverses the synapse configuration of the first node to the second node
		index = index + 1
	if(Edit == "Add"):
		PSNP[index] = 1
	else:
		PSNP[index] = 0
		#if(PathCheck(PSNP) == False):
		#	PSNP[index] = 1

		#	print("Terminate Failed SynapseEdit function.\n")
		#	return False

	#print("Terminate SynapseEdit function.\n")
	return True



def SynapseSwap (PSNP1, PSNP2, node1, node2): #Swaps synapses of the two nodes

	#print("Initialize SynapseSwap function.")

	PSNP1dummy = PSNP1[:]
	PSNP2dummy = PSNP2[:]

	node1synapses = SynapseCheck(PSNP1dummy, node1) #Get the synapses of the first node
	node2synapses = SynapseCheck(PSNP2dummy, node2) #And the second node

	#print("Node 1 synapses: {}".format(node1synapses))
	#print("Node 2 synapses: {}".format(node2synapses))

	for synapse in node1synapses:
		SynapseEdit(PSNP1dummy, node1, synapse, "Remove")
	for synapse in node2synapses:
		SynapseEdit(PSNP2dummy, node2, synapse, "Remove")
	for synapse in node2synapses:
		SynapseEdit(PSNP1dummy, node2, synapse, "Add")
	for synapse in node1synapses:
		SynapseEdit(PSNP2dummy, node1, synapse, "Add")
	
	if(PathCheck(PSNP1) == True and PathCheck(PSNP2) == True):
		PSNP1 = PSNP1dummy
		PSNP2 = PSNP2dummy
		#print("Terminate SynapseSwap function.\n")
		return True

	return False
	#print("Terminate Failed SynapseSwap function.\n")



def PathCheck (PSNP): #Checks if a path from either inputs to the output exist

	#print("Initialize PathCheck function.")

	neurons = PSNP[0]
	rules = PSNP[1]
	checkedinputs = 0

	for index in range(1, neurons + 1): #Traverse the PSNP backwards from the last element
		if(PSNP[-index] == 1): 
			inputnode1 = neurons + 1 - index #Gets the neuron number since the index is inverse
		if(PSNP[-index] == 2):
			inputnode2 = neurons + 1 - index #Gets the neuron number since the index is inverse

	path = [inputnode1] #Start with the first input node
	for node in path:
		connectednodes = SynapseCheck(PSNP, node) #Get the nodes connected
		for connectednode in connectednodes: #For each node that it's connected to:
			if(connectednode not in path): #Add it to the list of nodes to traverse (without repetition)
				path.append(connectednode)
		if(neurons in path): 
			checkedinputs += 1 #Mark if the output is found in the path
			break

	path = [inputnode2] #Same process applies to the second input node
	for node in path:
		connectednodes = SynapseCheck(PSNP, node)
		for connectednode in connectednodes:
			if(connectednode not in path):
				path.append(connectednode)
		if(neurons in path):
			checkedinputs += 1
			break

	#print("Terminate PathCheck function.\n")
	if(checkedinputs == 2): 
		return True #Both outputs are found in the path
	else:
		return False




def RuleCheck (PSNP, node): #Checks a node and returns the charges accepted by each rule

	#print("\nInitialize RuleCheck function.")

	neurons = PSNP[0]
	rules = PSNP[1]
	containedrules = []


	index = 2 + ((neurons - 1) * neurons) #Traverses to the first rule of the PSNP
	for x in range(1, rules + 1):
		rule = []
		if (PSNP[index] != -2):
			spikesconsumed = PSNP[index]
			containednode = PSNP[index + 1]
			chargeaccepted = PSNP[index + 3]
			chargefired = PSNP[index + 4]
			spikesfired = PSNP[index + 5]
			if(containednode == node):
				#if(chargeaccepted in containedrules):
				#	print("		RuleCheck: non-determinism by accepting charge {} with rules accepting charge/s {}.\n".format(chargeaccepted, containedrules))
				#	return [] #put this code back when non-determinism is implemented
				rule.append(spikesconsumed)
				rule.append(chargeaccepted)
				rule.append(chargefired)
				rule.append(spikesfired)
				containedrules.append(rule)
				#else:
				#	containedrules.append(chargeaccepted)
		index = index + 6 #Jump to the next rule

	#if(len(containedrules) >= 3):
	#	print("		RuleCheck: node {} contains {} rules.\n".format(node, containedrules))
	#	return []
	#else:
	#	print("Terminate RuleCheck function.")
	return containedrules



def RuleAdd (PSNP, spikesconsumed, node, chargeaccepted, chargefired, forgetting):

	#print("Initialize RuleAdd function.")

	#print("Adding rule to node {} with accepting charge {}".format(node, chargeaccepted))

	neurons = PSNP[0]
	rules = PSNP[1]

	#synapses = SynapseCheck(PSNP, node)

	index = 2 + ((neurons - 1) * neurons)
	#print ("Start index: {}".format(index))
	PSNP.insert(index, spikesconsumed)
	index += 1
	PSNP.insert(index, node)
	index += 1
	PSNP.insert(index, 1)
	index += 1
	PSNP.insert(index, chargeaccepted)
	index += 1
	PSNP.insert(index, chargefired)

	index += 1
	if(forgetting):
		PSNP.insert(index, 0)
	else:
		PSNP.insert(index, 1)
	
	PSNP[1] += 1

	#print("Terminate RuleAdd function.\n")



def RuleRemove (PSNP, spikesconsumed, node, chargeaccepted, chargefired, spikesfired): #Removes a rule with a certain chargeaccepted from a node

	#print("Initialize RuleRemove function.")

	neurons = PSNP[0]
	rules = PSNP[1]

	index1 = 2 + ((neurons - 1) * neurons)
	for x in range(1, rules + 1):
		index2 = index1
		if(node == PSNP[index1 + 1]):
			if(chargeaccepted == PSNP[index1 + 3]):
				if(spikesconsumed == PSNP[index1]):
					if(chargefired == PSNP[index1 + 4]):
						if(spikesfired == PSNP[index1 + 5]):
							index2 = index2 + 6
							rule = PSNP[index1 : index2]
							del PSNP[index1 : index2]
							PSNP[1] -= 1
							#print("Terminate RuleRemove function.\n")
							return rule
		index1 = index1 + 6

	#PSNP[1] -= 1
	#graph.graphPSNP(PSNP)
	#print("Terminate RuleRemove function.\n")

	#return rule



def RuleReplace (PSNP, spikesconsumed, node, chargeaccepted, chargefired, spikesfired): #Independent of randomizer and whatsh*te

	#print("Initialize RuleReplace function.")

	neurons = PSNP[0]
	rules = PSNP[1]
	mutated = False

	oldrule = True

	#Makes sure that the new rule isn't a duplicate of the old rule
	while(oldrule == True): 
		newspikesconsumed = random.randint(1, 5) #Choose elements of new rule
		newchargeaccepted = random.choice([-1, 2, 1])
		newchargefired = random.choice([-1, 2, 1])
		newspikesfired = random.random()
		if(random.random() <= 0.2):
			newspikesfired = 0
		else:
			newspikesfired = 1		
		if((newspikesconsumed != spikesconsumed) or (newchargeaccepted != chargeaccepted) or (newchargefired != chargefired) or (newspikesfired != spikesfired)):
			oldrule = False


	if(mutated == True):
		index = 2 + ((neurons - 1) * neurons)
		for x in range(1, rules + 1):
			if(node == PSNP[index + 1]):
				if(chargeaccepted == PSNP[index + 3]):
					if(spikesconsumed == PSNP[index]):
						if(chargefired == PSNP[index + 4]):
							if(spikesfired == PSNP[index + 5]):
								PSNP[index] = newspikesconsumed
								PSNP[index + 3] = newchargeaccepted
								PSNP[index + 4] = newchargefired 
								PSNP[index + 5] = newspikesfired 
								print("Terminate RuleReplace function.")
								return True
			index1 = index1 + 6

	#print("Terminate RuleReplace function.")
	return False



def RuleSwap (PSNP1, PSNP2, node1, node2): #Swaps rules between a node from a PSNP and another node from another PSNP

	#print("Initialize RuleSwap function.")

	rules1 = []
	rules2 = []

	PSNP1copy = PSNP1[:]
	PSNP2copy = PSNP2[:]

	rulecharges1 = RuleCheck(PSNP1copy, node1)
	rulecharges2 = RuleCheck(PSNP2copy, node2)

	for charge in rulecharges1:
		rule = RuleRemove(PSNP1copy, charge[0], node1, charge[1], charge[2], charge[3])
		rules1.append(rule)
		#print("Charge1 appended")
	for charge in rulecharges2:
		rule = RuleRemove(PSNP2copy, charge[0], node2, charge[1], charge[2], charge[3])
		#print("Charge2 appended")
		rules2.append(rule)

	#PrintPSNP(PSNP1)
	#PrintPSNP(PSNP2)
	#print("Rule1 rules: {}".format(rules1))
	#print("Rule2 rules: {}".format(rules2))
	for rule in rules2:
		if(rule[5] == 0):
			RuleAdd(PSNP1copy, rule[0], node1, rule[3], rule[4], True)
		else:
			RuleAdd(PSNP1copy, rule[0], node1, rule[3], rule[4], False)
		#PrintPSNP(PSNP1)
	for rule in rules1:
		if(rule[5] == 0):
			RuleAdd(PSNP2copy, rule[0], node2, rule[3], rule[4], True)
		else:
			RuleAdd(PSNP2copy, rule[0], node2, rule[3], rule[4], False)
		#PrintPSNP(PSNP2)

	PSNP1 = PSNP1copy
	PSNP2 = PSNP2copy
	#graph.graphPSNP(PSNP1)
	#graph.graphPSNP(PSNP2)
	#print("Terminate RuleSwap function.\n")



def Mutate (PSNP):

	#print("Initialize Mutate function.")

	neurons = PSNP[0]
	rules = PSNP[1]

	tomutatesynapse = 0.4
	tomutaterule = 0.4
	tosynapseadd = 0.5
	tosynapseremove = 0.5
	tosynapsemutate = (1 - tosynapseadd) - tosynapseremove
	toruleadd = 0.4
	toruleremove = 	0.4
	torulereplace = (1 - toruleadd) - toruleremove
	toruleforgetting = 0.2
	largestspike = 5

	mutated = False
	while(mutated == False):
		chance = random.random()
		#Synapse = 40%
		if(chance <= tomutatesynapse):															
			#print("Synapse Mutation")
			synapsemutate = random.random()
			#Add synapse = 50%
			if(synapsemutate <= tosynapseadd):
				if(AllSynapseExist(PSNP) == False):
					#print("Synapse Mutation: Addition")
					loop = 5
					while(loop > 0):
						node1 = random.randint(1, neurons - 1)
						node2 = node1
						while(node2 == node1):
							node2 = random.randint(1, PSNP[0] - 1)
						if(SynapseExist(PSNP, node1, node2) == False):
							loop = 0
						else:
							loop = loop - 1
					#print("THE DAMNED NODES ARE: {} AND {}".format(node1, node2))
					SynapseEdit(PSNP, node1, node2, "Add")
					mutated = True
			#Remove synapse = 50%
			elif((synapsemutate > tosynapseadd) and (synapsemutate <= (tosynapseadd + tosynapseremove))):
				#print("Synapse Mutation: Removal")
				synapses = []
				while(synapses == []):
					node1 = random.randint(1, neurons - 1)
					synapses = SynapseCheck(PSNP, node1)
				node2 = random.choice(synapses)
				SynapseEdit(PSNP, node1, node2, "Remove")
				mutated = True
				if(PathCheck(PSNP) == False):
					SynapseEdit(PSNP, node1, node2, "Add")
					mutated = False
			else:
				print("")
				#print("Synapse Mutation: Replace")

		#Rules = 40%
		elif((chance > tomutatesynapse) and (chance <= (tomutatesynapse + tomutaterule))):
			#print("Rule Mutation")
			rulemutate = random.random()
			#Add rule = 30%
			if(rulemutate <= toruleadd):
				#print("Rule Mutation: Addition")
				loop = True
				while(loop):
					node = random.randint(1, neurons - 1)
					containedrules = RuleCheck(PSNP, node)
					innerloop = 0
					while(innerloop < 3):
						innerloop = innerloop + 1
						spikesconsumed = random.randint(1, largestspike)
						chargeaccepted = random.choice([-1, 2, 1])
						chargefired = random.choice([-1, 2, 1])
						if(random.random() <= toruleforgetting):
							forgetting = 0
						else:
							forgetting = 1
						if([spikesconsumed, chargeaccepted, chargefired, forgetting] not in containedrules):
							loop = False
							innerloop = 3
					#if(len(containedcharges) < 3):
					#	loop = False
				#chargesaccepted = [charge for charge in [-1, 2, 1] if charge not in containedcharges]
				#chargeaccepted = random.choice(chargesaccepted)
				if(forgetting == 0):
					RuleAdd(PSNP, spikesconsumed, node, chargeaccepted, chargefired, True)
				else:
					RuleAdd(PSNP, spikesconsumed, node, chargeaccepted, chargefired, False)
				'''Old method of choosing if forgetting or not
				if(random.random() < toruleforgetting):
					RuleAdd(PSNP, spikesconsumed, node, chargeaccepted, random.choice([-1, 2, 1]), True)
					mutated = True
				else:
					RuleAdd(PSNP, spikesconsumed, node, chargeaccepted, random.choice([-1, 2, 1]), False)
					mutated = True
				'''
			#Remove rule = 30%
			elif((rulemutate > toruleadd) and (rulemutate <= (toruleadd + toruleremove))):
				#print("Rule Mutation: Removal")
				node = random.randint(1, neurons - 1)
				containedrules = RuleCheck(PSNP, node)
				if(len(containedrules) == 1):
					containedrule = containedrules[0]
					RuleRemove(PSNP, containedrule[0], node, containedrule[1], containedrule[2], containedrule[3])
					mutated = True
				elif(len(containedrules) >= 1):
					removerule = random.choice(containedrules)
					RuleRemove(PSNP, removerule[0], node, removerule[1], removerule[2], removerule[3])
					mutated = True
			#Replace rule = 40%
			else:
				#print("Rule Mutation: Replace")
				node = random.randint(1, neurons - 1)
				containedrules = RuleCheck(PSNP, node)
				if(len(containedrules) == 1):
					removerule = containedrules[0]
					if(RuleReplace(PSNP, removerule[0], node, removerule[1], removerule[2], removerule[3]) == True):
						mutated = True
				elif(len(containedrules) >= 1):
					removerule = random.choice(containedrules)
					if(RuleReplace(PSNP, removerule[0], node, removerule[1], removerule[2], removerule[3]) == True):
						mutated = True


		#Both - 20%
		else:
			#print("Synapse and Rule Mutation")
			synapsemutate = random.random()
			#Add synapse = 50%
			if(synapsemutate <= tosynapseadd):
				if(AllSynapseExist(PSNP) == False):
					#print("Synapse Mutation: Addition")
					loop = 5
					while(loop > 0):
						node1 = random.randint(1, neurons - 1)
						node2 = node1
						while(node2 == node1):
							node2 = random.randint(1, PSNP[0] - 1)
						if(SynapseExist(PSNP, node1, node2) == False):
							loop = 0
						else:
							loop = loop - 1
					SynapseEdit(PSNP, node1, node2, "Add")
					mutated = True
			#Remove synapse = 50%
			elif((synapsemutate > tosynapseadd) and (synapsemutate <= (tosynapseadd + tosynapseremove))):
				#print("Synapse Mutation: Removal")
				synapses = []
				while(synapses == []):
					node1 = random.randint(1, neurons - 1)
					synapses = SynapseCheck(PSNP, node1)
				node2 = random.choice(synapses)
				SynapseEdit(PSNP, node1, node2, "Remove")
				mutated = True
				if(PathCheck(PSNP) == False):
					SynapseEdit(PSNP, node1, node2, "Add")
					mutated = False
			else:
				print("")
				#print("Synapse Mutation: Replace")



			rulemutate = random.random()
			#Add rule = 30%
			if(rulemutate <= toruleadd):
				#print("Rule Mutation: Addition")
				loop = True
				while(loop):
					node = random.randint(1, neurons - 1)
					containedrules = RuleCheck(PSNP, node)
					innerloop = 0
					while(innerloop < 3):
						innerloop = innerloop + 1
						spikesconsumed = random.randint(1, largestspike)
						chargeaccepted = random.choice([-1, 2, 1])
						chargefired = random.choice([-1, 2, 1])
						if(random.random() <= toruleforgetting):
							forgetting = 0
						else:
							forgetting = 1
						if([spikesconsumed, chargeaccepted, chargefired, forgetting] not in containedrules):
							loop = False
							innerloop = 3
					#if(len(containedcharges) < 3):
					#	loop = False
				#chargesaccepted = [charge for charge in [-1, 2, 1] if charge not in containedcharges]
				#chargeaccepted = random.choice(chargesaccepted)
				if(forgetting == 0):
					RuleAdd(PSNP, spikesconsumed, node, chargeaccepted, chargefired, True)
				else:
					RuleAdd(PSNP, spikesconsumed, node, chargeaccepted, chargefired, False)
				'''Old method of choosing if forgetting or not
				if(random.random() < toruleforgetting):
					RuleAdd(PSNP, spikesconsumed, node, chargeaccepted, random.choice([-1, 2, 1]), True)
					mutated = True
				else:
					RuleAdd(PSNP, spikesconsumed, node, chargeaccepted, random.choice([-1, 2, 1]), False)
					mutated = True
				'''
			#Remove rule = 30%
			elif((rulemutate > toruleadd) and (rulemutate <= (toruleadd + toruleremove))):
				#print("Rule Mutation: Removal")
				node = random.randint(1, neurons - 1)
				containedrules = RuleCheck(PSNP, node)
				if(len(containedrules) == 1):
					containedrule = containedrules[0]
					RuleRemove(PSNP, containedrule[0], node, containedrule[1], containedrule[2], containedrule[3])
					mutated = True
				elif(len(containedrules) >= 1):
					removerule = random.choice(containedrules)
					RuleRemove(PSNP, removerule[0], node, removerule[1], removerule[2], removerule[3])
					mutated = True
			#Replace rule = 40%
			else:
				print("")
				#print("Rule Mutation: Replace")

	#print("Terminate Mutate function.\n")



def Crossover (PSNP1, PSNP2):

	neurons1 = PSNP1[0]
	neurons2 = PSNP2[0]


	

	loop = True

	while(loop):
		chance = random.random()

		node1 = random.randint(1, neurons1 - 1)
		node2 = random.randint(1, neurons2 - 1)

		#print("Crossover between node {} of PSNP1 and node {} of PSNP2".format(node1, node2))

		if(chance <= 0.4):
			loop = -(SynapseSwap(PSNP1, PSNP2, node1, node2))
		elif(chance > 0.4 and chance <= 0.8):
			RuleSwap(PSNP1, PSNP2, node1, node2)
			loop = False
		else:
			if(SynapseSwap(PSNP1, PSNP2, node1, node2) == True):
				RuleSwap(PSNP1, PSNP2, node1, node2)
				loop = False
			else:
				loop = True



def Populate (PSNP, populationsize):

	#print("Initialize Populate function.")

	population = []
	for individual in range(0, populationsize):
		population.append(PSNP[ : ])

	#print(population)

	for i in range(0, populationsize):
		Mutate(population[i])
		#for individual in population:
		#	PrintPSNP(individual)

	#print("Terminate Populate function.\n")

	return population