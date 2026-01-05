db_psw = 9988
db_otp = 505623

psw=int(input("enter your password : "))
if(psw==db_psw):
    otp = int(input("enter your OTP : "))
    if(otp==db_otp):
     print("login successfully")
    else:
       print("incorrect OTP ")
else:
   print("incorrect password")