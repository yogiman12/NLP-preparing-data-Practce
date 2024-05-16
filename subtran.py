# from pprint import pprint
# from google import 
# sub : list =[]
# with open ('Love.Lies.Bleeding.2024.WEBRip.srt','r') as f :
#     # number = f.readline()
#     # time = f.readline()
#     # caption = f.readline()
#     data :list[str] = f.readlines()
# data2= [i.replace('\n','') for i in data   ]
# data2[0]="1"
# # print(data2)
# line :list = []
# for i in data2 :
#     if i == "":
#         sub.append({"n":int(line[0]),"time":line[1],'text':line[2:]})
        
#         line=[]
#     else : line.append(i)
# print(sub[0]['text'])
# https://translatepress.com/docs/automatic-translation/generate-google-api-key/
from googletrans import Translator

def translate_text(text, source_lang, target_lang):
    translator = Translator()
    translated = translator.translate(text, src=source_lang, dest=target_lang)
    return translated.text

text_to_translate = "Hello, how are you?"
source_language = "en"
target_language = "fr"
p = translate_text(text_to_translate, source_language, target_language)
print(p)