
import pandas as pd
import numpy as np


class csvAnalyzer(object): 
    def __init__(self):

        self.defaultFile="may8/sales_data_sample.csv"
        self.currentFile=self.defaultFile
        self.columns=None
        self.df=None
    def loadFile(self):
        flag=input(f"do you want to load the default file {self.defaultFile} [Y/N] ")
        if flag=="Y":
            self.df=pd.read_csv(self.defaultFile ,encoding='latin1')
            
            self.columns=self.df.columns
            print("file loaded")
            #return self.df
        else:
            filename=input("enter the file name ")
            self.currentFile="may8/"+filename
            try:
                self.df=pd.read_csv(self.currentFile)
                print("file loaded")
                #return self.df
            except FileNotFoundError:
                print("file not found")
        
        return self.df
    def getColumns(self):
        if self.df is None:
            print("file not loaded")
            return None
        else:
            self.columns=self.df.columns
            for i in range(len(self.columns)):
                print(f"{i} : {self.columns[i]}")
            return self.columns
    def showDataSet(self):
        if self.df is None:
            print("file not loaded")
            return None
        else:
            x=input("do you want to see the first 5 rows of the dataset [Y/num] if no enter Number of rows to see ")
            if x=="Y":
                print(self.df.head())
            elif x.isnumeric():
                x=int(x)
                if x>0:
                    print(self.df.head(x))
                else:
                    print("invalid number")
            else:
                print("invalid input")
    def InsertRow(self):
        if self.df is None:
            print("file not loaded")
            return None
        else:
            row = {}
            for i in range(len(self.columns)):
                col=self.columns[i]
                val=input(f"enter the value for {col} : ")
                row[col]=val
            self.df=self.df.append(row, ignore_index=True)
            print("row inserted")
            return self.df
    def showInfo(self):
        if self.df is None:
            print("file not loaded")
            return None
        else:
            print(self.df.info())
def main():
    obj=csvAnalyzer()
    obj.loadFile()
    while True:
        print("1. show columns")
        print("2. show dataset")
        print("3. insert row")
        print("4. show info")
        print("5. exit")
        choice=input("enter your choice : ")
        if choice=="1":
            obj.getColumns()
        elif choice=="2":
            obj.showDataSet()
        elif choice=="3":
            obj.InsertRow()
        elif choice=="4":
            obj.showInfo()
        elif choice=="5":
            break
        else:
            print("invalid choice")

if __name__=="__main__":
    main()
