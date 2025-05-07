import os
class WordsInFIle(object):
    def __init__(self,filename=None):
        self.filename = filename
        self.wordCount = {}
        self.words=[]
        
    def readFile(self):

        try:

            if self.filename is None:
                name = "may7/"+input("Enter the file name: ")
                self.filename = name


            with open(self.filename, 'r') as file:
                
                text = file.read()

                

                for word in text.split():
                    word = word.strip('.,!?()[]{};:"\'')
                    self.words.append(word.lower())
            return True
        except FileNotFoundError:
            print(f"Error: The file '{self.filename}' was not found.")
            return False
    def countWords(self):
        for word in self.words:
            if word in self.wordCount:
                self.wordCount[word] += 1
            else:
                self.wordCount[word] = 1
    def printWordCount(self):
        for word, count in self.wordCount.items():
            print(f"{word}: {count}")
    def setNewFile(self, filename=None):
        self.filename = "may7/"+input("Enter the new file name: ") 
        self.wordCount = {}
        self.words = []
        print(f"File set to {self.filename}")

def main():
    
    word_counter = WordsInFIle()
    print("Welcome to the Word Frequency Counter")
    while True:
        choice=input("1.load file\n2.count words\n3.print word count\n4.set New File\n5.exit\nEnter your choice: ")

        if choice=='1':
            word_counter.readFile()
        elif choice=='2':
            word_counter.countWords()
        elif choice=='3':
            word_counter.printWordCount()
        elif choice=='4':
            word_counter.setNewFile()
        elif choice=='5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()

        
        