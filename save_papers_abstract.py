import os
import requests

from settings import API_KEY

def _save_papers_abstract(abst,title):
    with open("./papers/" + title + "/abstract.txt","w") as f:
        try:
            f.write(abst)
        except UnicodeEncodeError as e:
            f.write("failed")
            print("error:",e)
            print(abst)
            pass

def _save_papers_metainfo(metainfo,title):
    with open("./papers/" + title + "/metainfo.txt","w") as f:
        f.write(metainfo.title + "\n")
        f.write(str(metainfo.published) + "\n")
        f.write(metainfo.url + "\n")
        category_str = str(metainfo.category).replace("'","")
        f.write(category_str + "\n")
        try:
            f.write(metainfo.summary.replace("\n"," "))
        except UnicodeEncodeError as e:
            print("error:",e)
            print(metainfo.summary)
            pass

def _translate_into_japanese(text):
    source_lang = "EN"
    target_lang = "JA"
    
    params = {
        "auth_key"    : API_KEY,
        "text"        : text,
        "source_lang" : source_lang,
        "target_lang" : target_lang,
    }

    request = requests.post("https://api-free.deepl.com/v2/translate", data=params)
    result = request.json()

    translated_text = result["translations"][0]["text"]
    return translated_text 


def save_papers(paperinfo):
    new_flag = False
    title = paperinfo.title
    # ディレクトリに使えない文字を置き換える
    if ":" in title:
        title = title.replace(":",";")
    
    if "\\" in title:
        title = title.replace("\\","")
    
    if "\"" in title:
        title = title.replace("\"","\'")
    
    if "?" in title:
        title = title.replace("?","？")

    if "*" in title:
        title = title.replace("*",".")
    
    if "/" in title:
        title = title.replace("/",",")

    if not os.path.exists("./papers/" + title):
        os.mkdir("./papers/" + title)
        new_flag = True

        translated = _translate_into_japanese(paperinfo.summary.replace("\n"," "))
        _save_papers_abstract(translated,title)
        _save_papers_metainfo(paperinfo,title)
    
    return new_flag

if __name__ == "__main__":
    if not os.path.exists("./papers"):
        os.mkdir("./papers")
    title = "test"
    abst = "テストだよ。"

    _save_papers_abstract(abst,title)