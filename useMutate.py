import graph
import Mutation
import os

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
		
		'''
		for x in range (0,10):
			Mutation.Mutate(PerfectPSNP)
			graph.graphPSNP(PerfectPSNP,'mutated'+'['+str(x)+']','mutated')
			#completeName = os.path.join(save_path, name_of_file+".txt")  
			#out = open(completeName, 'w')
			#out.write(' '.join(PerfectPSNP))
		'''
		save_path = os.getcwd()+'\mutated_txt'
		access_rights = 0o755
		try:
		    os.mkdir(save_path, access_rights)
		except OSError:
		    print ("Creation of the directory %s failed" % save_path)
		else:
		    print ("Successfully created the directory %s " % save_path)
		
		for x in range (0,10):
			Mutation.Mutate(PerfectPSNP)
			graph.graphPSNP(PerfectPSNP,'mutated'+'['+str(x)+']','mutated_graph')
			completePath = os.path.join(save_path, 'mutated'+'['+str(x)+']'+".txt")  
			out = open(completePath, 'w')
			str_PSNP = [str(i) for i in PerfectPSNP] 
			out.write(' '.join(str_PSNP))



		break
	except FileNotFoundError:
		print("Enter a valid filename...")
