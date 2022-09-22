import requests
import arxiv

from settings import API_KEY

def get_papers(query,max_num=10):
    search = arxiv.Search(
        query = query,
        max_results = max_num,
        sort_by = arxiv.SortCriterion.SubmittedDate
    )

    return search

def translate_into_japanese(text):
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


if __name__ == "__main__":
    papers = get_papers(query="interpretable",max_num=10)
    for paper in papers.results():
        print(paper.title)
        print(paper.published)

    print("deepl test")
    print(translate_into_japanese("test"))
    """
    paper = next(papers.results())
    print(paper.title)
    print(paper.entry_id)
    print(paper.published)
    print(paper.updated)
    print(paper.summary)
    """
