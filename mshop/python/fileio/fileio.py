#########################################################
# Name: create_datetime_file
# Desc: Creates a single file within specified path.
# This file's name is a simple date/time 
# string, ensuring all future file creations will have
# a unique name.
#########################################################
def create_datetime_file(path, data, ext=".txt"):
    from datetime import datetime

    file_name = datetime.now().strftime("%d-%m-%Y_%H:%M:%S") + ext
    try:
        with open(path + file_name, 'a') as f:
            f.write(data + "\n")
    except IOError as e:
        print(e)

#########################################################
# Name: create_datetime_entry
# Desc: Creates a single line data entry within the
# specified file. Useful for data logging time sensitive
# information.
#########################################################
def create_datetime_entry(path, data):
    from datetime import datetime

    dt = datetime.now().strftime("[%d-%m-%Y_%H:%M:%S] ")
    try:
        with open(path, 'a+') as f:
            f.write(dt + data + "\n")
    except IOError as e:
        print(e)


### Example Use Case ###
#create_datetime_file("/home/pi/mshop/mshop/fileio/", "datadatadata", ".py")
#create_datetime_entry("/home/pi/mshop/mshop/fileio/entry.txt", "entryentryentry")
