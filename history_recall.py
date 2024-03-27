class history:
    def __init__(self):
        self.chat = {str:str}

    def history_add(self, chapter, text):
        self.chat[chapter] = text

    def history_return(self):
        return(self.chat)
    
    
    
    def histore(text):
        hisfile = open('history.txt', 'a')
        hisfile.write(text)
        hisfile.write("\n")
        hisfile.write(text)
        hisfile.close()

