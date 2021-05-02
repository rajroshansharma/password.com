from cryptography.fernet import Fernet




#Get the key from the file
file = open('key.key','rb')
key=file.read()
file.close()

#Encode the message
def encode_dark_msg(msg_12):
    message = msg_12
    encoded = message.encode()
    # E N C R Y P T I N G   T H E   M E S S A G E
    f = Fernet(key)
    encrypted = f.encrypt(encoded)
    return encrypted.decode()

#Decode the message
def decode_dark_msg(msg_13):
    var = msg_13
    message = var
    # f2 = Fernet(key)
    # decrypted = f2.decrypt(message)
    # print(decrypted.decode())
    msg = message.encode()
    f2 = Fernet(key)
    decrypted = f2.decrypt(msg)
    return decrypted.decode()


