import random
import string
import argparse




class Password:


    def __init__(self,charset,length):
        self.charset = charset
        self.length = length
        self.char_arrey = []
        self.password = []
        

    def set_char_arrey(self):

        if("l" in self.charset):
            self.char_arrey.append(string.ascii_lowercase)
        if("u" in self.charset):
            self.char_arrey.append(string.ascii_uppercase)
        if("n" in self.charset):
            self.char_arrey.append(string.digits)
        if("s" in self.charset):
            self.char_arrey.append(string.punctuation)



    def get_char_arrey(self):
        return self.char_arrey

        
    
    def generate_password(self):
        for i in range(self.length):

            outer_index = random.randrange(0,len(self.char_arrey))
            inner_index= random.randrange(0,len(self.char_arrey[outer_index]))
            self.password.append(self.char_arrey[outer_index][inner_index])
            
    def get_password(self):
        return ''.join(self.password)




args = argparse.ArgumentParser('''Passwordgen.py -c [CHARSET] -l [LENGTH] \n\n For CHARSET :- \n 1. l --> LOWERCASE \n 2. u --> UPPERCASE \n 3. n --> NUMERIC \n 4. s --> SYMBOLS \n''')
args.add_argument('-c','--charset', default="luns")
args.add_argument('-l','--length',default=8)
options = args.parse_args()

password = Password(options.charset,int(options.length))
password.set_char_arrey()
password.generate_password()
print("---------------------------------------------------------------------------")
print("|                                                                         |")
print("|                                                                         |")
print(f'  Your Password is : {password.get_password()}') 
print("|                                                                         |")
print("|                                                                         |")
print("|                                                                         |")
print("|                                                                         |")
print("|                                                                         |")
print("|                                                      [Made By Vivek]    |")
print("---------------------------------------------------------------------------")




        