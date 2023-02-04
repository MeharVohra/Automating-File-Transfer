''' You work at a company that receives daily data files from external partners. These files need to be 
processed and analyzed, but first, they need to be transferred to the company's internal network.

The goal of this project is to automate the process of transferring the files from an external FTP server to 
the company's internal network.

Here are the steps you can take to automate this process:

    Use the ftplib library to connect to the external FTP server and list the files in the directory.

    Use the os library to check for the existence of a local directory where the files will be stored.

    Use a for loop to iterate through the files on the FTP server and download them to the local directory using the ftplib.retrbinary() method.

    Use the shutil library to move the files from the local directory to the internal network.

    Use the schedule library to schedule the script to run daily at a specific time.

    You can also set up a log file to keep track of the files that have been transferred and any errors that may have occurred during the transfer process. '''




#%%


from datetime import time, datetime, timedelta
import ftplib
import os
import sched
import shutil
import schedule
import time as tm
import io
import sys

# Defining  function
def transfer_files():

    # connect to host, default port
    ftp = ftplib.FTP("ftp.us.debian.org")
    ftp.login("anonymous", "anonymous@")

    # change the directory
    ftp.cwd("debian")

    # tale all the files from debian directory
    files = ftp.nlst()
    
    # Gice the path of local directory
    local_directory = "C:/Users/mehar_uslilw0/Documents/local_files"

    # Check if the local directory exists, if not then create it
    if not os.path.exists(local_directory):
        os.makedirs(local_directory)

    for file in files:
        # Join each file with the local directory
        local_file = os.path.join(local_directory, file)
        # Used exceptional handling here since some files were not opening
        # Hence, ignored them
        try:
            with open(local_file, 'wb') as f:
                ftp.retrbinary('RETR ' + file, f.write)
                print(file)
        except:
            print("not able to open the file", file)
            continue

    print("Already dowloaded")
    print("Now shifting")    

    # Path for another local directory
    Another_local_directory = "C:/Users/mehar_uslilw0/Documents/shift_local_files"

    for file in files:
        # Move every file from local directory to another local directory
        shutil.move(local_directory + "/" + file, Another_local_directory + "/" + file)

    print("All done!")

    ftp.quit()

# Function for Scheduling
def timing(time, function):
    schedule.every().day.at(time).do(function)
    while True:
        # Run all jobs that are scheduled to run
        schedule.run_pending()
        #tm.sleep()


timing("00:12", transfer_files)

# %%
