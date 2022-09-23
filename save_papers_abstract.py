import os

def _get_available_title(title):
    # ディレクトリに使えない文字を置き換える
    if ":" in title:
        title = title.replace(":",";")
    
    return title


def create_paper_directory(title):
    new_flag = False

    title = _get_available_title(title)
    if not os.path.exists("./papers/" + title):
        os.mkdir("./papers/" + title)
        new_flag = True
    
    return new_flag

def save_papers_abstract(abst,title):
    title = _get_available_title(title)
    with open("./papers/" + title + "/abstract.txt","w") as f:
        f.write(abst)


if __name__ == "__main__":
    if not os.path.exists("./papers"):
        os.mkdir("./papers")
    title = "test"
    abst = "テストだよ。"
    create_paper_directory(title)
    save_papers_abstract(abst,title)