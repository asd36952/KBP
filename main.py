import load
import time

DOC_PATH="/home/asd36952/KBP/Data/document/"
DIR_LIST_PATH="/home/asd36952/KBP/Data/LDC2015E45_TAC_KBP_Comprehensive_English_Source_Corpora_2009-2014/docs/all_zipid_docid_evalyrs.tab"
listFile=open(DIR_LIST_PATH)
DIR_LIST=listFile.read().split()
listFile.close()

if __name__=="__main__":
    t=time.time()
    #load.loadDocs(DIR_LIST,DOC_PATH)
    wordList=load.makeDict(DIR_LIST,DOC_PATH)
    #print(load.countDoc(DIR_LIST,DOC_PATH))
    t=time.time()-t
    print(t)
