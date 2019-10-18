import graph

while True:
	try:
		fileName = input("Enter PSNP filename to modify: ")
		fileName = fileName+'.txt'
		File = open(fileName, "r+")
		#File = (File.readline())
		PerfectPSNP = []
		for line in File:
			line = (line.strip())
			#print (line)
			[PerfectPSNP.append(int(item)) for item in line.split(' ')]
		print (PerfectPSNP)
		graph.graphPSNP(PerfectPSNP,'flakes','flakes')
		break
	except FileNotFoundError:
		print("Enter a valid filename...")

