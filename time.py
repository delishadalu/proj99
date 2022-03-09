import time
import os
import shutil

time= time.time() - (30*24*60*60)



def main():
    folder=input('folder name? ')

    for root,folder,file in os.walk(folder):

        if(time< os.stat(root).st_ctime):
            shutil.rmtree(root)

        else:
            for folder in folder:
                if(time < os.stat(root+'/'+folder).st_ctime):
                    shutil.rmtree(root+'/'+folder)

            for file in file:
                if(time < os.stat(root+'/'+file).st_ctime):
                    os.remove(root+'/'+file)

            

        
        

        
         
     





main()