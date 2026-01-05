email_path="file_operations\\email_process\\email.txt"

gmail_path="file_operations\\email_process\\gmail.txt"

outlook_path="file_operations\\email_process\\outlook.txt"

yahoo_path="file_operations\\email_process\\yahoo.txt"

fr_email=open(email_path,"r")

fw_gmail=open(gmail_path,"w")

fw_outlook=open(outlook_path,"w")

fw_yahoo=open(yahoo_path,"w")

for line in fr_email:

    email_id=line.rstrip("\n")

    if email_id.endswith("@gmail.com"):

        fw_gmail.write(email_id+"\n")

    elif email_id.endswith("@outlook.com"):

        fw_outlook.write(email_id+"\n")

    elif email_id.endswith("@yahoo.com"):

        fw_yahoo.write(email_id+"\n")

print("end program")