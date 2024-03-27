class history:

    
    
    
    def histore(text):
        hisfile = open('history.txt', 'a')
        hisfile.write(text)
        hisfile.write("\n")
        hisfile.write(text)
        hisfile.close()

