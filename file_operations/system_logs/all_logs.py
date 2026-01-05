all_logs_path="file_operations\\system_logs\\all_logs.txt"

error_path="file_operations\\system_logs\\error.txt"

info_path="file_operations\\system_logs\\info.txt"

warning_path="file_operations\\system_logs\\warning.txt"

fr_logs=open(all_logs_path,"r")

fw_error=open(error_path,"w")

fw_info=open(info_path,"w")

fw_warning=open(warning_path,"w")

for line in fr_logs:

    line=line.rstrip("\n")

    log_type=line.split(" ")[2].casefold()

    if log_type=="error":

        fw_error.write(line+"\n")

    elif log_type=="warning":

        fw_warning.write(line+"\n")

    elif log_type=="info":

        fw_info.write(line+"\n")

print("progream end")




