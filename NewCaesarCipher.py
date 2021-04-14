import string
class CaesarCipher: 
    def __init__(self, plain_input, ciph_key):
        self.plain_input = plain_input
        self.ciph_key = ciph_key
        print(ciph_key)

    def split(self, word): 
        self.word = word
        split_list = [char for char in self.word]
        #print(split_list)
        return split_list  #list comprehension

    def getPlaintext(self, plaintext_input):
        plaintext = self.split(self.plain_input)
        #print(plaintext)
        return plaintext

    def encrypt(self):
        self.encrypt_plaintext = self.getPlaintext(self.plain_input)#returns list of characters in plaintext
        #print("encrypt: ", self.encrypt_plaintext)
        ciphertext = " " #empty string
        
        for ch in self.encrypt_plaintext:
            if ch.isupper():
                ciphertext += chr((ord(ch) + self.ciph_key - 65) % 26 + 65)
                #print(ciphertext)
            elif ch.islower():
                ciphertext += chr((ord(ch) + self.ciph_key - 97) % 26 + 97)
                #print(ciphertext)
            else:
                ciphertext += ch
                #print(ciphertext)
        print(ciphertext)
        return ciphertext

    def decrypt(self):
        self.decrypt_plaintext = self.getPlaintext(self.plain_input)
        text = " "
        for ch in self.decrypt_plaintext:
            if ch.isupper():
                text += chr((ord(ch) - self.ciph_key - 65) % 26 + 65)
                #print(text)
            elif ch.islower():
                text += chr((ord(ch) - self.ciph_key - 97) % 26 + 97)
                #print(text)
            else:
                text += ch
                #print(text)    
        return text

new_input = input("Type your message here: ")
ciph_key = int(input("How many characters do you want to shift by: "))
cipher = CaesarCipher(new_input, ciph_key)
#cipher.decrypt()
cipher.encrypt()










