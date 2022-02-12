
#Polyalphabetic Cipher 

txt = input("Enter text (Polyalphabetic Cipher): ").upper()
q = input("- Encode  (1): \n- Decode  (2):\n- Both (3):\n- Make a choice, Comrade ! : ")

alpha = [chr(i) for i in range(65, 91)]

res = []
for i in [txt[i:i+3] for i in range(0, len(txt), 3)]:
	for x, y in zip([3, 5, 7], i):res.append(alpha[(ord(y)%65+x)%26])

txt = "".join(res) if q != "2" else txt

print("\n\nEncoding result: "+txt if q == "1" or q == "3" else "")

res = []
for i in [txt[i:i+3] for i in range(0, len(txt), 3)]:
	for x, y in zip([-3, -5, -7], i):res.append(alpha[(ord(y)%65+x)%26])

print("\n\nDecoding result: "+"".join(res) if q == "2" or q == "3" else "")

##### optional #####
import time,sys
for i in range(9,1,-1):
	time.sleep(1)
	sys.stdout.write("\r"+str(i)+ " time left.")
	sys.stdout.flush()
sys.exit()
