from flask import Flask,render_template,request
from supporter import pwd_gen,Strong_password,encr,decr
from encryption_decryption import encode_dark_msg,decode_dark_msg
from hashing_algorithms import *
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from password_cal import pwd_analyseir
from supporter import *
from username_init import recom_username_loop


app = Flask(__name__)

#Configuration of username database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cool_user_name.db"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)

#creating class
class username(db.Model):
    Sno = db.Column(db.Integer,primary_key=True)
    u_name = db.Column(db.String(200),nullable=False)
    date_inserted = db.Column(db.DateTime,default=datetime.utcnow)

    # representation of data objects
    def __repr__(self) -> str:
        return f"{self.Sno} - {self.u_name}"

# Home page

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/learn_more')
def learn_more():
    return render_template('learn_more.html')

@app.route('/Sign_up')
def sign_up_form():
    return render_template('sign_up_form.html')

@app.route('/Log_in')
def log_in_form():
    return render_template('sign_in.html')

@app.route('/Load_more')
def load_more():
    return render_template('discover_more.html')

@app.route('/index/Descover_more/username/gate_way')
def username_gateway():
    return render_template('username_gateway.html')

@app.route('/rev_hash',methods=['GET','POST'])
def reversing_hash():
    if request.method=='POST':
        var_1 = request.form['hash_name_56']
        if var_1=="":
            return render_template('error_page.html')
        var_2 = "not found in our database !"
        return render_template('reverse_hash.html',var_1=var_1,var_2=var_2)
    else:
        return render_template('reverse_hash.html')


# E N C R Y P T I O N    &   D E C R Y P T I O N
# VARIABLES FOR THIS IS DECLARED HERE BE AWARE !

@app.route('/index/Descover_more/Encryption_Decryption/coo89_80924rfujn$r/Encrypt$Decrypt/Gateway9modificationSystemdotin')
def en_de_gateway():
    return render_template('en_de_gateway.html')

@app.route('/index/Descover_more/Encryption_Decryption/coo89_80924rfujn$r/Encrypt$Decrypt/Gateway9modificationSystemdotin/bothGateWAY')
def ende_long_gateway():
    return render_template('ende_long_gateway.html')

@app.route('/index/Descover_more/username/gate_way/en=cryption_de=cryption',methods=['GET','POST'])
def encryption_decryption():
    if request.method=='POST':
        var_3 = request.form['hash_name_54']
        var_4 = request.form['hash_name_55']
        #encrypting
        var_5 = encr(var_3)
        var_6 = decr(var_4)
        print(var_5,var_6)
        return render_template('en_decryption_short.html',var_5=var_5,var_6=var_6)
    else:
        return render_template('en_decryption_short.html')
#code for Decryption and  of  L O N G

@app.route('/index/Descover_more/Encryption_Decryption/coo89_80924rfujn$r/Encrypt$Decrypt/Gateway9modificationSystemdotin/De_de&Long',methods=['GET','POST'])
def decryption():
    if request.method=='POST':
        #Encrypting
        var_9 = request.form['hash_name_57'] # Long string will come here as a input here.
        len_var_1 = len(var_9)
        print("Length of the ",len_var_1)
        if len_var_1 < 100:
            return render_template('error_page.html')
        else:
            #Decrypting
            var_10 = decode_dark_msg(var_9)
            return render_template('decrypt_long.html',var_10=var_10)
    else:
        return render_template('decrypt_long.html')

#code for Encryption and  of  L O N G
@app.route('/index/Descover_more/username/gate_way/en=cryption_de=cryptionEN',methods=['GET','POST'])
def encrypt_long():
    if request.method=='POST':
        #Encrypting
        var_7 = request.form['hash_name_58'] # short input will come here
        len_var_2 = len(var_7)
        print("lenght of the string is :",len_var_2)
        if len_var_2 == " ":
            return render_template('error_page.html')
        else:
            #Decrypting
            var_8 = encode_dark_msg(var_7)
            return render_template('encrypt_long.html',var_8=var_8)
    else:
        return render_template('encrypt_long.html')




#Password Generation pakage
a_num_1 = [m for m in '1234567890']
c_alpha_sml_3 = [letter for letter in 'abcdefghijklmnopqrstuvwxyz']
b_alpha_cap_2 = [i for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
d_special_char_4 = [ ch  for ch in '!@#$%^&*()_":?><,./-+']
menu_arr = [a_num_1, b_alpha_cap_2, c_alpha_sml_3, d_special_char_4]

# Variables used in recommending page (can also be used globaly)
one = 1
two =2
three = 3
forth_Snum = 4
fiv_Snum = 5
serial_num = "Sno"
pwd = "password"
strength = "Strength"
class_var = "Excellent"

@app.route('/recommend_password',methods=['GET','POST'])
def rec_pwd():
    if request.method=='POST':
        var = pwd_gen(menu_arr) # returning a list of paswords
        first = var[0]
        sec = var[1]
        thi = var[2]
        forth = var[3]
        fiv = var[4]
        grade = 99
        return render_template('recommend.html',first=first,sec=sec,thi=thi,forth=forth,serial_num=serial_num,pwd=pwd,
        strength=strength,fiv=fiv,grade=grade,class_var=class_var,one=one,two=two,three=three,forth_Snum=forth_Snum,fiv_Snum=fiv_Snum)
    else:
        return render_template('recommend.html')

# Password strength checker

@app.route('/strong_pwd',methods=['GET','POST'])
def str_pwd():
    if request.method=='POST':
        var2 = request.form['test_pwd']
        var7 = sen_pwd_length_con(var2)
        var8 = sen_pwd_uppercase_con(var2)
        var9 = sen_pwd_lowercase_con(var2)
        var10 = sen_pwd_numbers_con(var2)
        var11 = sen_pwd_common_con(var2)
        var12 = sen_pwd_char_con(var2)
        if var2=="":
            return render_template('error_page.html')
        else:
            var1 = pwd_analyseir(var2)
            # print(var1,var2)    
            iner_val = var1[0]
            # print(iner_val)
            if iner_val == 0:
                var3 = "very weak/poor"
                return render_template('strong_password.html',var3=var3,iner_val=iner_val,var7=var7,var8=var8,var9=var9,var10=var10,var11=var11,var12=var12)
            elif iner_val == 1:
                var4 = "average"
                return render_template('strong_password.html',var4=var4,iner_val=iner_val,var7=var7,var8=var8,var9=var9,var10=var10,var11=var11,var12=var12)
            elif iner_val == 2:
                var5 = "very Strong"
                return render_template('strong_password.html',var5=var5,iner_val=iner_val,var7=var7,var8=var8,var9=var9,var10=var10,var11=var11,var12=var12)

            
                
        return render_template('strong_password.html')
    else:
        return render_template('strong_password.html')


# E  N  C  R  Y  P  T  I  N  G    A  N  D    D  E  C  R  Y  P  T  I  N  G   F I L E S

@app.route('/index/Descover_more/Encryption_Decryption/coo89_80924rfujn$r/Encrypt$Decrypt/Gateway9modificationSystemdotin/Ende_de&Long/Encrypting_filesconstu_?nuolkij')
def en_File():
    return render_template('encrypt_file.html')

@app.route('/index/Descover_more/Encryption_Decryption/coo89_80924rfujn$r/Encrypt$Decrypt/Gateway9modificationSystemdotin/Ende_de&Long/DEcrypting_filesconstu_?nuolkij')
def de_File():
    return render_template('decrypt_file.html')


# ************************ A L L   H A S H I N G   A L G O R I T H M S *********************************

@app.route('/index/Descover_more/Hashing_All/AlogrithMSuolkij')
def Hashing_all_home():
    return render_template('hashing_page.html')

@app.route('/index/Descover+more/Hashing/Hashing_from0kjlpnopenanana_kl/HashinhHo/rahah',methods=['POST','GET'])
def hashing_page():
    if request.method=='POST':
        seq_var = request.form['hash_name_60']
        print(seq_var)
        if seq_var=="":
            return render_template('error_page.html')
        else:
            var_shake_128=hashing_shake_128(seq_var)
            var_sha1=hashing_sha1(seq_var)
            var_sha3_512=hashing_sha3_512(seq_var)
            var_sha512=hashing_sha512(seq_var)
            var_sha3_256=hashing_sha3_256(seq_var)
            var_sha3_384=hashing_sha3_384(seq_var)
            var_sha256=hashing_sha256(seq_var)
            var_blake2b=hashing_blake2b(seq_var)
            var_sha384=hashing_sha384(seq_var)
            var_md5=hashing_md5(seq_var)
            var_sha3_224=hashing_sha3_224(seq_var)
            var_shake_256=hashing_shake_256(seq_var)
            var_blake2s=hashing_blake2s(seq_var)
            var_sha224=hashing_sha224(seq_var)
            return render_template('hashing_page.html',var_shake_128=var_shake_128,
                                                        var_sha1=var_sha1,
                                                        var_sha3_512=var_sha3_512,
                                                        var_sha512=var_sha512,
                                                        var_sha3_256=var_sha3_256,
                                                        var_sha3_384=var_sha3_384,
                                                        var_sha256=var_sha256,
                                                        var_blake2b=var_blake2b,
                                                        var_sha384=var_sha384,
                                                        var_md5=var_md5,
                                                        var_sha3_224=var_sha3_224,
                                                        var_shake_256=var_shake_256,
                                                        var_blake2s=var_blake2s,
                                                        var_sha224=var_sha224)
    else:
        return render_template('hashing_page.html')


# USENAME MECHANISM WORKS HERE .************** DATABASE IS BBEN DECLARED ABOVE ##DATABASE_CONFIGUTATION


# @app.route('/index/Descover_more/klopyu7njnui/90hnbty/Uder$name/Username',methods=['POST','GET'])
# def Sugestion_usernme():
#     if request.method=='POST':
#         sug_var = request.form['suggestion_name_100']
#         print(sug_var)
#         if sug_var=="":
#             return render_template('error_page.html')
#         else:
#             sug_var_two = username(u_name=sug_var)
#             db.session.add(sug_var_two)
#             db.session.commit()
#             return render_template('succes_page.html')
#     else:
#         return render_template('suggest_username.html')


@app.route('/index/Descover_more/klopyu7njnui/90hnbty/Uder$name/Username',methods=['POST','GET'])
def Sugestion_usernme():
    if request.method=='POST':
        sug_var = request.form['suggestion_name_100']
        if sug_var=="":
            return render_template('error_page.html')
        else:
            return render_template('succes_page.html')
    else:
        return render_template('suggest_username.html')


# ****************user name recomendation*****************

@app.route('/index/Descover_more/killjoy/loppikj/loljehhfnjmk2io290ij$rgropp/mklopqqoj7887455oki3354374iiu', methods =['POST','GET'])
def recommend_username():
    if request.method=='POST':
        data = recom_username_loop()
        # print(data)
        return render_template('user_recomnd.html',data=data)
    else:
        return render_template('user_recomnd.html')
    


if __name__ == '__main__':
    app.run(debug=True)


    