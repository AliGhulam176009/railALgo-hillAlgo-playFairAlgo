key = input("Enter key : ")
key=key.upper()

def matrix5by5(x, y, starting):
    return [[starting for i in range(x)] for j in range(y)]
    
record = list()
for cha in key: #storing key
    if cha not in record:
        if cha == 'I':
            record.append('J')
        else:
            record.append(cha)
flag=10
for i in range(65, 91): #storing other character
    if chr(i) not in record:
        if i == 73 and chr(74) not in record:
            record.append("I")
            flag=1
        elif flag == 0 and i == 73 or i == 74:
            pass    
        else:
            record.append(chr(i))
k = 0
my_matrix = matrix5by5(5,5,0) #initialize matrix
for i in range(0,5): #making matrix
    for j in range(0,5):
        my_matrix[i][j] = record[k]
        k+=1

def locindex(c): #get location of each character
    loc = list()
    if c == 'J':
        c = 'I'
    for i ,j in enumerate(my_matrix):
        for k,l in enumerate(j):
            if c == l:
                loc.append(i)
                loc.append(k)
                return loc
            
def encrypt():  
    text = str(input("ENTER Plain TEXT : "))
    text = text.upper()            
    i = 0
    for s in range(0, len(text)+1, 2):
        if s < len(text)-1:
            if text[s] == text[s+1]:
                text = text[:s+1]+'X'+text[s+1:]
                
    if len(text)%2!=0:
        text=text[:]+'X'
    print("CIPHER TEXT : ", end='')
    
    while i<len(text):
        loc = list()
        loc = locindex(text[i])
        loc1 = list()
        loc1 = locindex(text[i+1])
        if loc[1] == loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]+1)%5][loc[1]], my_matrix[(loc1[0]+1)%5][loc1[1]]), end=' ')
        elif loc[0] == loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]+1)%5], my_matrix[loc1[0]][(loc1[1]+1)%5]), end=' ')  
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]], my_matrix[loc1[0]][loc[1]]), end=' ')    
        i = i+2        
                 
def decrypt():
	text = str(input("ENTER CIPHER TEXT:"))
	text = text.upper()
	print("PLAIN TEXT:", end=' ')
	i = 0
	while i<len(text):
		loc = list()
		loc = locindex(text[i])
		loc1 = list()
		loc1 = locindex(text[i+1])
		if loc[1] == loc1[1]:
			print("{}{}".format(my_matrix[(loc[0]-1)%5][loc[1]], my_matrix[(loc1[0]-1)%5][loc1[1]]), end=' ')
		elif loc[0] == loc1[0]:
			print("{}{}".format(my_matrix[loc[0]][(loc[1]-1)%5], my_matrix[loc1[0]][(loc1[1]-1)%5]), end=' ')  
		else:
			print("{}{}".format(my_matrix[loc[0]][loc1[1]], my_matrix[loc1[0]][loc[1]]), end=' ')   
		i = i+2        

while(True):
    choice = int(input("1)Encryption  2)Decryption:  3)EXIT \nSelect one option :"))
    print(" ")
    if choice == 1:
        encrypt()
        print("")
    elif choice == 2:
        decrypt()
        print("")
    elif choice == 3:
        exit()
    else:
        print("Choose correct choice")
