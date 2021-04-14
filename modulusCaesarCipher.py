import string

def split(word): 
    return [char for char in word]  #list comprehension

#word = "the"
#print(split(word))


#Alphabet dict:
alphabet = dict.fromkeys(string.ascii_lowercase, 0) #returns a dictionary with string object
#print(alphabet)

n = 0 #position/index 
for k in alphabet.keys():
    n += 1 
    alphabet[k] += n #increase each index by 1 

'''print(alphabet) #each letter is assigned to its index in alphabet
print(alphabet.keys())'''

def getKey(diction, val): #takes in value of key
    for key,value in diction.items(): #for each key value pair
        if val == value: #if the input key is in the dictionary, return that key
            return key     


j = (getKey(alphabet, 10))
#print(j)

plain_input = "alphabet"
plaintext = split(plain_input)

'''print(plaintext)
print(alphabet.keys())'''

ciph_key = 3
cipher = 0
ciphertext = " "
cipher_lst = [] #list of cipher values
for char in plaintext:
    for wrd in alphabet.keys():
        if char in wrd:
            #print(alphabet[char])
            cipher = alphabet[char] + ciph_key
            ciphertext = cipher % len(alphabet)
            cipher_lst.append(ciphertext)
#print(cipher_lst)

encrypted_text = "" #empty string
new_val = ""
for final_val in cipher_lst:
    new_val = getKey(alphabet, final_val)
    print(new_val)
    encrypted_text += new_val           
print(encrypted_text)
#print(alphabet)

