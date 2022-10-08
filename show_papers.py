"""
streamlitを使って取得してあるpaparsを表示する
"""
import os 
import datetime
import streamlit as st
st.set_page_config(page_title="Show Papers",page_icon=":memo:")

def init():
    global papers
    papers = os.listdir("papers")

    global papers_size
    papers_size = {}
    papers_size["All"] = len(papers)
    papers_size["Sorted"] = len(papers)

    _sort_papers_list()

def side_bar():
    global select
    with st.sidebar:
        st.sidebar.write("Mode")
        select = st.selectbox("Select show mode.",
                             ("All","Sorted","cs.CV","cs"),
                             )

        st.write(f"Number of papers in \"{select}\" category: {papers_size[select]}")

def _sort_papers_list():
    global papers_dict
    cscv_size = 0
    cs_size = 0
    papers_dict = {}
    for paper in papers:
        papers_path = "papers/" + paper + "/" 
        with open(papers_path + "metainfo.txt","r") as info:
            _,date,_,category,_ = info.readlines()
            time = datetime.datetime.strptime(date[:-1],"%Y-%m-%d")
            date = time.date()

        # count each category papers size
        if "cs" in category:
            cs_size += 1
        if "cs.CV" in category:
            cscv_size += 1

        papers_dict[paper] = date
    
    # memory category papers size
    papers_size["cs"] = cs_size
    papers_size["cs.CV"] = cscv_size

    papers_dict = sorted(papers_dict.items(),key=lambda x:x[1], reverse=True)

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

def show_sorted_papers():
    for dicted_paper in papers_dict:
        papers_path = "papers/" + dicted_paper[0] + "/"
        with open(papers_path + "metainfo.txt","r") as info:
            title,date,url,category,_ = info.readlines()
        with open(papers_path + "abstract.txt","r") as abst:
            abstract = abst.read()

        categories = category[1:-2]
        _show_paper(title=title,date=date,url=url,category=categories,abstract=abstract)

def show_specific_category_papers(target):
    for dicted_paper in papers_dict:
        papers_path = "papers/" + dicted_paper[0] + "/" 
        with open(papers_path + "metainfo.txt","r") as info:
            title,date,url,category,_ = info.readlines()
        with open(papers_path + "abstract.txt","r") as abst:
            abstract = abst.read()
    
        categories = category[1:-2]
        if target in categories:
            _show_paper(title=title,date=date,url=url,category=categories,abstract=abstract)


def main_page():
    init() 
    side_bar()
    if select == "All":
        show_all_papers()
    elif select == "Sorted":
        show_sorted_papers()
    elif select == "cs.CV":
        show_specific_category_papers(target = "cs.CV")
    elif select == "cs":
        show_specific_category_papers(target = "cs")

main_page()