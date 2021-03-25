#Create a function that returns the whole of the first sentence which contains a specific word. Include the full stop at the end of the sentence.
def Sentence_searcher(txt,fltr):
    txt = txt.split('.')
    for snt in txt :
        if fltr.lower() in snt.lower() :
            return snt+'.'
    return ''

res = sentence_searcher('I have a cat. I have a mat. Things are going swell.','cat')
res2= sentence_searcher('I have a cat. I have a mat. Things are going swell.','mat')
res3 = sentence_searcher('I have a cat. I have a mat. Things are going swell.','swell')
print(res)
print(res2)
print(res3)
print(res+res2)
#this is a training






