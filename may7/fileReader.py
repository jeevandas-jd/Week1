

class FileReader(object):

    def __init__(self):

        self.files=[]

        self.currentfile=None

    def NewFile(self):

        filename="may7/inputFiles/"+input("enter file name ")

        if filename not in self.files:
            self.currentfile=filename

            self.files.append(filename)
        else:
            x=input("file aldredy existing do you want to read that file [Y/N]")

            if x=="Y":
                self.currentfile=filename

                self.ReadFile()
    def ReadFile(self):

        with open(self.currentfile,"r") as file:

            file.read()
    
    def WriteFile(self):


        with open(self.currentfile,"a") as file:

           lines=[]
           print("start typing the content press'ENTER' after every sentece,to stop listening type '../..'")
           text=None
           while text!="../..\n":
               text=input()+"\n"
               lines.append(text)
            
           file.writelines(lines)
    def listFiles(self):

        if len(self.files)==0:
            print("no files found")
        else:
            for i in range(len(self.files)):
                print(f"{i} : {self.files[i]}")
    def selectFile(self):
        self.listFiles()
        num=int(input("enter the index of file you want to slect"))
        self.currentfile=self.files[num]
        

def main():
    print("welcom to fileWriting CLI follow the Instructions to write your files")
    while(True):
        x=input("1.create a new file\n2.list all files\n3.select file\n4.write file\n5.read file\n6.exit program\n>>>")
        if x=="1":
            file=FileReader()
            file.NewFile()
        elif x=="2":
            file.listFiles()
        elif x=="3":
            file.selectFile()
        elif x=="4":
            file.WriteFile()
        elif x=="5":
            file.ReadFile()
        else:
            print("thank you for using fileWriting CLI")
            break
        

if __name__=="__main__":
    main()


                

