"""
streamlitを使って取得してあるpaparsを表示する
"""
import os 
import streamlit as st
st.set_page_config(page_title="Show Papers",
                       page_icon=":memo:")

def init():
    global papers
    papers = os.listdir("papers")

    global papers_size
    paper_size = len(papers)

def side_bar():
    global select
    with st.sidebar:
        st.sidebar.write("Mode")
        select = st.selectbox("Select show mode.",
                             ("All","Sorted","cs.CV","cs"),
                             )

        st.write(select)

def _show_paper(**kwargs):
    st.title(kwargs["title"])
    st.write(kwargs["date"])
    st.write(kwargs["url"])
    st.write(kwargs["category"])
    st.write(kwargs["abstract"])

def show_all_papers():
    # 雑に全部表示
    for paper in papers:
        papers_path = "papers/" + paper + "/" 
        with open(papers_path + "metainfo.txt","r") as info:
            title,date,url,category,_ = info.readlines()
        with open(papers_path + "abstract.txt","r") as abst:
            abstract = abst.read()
        
        categories = category[1:-2]
        categories_list = categories.split(",")
        _show_paper(title=title,date=date,url=url,category=categories,abstract=abstract)


def show_specific_category_papers(target):
    for paper in papers:
        papers_path = "papers/" + paper + "/" 
        with open(papers_path + "metainfo.txt","r") as info:
            title,date,url,category,_ = info.readlines()
        with open(papers_path + "abstract.txt","r") as abst:
            abstract = abst.read()
    
        categories = category[1:-2]
        #categories_list = categories.split(",")

        if target in categories:
            _show_paper(title=title,date=date,url=url,category=categories,abstract=abstract)


def main_page():
    init()
    side_bar()
    if select == "All":
        show_all_papers()
    elif select == "Sorted":
        # TODO
        pass
    elif select == "cs.CV":
        show_specific_category_papers(target = "cs.CV")
    elif select == "cs":
        show_specific_category_papers(target = "cs")

main_page()