import random
import base64
import sys,math,re


# Password generating page!
# this function generates password 
def pwd_gen(str_list_var):
    pasword = []
    for i in range(5):
        cd = ''
        for j in range(12):
            temp = (random.choice(random.choice(str_list_var)))
            cd = cd + temp
        pasword.append(cd)
    return pasword


# Password Strength checker
def Strong_password(pwd):
    n = len(pwd)
    points = 0
    for i in range(n): 
        var = pwd[i]
        if var.islower()==True:
            points = points + 1
        elif var.isupper()==True:
            points = points + 1
        elif var.isnumeric()==True:
            points = points + 2
        else:
            points = points + 3
        var2 = points * 4
    return var2
    

# Ecryption and Decryption
#function for encoding
def encr(var_b):
    #initializing string
    var2 = var_b
    #encoding string
    var2_bytes = var2.encode("ascii")
    base64_bytes = base64.b64encode(var2_bytes)
    global base64_string
    base64_string = base64_bytes.decode("ascii")
    #printing the encoded string
    return base64_string


#function for decoding
def decr(var_b):
    #initializing string
    base64_string = var_b
    #decoding string
    base64_bytes = base64_string.encode("ascii") 
    sample_string_bytes = base64.b64decode(base64_bytes) 
    global sample_string
    sample_string = sample_string_bytes.decode("ascii") 
    #printing decoded string
    return sample_string
    

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
#function for pwd strength cheker

def sen_pwd_length_con(password):
    length = str(len(password))
    global pass_length_good

    if len(password) < 8:
        pot1 = "[!] Password should be a at least 8 charcters long"
        pot2 = "[!] password is only" ,length,"charcters(s) long"
        password_length_good = False;
        return pot2 
    else:
        pot3 = "[*] Your password is ",length,"charcters"
        password_length_good = True;
        return pot3

def sen_pwd_uppercase_con(password): # for uppercase
    global upperlength
    upperlength = len(re.findall(r'[A-Z]',password))

    # pot4 = "[*] Your passwrd contains", upperlength,"upper case character(s)"

    if upperlength == 0:
        pot5 = "[!] password must contain some uppercase letters."
        return pot5


def sen_pwd_lowercase_con(password): # for lowercase
    global lowerlength
    lowerlength = len(re.findall(r'[a-z]',password))

    # pot6 = "[*] Your passwrd contains", lowerlength,"lower case character(s)"

    if lowerlength == 0:
        # print("[!] No lowercase charactes in password")
        pot7 = "[!] password must contain some lowercase letters."
        return pot7

    
def sen_pwd_numbers_con(password): # for numbers

    global digits
    digits = len(re.findall(r'[0-9]',password))

    # print("[*] Your password contains",digits,"numeric dogit(s)")

    if digits == 0:
        # print("[!] No digits in password")
        pot8 = "[!] password must contain some numeric value."
        return pot8
    

def sen_pwd_common_con(password): # commonly used
    global matchedpass 
    matchedpass = False

    commonpasswords = ['password','letmein','football','dragon','1234567','name','lemon']

    for commonpass in commonpasswords:
        if commonpass == password:
            matchedpass = True
    
    if matchedpass == True:
        pot9 = "[!] the passwords seems to be common. Please choose diffrent!"


def sen_pwd_char_con(password):# for charcters
    global match_char
    counter = 0
    # chars = ['!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',',','[',']']
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    # Pass the string in search 
    # method of regex object.    
    if(regex.search(password) == None):
        pot11 = "[!] password must contain some character value."
        return pot11
        # print(pot11)
    else:
        pass
        
                
    
            
        
        



def sen_pwd_eval_con(pass_length_good,upperlength,digits,matchedpass): # overall evaluation
    print("[*] Password Evaluation:")
    if password_length_good == True:
        print("[*] password length is good")
    else:
        print("[!] password length is bad")

    if upperlength >=3:
        print("[*] Your password have uppercase letters")
    else:
        print("[!] Your passwords does\'t contain uppercase letters")

    if digits >=3:
        print("good")
    else:
        print("bad")

    if matchedpass == True:
        print("match ho gya ..bad")
    else:
        print("match nahi hua ....good")
    

    if password_length_good == True and upperlength >=3 and matchedpass == False:
        print("good")
    else:
        print("not good")





# sen_pwd_uppercase_con("gojiu")
# sen_pwd_numbers_con("gojiu")
# sen_pwd_common_con("password")
sen_pwd_char_con("hallabol")
# sen_pwd_lowercase_con("PASS#$$")