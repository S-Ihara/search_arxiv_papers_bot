import arxiv

def get_papers(query,max_num=10):
    search = arxiv.Search(
        query = query,
        max_results = max_num,
        sort_by = arxiv.SortCriterion.SubmittedDate
    )

    return search

if __name__ == "__main__":
    papers = get_papers(query="interpretable",max_num=10)
    for paper in papers.results():
        print(paper.title)
        print(paper.published)

    """
    paper = next(papers.results())
    print(paper.title)
    print(paper.entry_id)
    print(paper.published)
    print(paper.updated)
    print(paper.summary)
    """
