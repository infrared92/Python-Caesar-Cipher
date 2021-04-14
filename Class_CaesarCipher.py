import string
class CaesarCipher: 
    def __init__(self, plain_input, ciph_key):
        self.alphabet = dict.fromkeys(string.ascii_lowercase, 0)  
        #self.val = val
        self.plain_input = plain_input
        self.ciph_key = ciph_key
        #print(self.alphabet)

    def index(self, dict):
        self.dict = dict
        n = 0 #position/index 
        for k in dict.keys():
            n += 1
            dict[k] += n #increase each index by 1 
        #print(dict) 
        return dict

    def split(self, word): 
        self.word = word
        split_list = [char for char in self.word]
        #print(split_list)
        return split_list  #list comprehension

    def getKey(self, diction, val): #takes in value of key
        self.diction = diction
        print(self.diction)
        self.val = val
        for key,value in self.diction.items(): #for each key value pair
            if self.val == value: #if the input key is in the dictionary, return that key
                print("getKey: ", key)
                return key

    def getPlaintext(self, plaintext_input):
        plaintext = self.split(self.plain_input)
        #print(plaintext)
        return plaintext

    def encrypt(self):
        self.encrypt_plaintext = self.getPlaintext(self.plain_input)#returns list of characters in plaintext
        #print("encrypt: ", self.encrypt_plaintext)
        ciphertext = " " #empty string
        cipher_lst = [] #list of cipher values
        indexed_alphabet = self.index(self.alphabet) 
        print(indexed_alphabet)
        for char in self.encrypt_plaintext: 
            for wrd in indexed_alphabet.keys():
                if char in wrd:
                    #print("letter pos: ", self.alphabet[char])
                    cipher = indexed_alphabet[char] + self.ciph_key #shift the position of the character in the alphabet
                    #print("shifted pos: ", cipher)
                    ciphertext = cipher % len(self.alphabet) #use % to find the new char
                    cipher_lst.append(ciphertext) #list of each char in ciphertext (numbers)
        print("cipher_lst: ", cipher_lst)

        encrypted_text = "" #empty string
        new_val = ""
        for final_val in cipher_lst:
            new_val = self.getKey(indexed_alphabet, final_val)
           # print(new_val)
           # print(encrypted_text + new_val)
            encrypted_text += new_val           
        print(encrypted_text)
        #print(alphabet)


new_alphabet = dict.fromkeys(string.ascii_lowercase, 0)  
new_input = input("Enter your message here: ")
cipher = CaesarCipher(new_input, 4)
cipher.encrypt()










