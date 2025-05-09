import os
import pandas as pd


class CSVanalyzer(object):

    def __init__(self):
        self.filepath=None
        self.df=None
        self.currentfile=None
    def createCSV(self):
        
        fileName=input("Enter file name")
        if os.path.exists(f"may9/sampleCSV/{fileName}.csv"):
            print(f"file name {fileName}.csv aldredy existing")
        else:
            with open(f"may9/sampleCSV/{fileName}.csv","w") as f:
                pass
            print(f"file {fileName}.csv created successfully")
    def loadCSV(self):
        files = os.listdir("may9/sampleCSV")
        for i in range(len(files)):
            print(f"{i+1}. {files[i]}")
        x = int(input("choose file index .>>"))
        self.currentfile = files[x - 1]
        file_path = f"may9/sampleCSV/{self.currentfile}"

        try:
            self.df = pd.read_csv(file_path)
        except pd.errors.EmptyDataError:
            print("Warning: The file is empty. Creating an empty DataFrame.")
            self.df = pd.DataFrame()
    def AddColums(self):

        if self.df is None:
            print("file is not loaded")
            return
        else:
            flag=input(f"the file loaded is {self.currentfile} proceed with that [y/n]>>> ")

            if flag=='y':
                existingColums=self.df.columns
                print(f"existing columns = {existingColums}")
                newCol=input("enter new column >>> ")
                self.df[newCol]=None
                self.df.to_csv(f"may9/sampleCSV/{self.currentfile}",index=False)


            else:
                return
    def insertValues(self):
        if self.df is None:
            print("file is not loaded")
            return
        print(f"working on the file {self.currentfile}")
        new_row = {}
        for col in self.df.columns:
            new_row[col] = input(f"Enter value for {col} >>> ")
        self.df.loc[len(self.df)] = new_row
        self.df.to_csv(f"may9/sampleCSV/{self.currentfile}", index=False)
    def showData(self):
        if self.df is None:
            print("file is not loaded")
            return
        else:
            print(self.df)
            #self.df.to_csv(f"may9/sampleCSV/{self.currentfile}", index=False)
        #print("Row inserted and file saved.")


            


def main():
    print("welcom to CSV analyzer ")
    csv=CSVanalyzer()
    while True:
        x=input("1.create new CSV\n2.load CSV\n3.add columns\n4.inser values\n5.show csv\n6.exit\n>>")
        if x=="1":
        
            csv.createCSV()
        elif x=="2":
            csv.loadCSV()
        elif x=="3":
            csv.AddColums()
        elif x=="4":
            csv.insertValues()
        elif x=="5":
            csv.showData()
        elif x=="6":

            print("Leaving the CLI")
            break
        else:
            print("invalid choice")
if __name__=="__main__":
    main()

        
        

