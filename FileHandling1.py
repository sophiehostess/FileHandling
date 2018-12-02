
#!/usr/bin/python
# -*- coding: utf-8 -*-
# Read file, line by line
f = open("C:/Users/aiwuj_000/OneDrive/Python/FileHandling/FileHandling1.py")  
while True:
    text = f.readline()    
    if text:
        print(text)
    else:  
        print(len(text))
        break
f.close()  







