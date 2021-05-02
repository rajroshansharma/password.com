import hashlib as hb

# v = b'this is a example'
# print(v.decode())

def hashing_shake_128(var_hash):
    msg = var_hash
    msg_encoded = msg.encode()
    hashed_st = hb.shake_128(msg_encoded).hexdigest(80) # needs length declaration 
    return(hashed_st)


def hashing_sha1(var_hash):
    msg = var_hash
    msg_encoded = msg.encode()
    hashed_st = hb.sha1(msg_encoded).hexdigest()  
    return(hashed_st)

def hashing_sha3_512(var_hash):
    msg = var_hash
    msg_encoded = msg.encode()
    hashed_st = hb.sha3_512(msg_encoded).hexdigest()  
    return(hashed_st)


def hashing_sha512(var_hash):
    msg = var_hash
    msg_encoded = msg.encode()
    hashed_st = hb.sha512(msg_encoded).hexdigest()  
    return(hashed_st)    


def hashing_sha3_256(var_hash):
    msg = var_hash
    msg_encoded = msg.encode()
    hashed_st = hb.sha3_256(msg_encoded).hexdigest()  
    return(hashed_st) 


def hashing_sha3_384(var_hash):
    msg = var_hash
    msg_encoded = msg.encode()
    hashed_st = hb.sha3_384(msg_encoded).hexdigest()  
    return(hashed_st) 


def hashing_sha256(var_hash):
    msg = var_hash
    msg_encoded = msg.encode()
    hashed_st = hb.sha256(msg_encoded).hexdigest()  
    return(hashed_st) 


def hashing_blake2b(var_hash):
    msg = var_hash
    msg_encoded = msg.encode()
    hashed_st = hb.blake2b(msg_encoded).hexdigest()  
    return(hashed_st)

def hashing_sha224(var_hash):
    msg = var_hash
    msg_encoded = msg.encode()
    hashed_st = hb.sha224(msg_encoded).hexdigest()  
    return(hashed_st)


def hashing_sha384(var_hash):
    msg = var_hash
    msg_encoded = msg.encode()
    hashed_st = hb.sha384(msg_encoded).hexdigest()  
    return(hashed_st)


def hashing_md5(var_hash):
    msg = var_hash
    msg_encoded = msg.encode()
    hashed_st = hb.md5(msg_encoded).hexdigest()  
    return(hashed_st)


def hashing_sha3_224(var_hash):
    msg = var_hash
    msg_encoded = msg.encode()
    hashed_st = hb.sha3_224(msg_encoded).hexdigest()  
    return(hashed_st)


def hashing_shake_256(var_hash):
    msg = var_hash
    msg_encoded = msg.encode()
    hashed_st = hb.shake_256(msg_encoded).hexdigest(80)  # needs length declaration 
    return(hashed_st)


def hashing_blake2s(var_hash):
    msg = var_hash
    msg_encoded = msg.encode()
    hashed_st = hb.blake2s(msg_encoded).hexdigest()  
    return(hashed_st)


    