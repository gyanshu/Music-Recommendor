import re
currTimeStamp=0
currUser=""
SESSION_ID=0

def timeDiff(DATE):
	global currTimeStamp,currUser,SESSION_ID

	if currTimeStamp!=0:
		if(currTimeStamp.split('T')[0]!=DATE.split('T')[0]):
			currTimeStamp=DATE
			return False
		else:
			arr1=re.split('Z|:',currTimeStamp.split('T')[1])
			arr2=re.split('Z|:',DATE.split('T')[1])

			diff =0
			diff= diff+abs(int(arr1[0])-int(arr2[0]))*3600
			diff= diff +abs(int(arr1[1])-int(arr2[1]))*60
			diff= diff +abs(int(arr1[2])-int(arr2[2]))

			currTimeStamp=DATE	
			if(diff>800):
				return False
			else:
				return True
	else:
		currTimeStamp=DATE
		return False


def main():
	i=0
	SESSION=[]

	global currUser,currTimeStamp,SESSION_ID

	FOUT =open("OUT.txt",'w')

	with open('/home/shivani/Downloads/lastfm/userid-timestamp-artid-artname-traid-traname.tsv') as INPUTFILE:
		line = INPUTFILE.readline()
		while(line):
			# print("__________")
			# print(line)

			entries=line.split('\t')
			USER= entries[0].split('_')[1]
			TIME= entries[1]
			SONGID=entries[2]
			print(USER)
			print(TIME)
			print(SONGID)

			if(USER!=currUser or not timeDiff(TIME)):
				if(len(SESSION)>=10):
					SESSION_ID =SESSION_ID+1
					SESSION.insert(0,currUser)
					SESSION.insert(0,SESSION_ID)
					# ALL =ALL.append(SESSION)

					for element in SESSION:
						FOUT.write(str(element))
						FOUT.write(" ")
					FOUT.write("\n")

					print(SESSION)
					SESSION=[]
			else:

				SESSION.append(SONGID)
			currUser=USER
			currTimeStamp=TIME

			i=i+1
			if(i>25000):
				break
			line = INPUTFILE.readline()
			# timeDiff("2009-05-04T13:40:10Z")

	print(SESSION)	
	FOUT.close()

if __name__=="__main__":
	currTimeStamp=0
	currUser=""
	main()	