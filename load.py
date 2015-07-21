from bs4 import BeautifulSoup
import nltk

def loadDocs(DIR_LIST,DOC_PATH):
    count=0
    while(count<len(DIR_LIST)):
        try:
            docFile=open(DOC_PATH+DIR_LIST[count]+"/"+DIR_LIST[count+1])
        except FileNotFoundError:
            docFile=open(DOC_PATH+DIR_LIST[count]+"/"+DIR_LIST[count+1]+".LDC2009T13")
        #print(DIR_LIST[count])
        #print(DIR_LIST[count+1])
        soup=BeautifulSoup(docFile.read())
        docFile.close()
        docId=soup.find("docid")
        if(docId==None):
            docId=soup.find('doc')['id']
        else:
            docId=docId.text
        print(docId)
        docType=soup.find("doctype")
        source=""
        if(docType!=None):
            source=docType["source"]
            print(docType.text)
        else:
            docType=soup.find("doc")['type']
            print(docType)
        datetime=soup.find('datetime')
        if(datetime!=None):
            print(datetime.text)
        else:
            pass        #### datetime
        headline=soup.find('headline')
        if(headline!=None):            
            print(headline.text)
        docContent=""
        if(source=="broadcast news"):
            for m in soup.find_all("turn"):
                m.speaker.extract()
                docContent=docContent+m.text
        else:
            for m in soup.find_all("text"):
                docContent=docContent+m.text
        print(docContent)

        count=count+3
        print("==============================================================================================")

    return

def makeDict(DIR_LIST,DOC_PATH):
    count=0
    fileNumber=0
    wordList={}
    listFile=open("/home/asd36952/KBP/code/docList"+str(fileNumber)+".txt","w")
    while(count<len(DIR_LIST)):
        try:
            docFile=open(DOC_PATH+DIR_LIST[count]+"/"+DIR_LIST[count+1])
        except FileNotFoundError:
            try:
                docFile=open(DOC_PATH+DIR_LIST[count]+"/"+DIR_LIST[count+1]+".LDC2009T13")
            except FileNotFoudError:
                print("File not found : "+DOC_PATH+DIR_LIST[count]+"/"+DIR_LIST[count+1])
        soup=BeautifulSoup(docFile.read())
        docFile.close()
        docId=soup.find("docid")
        if(docId==None):
            docId=soup.find('doc')['id']
        else:
            docId=docId.text
        docType=soup.find("doctype")
        source=""
        if(docType!=None):
            source=docType["source"]
        docContent=""
        if(source=="broadcast news"):
            for m in soup.find_all("turn"):
                m.speaker.extract()
                docContent=docContent+m.text
        else:
            for m in soup.find_all("text"):
                docContent=docContent+m.text
        docContent=docContent.casefold()
        docContent=nltk.word_tokenize(docContent)
        docContent=set(docContent)
        for word in docContent:
            if(wordList.get(word)==None):
                wordList[word]=[DIR_LIST[count]+"/"+DIR_LIST[count+1]]
            else:
                wordList[word].append(DIR_LIST[count]+"/"+DIR_LIST[count+1])
        count=count+3
        if(int(count/800000)>fileNumber):
            for k in wordList.keys():
                listFile.write(k)
                listFile.write(":")
                for d in wordList.get(k):
                    listFile.write(d)
                    listFile.write(",")
                listFile.write("\n")
            wordList={}
            fileNumber=fileNumber+1
            listFile.close()
            listFile=open("/home/asd36952/KBP/code/docList"+str(fileNumber)+".txt","w")
    listFile.close()
    return wordList

def countDoc(DIR_LIST,DOC_PATH):
    count=0
    while(count<len(DIR_LIST)):
        try:
            docFile=open(DOC_PATH+DIR_LIST[count]+"/"+DIR_LIST[count+1])
        except FileNotFoundError:
            try:
                docFile=open(DOC_PATH+DIR_LIST[count]+"/"+DIR_LIST[count+1]+".LDC2009T13")
            except FileNotFoundError:
                print("File not found : "+DOC_PATH+DIR_LIST[count]+"/"+DIR_LIST[count+1])
        count=count+3
    return count/3

def findKeyword(keyword):
    fileNumber=0
    DOC_PATH=[]
    try:
        while(True):
            listFile=open("/home/asd36952/KBP/code/docList"+str(fileNumber)+".txt","r")
            wordList=listfile.readlines()
            for line in wordList:
                line=line.split(":")
                if(line[0]==keyword):
                    line=line[1].split("\n")[0].split(",")
                    for path in line:
                        DOC_PATH.append(path)
                    break
            fileNumber=fileNumber+1
    except FileNotFoundError:
        pass
    return DOC_PATH



#
#    if(docId==None):
#        docId=root.attrib['id']
#    print(docId)
#    docType=root.findtext("DOCTYPE")
#    if(docType==None):
#        docType=root.attrib["type"]
#    datetime=root.findtext("DATETIME")
#    docContent("")
#    if(root.find("BODY")!=None):
#        headline=root.find("BODY").findtext("HEADLINE")
#        for m in root.find("BODY").find("TEXT"):
#            docContent=docContent+m.text
#    else:
#        headline=root.findtext("HEADLINE")
#        for m in root.find("TEXT"):
#            docContent=docContent+m.text
#
#    print(docType)
#    print(datetime)
#    print(headline)
#    print(docContent)


