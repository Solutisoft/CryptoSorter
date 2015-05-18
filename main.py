 # -*- coding: cp1252 -*-
# Open Source GNU GPLv3 Licence
# http://www.gnu.org/licenses/gpl-3.0.txt

#   CryptoSorter 
#   This was written in response the the awful CryptoLocker virus
#   While it is not able to decrypt files it automatically sorts the of
#   The file types that CryptoLocker attacks. Any unencrypted files are
#   then moved to a user specified directory. It is recommended to run this
#   offline through a linux distribution due to the worm like nature of 
#   the virus so as to prevent further infection

print("                             Welcome to CryptoSorter!")
print("If you are reading this then you have likely been the unfortunate victim of the cryptolocker virus. While it is impossible to decrypt your files without the key this program automatically finds any files that CryptoLocker happened to miss and moves them to a directory of you choice. It is recommended to run this utility from a live linux environment so as to keep the virus from infecting your external storage device. This utility is free to use and modify under GNU GPLv3 open source licence")
print("*******************************************************************************")
print("-Feel free to contact me with any questions or comments: Josiah@solutisoft.com-")
print("*******************************************************************************")
print('')
print("________________________________________")
print("|This software Sorts through the following file types: '*.jpg','*.pdf','*.jpeg','*.docx','*.xlsx','*.doc','*.pst','*.ppt','*.pptx','*.jpe'")
print("_______________________________________")

import os
from os import walk
import re
import glob
import shutil
TD=raw_input("Please type the directory to search: ") 
ND=raw_input("Please type the directory to copy good files to: ")
BadFiles=[]
FileList=[]
TDList=[]
ftypes=[]
img=[]
offc=[]
pdf=[]
FileTypes=['*.jpg','*.pdf','*.jpeg','*.docx','*.xlsx','*.doc','*.pst','*.ppt','*.pptx','*.jpe']
HeaderStrings=['PK','xif','ÐÏ','BDN','PDF','JFIF','','ÿØÿ']
imgHeaders=['xif','JFIF']
offcHeaders=['ÐÏ','PK','BDN','ÿØÿ','',]
pdfHeaders=['pdf']
GoodFiles=[]
print('')
print('___________________________________________________')
print("Now searching for valid files. Please wait")
for path, dirs, files in os.walk(TD): # this is to gather all file's with the extensions in FileTypes into an array
        for f in xrange(len(files)):
                fstring=(os.path.join(path, files[f]))
                fstring=fstring.replace("\\","/")
                if fstring.rfind(('jpg')or('jpeg')or('jpe')) > -1:
                        img.append(fstring)
                if fstring.rfind('pdf') > -1:
                        pdf.append(fstring)
                if fstring.rfind(('docx')or('xlsx')or('pst')or('ppt')or('pptx')or('doc'))>-1:
                        offc.append(fstring)

def cryptocheck(targetPath,headerArray): #this is the function that checks for encryption. it searchs the header of the file for the appropriate text that typically
        q=1
        targetFile=open(targetPath,'r') 
        Sstring=targetFile.readline()
        Sstring=(Sstring+str(targetFile.readline()))
        Sstring=(Sstring+str(targetFile.readline()))
        for i in xrange(len(headerArray)):
                if Sstring.rfind(headerArray[i]) > -1:
                        GoodFiles.append(targetPath)
                        q=2
                if q==2:
                        break
        if q==1:
                BadFiles.append(targetPath)

print("______________________________")
print("Now checking for encryption on files")

for x in (img):
        cryptocheck(x,imgHeaders)
for x in (offc):
        cryptocheck(x,offcHeaders)
for x in (pdf):
        cryptocheck(x,pdfHeaders)

FileList=img+offc+pdf
print("The total number of files found on the system: "+str(len(FileList)))
print"Of these, "+str(len(BadFiles))," seem to be encrypted"
cont=input("Enter 1 to move unencrypted files to target directory or 0 to write log files and exit.")


goodLOG=open(ND+str("\UnencryptedFiles.txt"),"w")
allLOG=open(ND+str("\AllFiles.txt"),"w")
badLOG=open(ND+str("\EncryptedFiles.txt"),"w")

for x in FileList:
        allLOG.write("%s\n" % x)
for x in GoodFiles:
        goodLOG.write("%s\n" %x)
for x in BadFiles:
    badLOG.write("%s\n" %x)
badLOG.close()
allLOG.close()
goodLOG.close()
if cont==1:
        print("Now Writing unencrypted files")
        for x in GoodFiles:
                shutil.copy(x,ND)
        print("***********************************************************")
        print("*          Search and Recovery Complete!!!                *")
        print("***********************************************************")
        print("Total files found: "+str(len(FileList)))
        print("Total Encrypted files found "+str(len(FileList)-len(GoodFiles)))
        print("Total unencrypted files found: "+str(len(GoodFiles)))
        des=raw_input("Thank you for using CryptoSorter! Press any key to quit")
else:
        print("Thank you for using CryptoSorter. All log files have been saved to the target directory")
        
                        
        
        
