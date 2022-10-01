import arxiv

def get_papers(query,max_num=10):
    search = arxiv.Search(
        query = query,
        max_results = max_num,
        sort_by = arxiv.SortCriterion.SubmittedDate
    )

    return search


if __name__ == "__main__":
    query = "cat:cs.* AND (ti:explain OR abs:explain)"
    papers = get_papers(query=query,max_num=5)
    for paper in papers.results():
        print(paper.title)
        print(paper.categories)
        print(paper.primary_category)
        print(paper.published)

    #print("deepl test")
    #print(translate_into_japanese("test"))
    """
    paper = next(papers.results())
    print(paper.title)
    print(paper.entry_id)
    print(paper.published)
    print(paper.updated)
    print(paper.summary)
    """
