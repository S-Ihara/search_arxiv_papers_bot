import os
import argparse
import datetime
from dataclasses import dataclass

from get_papers import get_papers
from save_papers_abstract import save_papers
from settings import Search_Querys

@dataclass
class Paperinfo:
    title: str
    url: str
    published: datetime.date
    summary: str
    category: list

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

def main(size=10):
    if not os.path.exists("./papers"):
        os.mkdir("./papers")

    cnt = 0
    for query in Search_Querys:
        papers = get_papers(query=query,max_num=size)
        for paper in papers.results():
            title = paper.title
            summary = paper.summary
            published = paper.published.date()
            paper_url = paper.entry_id
            category = paper.categories
            paperinfo = Paperinfo(title,paper_url,published,summary,category)

            new_check = save_papers(paperinfo)
            cnt += new_check

    print(f"{cnt} papers are added.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("--size","-S",type=int,default=10,help="Number of search papers for each query")
    args = parser.parse_args()

    main(size=args.size)
