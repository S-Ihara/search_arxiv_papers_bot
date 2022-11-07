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

    if "init" not in st.session_state:
        st.session_state["init"] = True
        st.session_state["num_papers_show"] = 10
        st.session_state["start_index"] = 0
        st.session_state["end_index"] = min(st.session_state["num_papers_show"],papers_size["All"])

    _sort_papers_list()

def side_bar():
    global select
    global pages
    with st.sidebar:
        st.sidebar.write("Mode")
        select = st.selectbox("Select show mode.",
                             ("All","Sorted","cs.CV","cs.LG","cs"),
                             )

        st.write(f"Number of papers in \"{select}\" category: {papers_size[select]}")

        # 改ページ機能
        num_pages = papers_size[select] // st.session_state["num_papers_show"]
        pages = st.number_input("Pages",
                                min_value=0,
                                max_value=num_pages)
        st.session_state["start_index"] = pages * st.session_state["num_papers_show"]
        st.session_state["end_index"] = min(st.session_state["start_index"] + st.session_state["num_papers_show"],papers_size[select])
        st.write(f"pages : {0} - {num_pages}")

def _sort_papers_list():
    global papers_dict
    cscv_size = 0
    cslg_size = 0
    cs_size = 0
    papers_dict = {}
    for paper in papers:
        papers_path = "papers/" + paper + "/"
        with open(papers_path + "metainfo.txt","r") as info:
            try:
                _,date,_,category,_ = info.readlines()
                time = datetime.datetime.strptime(date[:-1],"%Y-%m-%d")
                date = time.date()
            except ValueError:
                # save時に失敗して何も書き込まなかったファイルをスルー
                continue

        # count each category papers size
        if "cs" in category:
            cs_size += 1
        if "cs.CV" in category:
            cscv_size += 1
        if "cs.LG" in category:
            cslg_size += 1

        papers_dict[paper] = date

    # memory category papers size
    papers_size["cs"] = cs_size
    papers_size["cs.CV"] = cscv_size
    papers_size["cs.LG"] = cslg_size

    papers_dict = sorted(papers_dict.items(),key=lambda x:x[1], reverse=True)

def _show_paper(**kwargs):
    st.title(kwargs["title"])
    st.write(kwargs["date"])
    st.write(kwargs["url"])
    st.write(kwargs["category"])
    st.write(kwargs["abstract"])

def show_all_papers():
    # 雑に全部表示
    start_index = st.session_state["start_index"]
    end_index = st.session_state["end_index"]
    for paper in papers[start_index:end_index]:
        papers_path = "papers/" + paper + "/"
        with open(papers_path + "metainfo.txt","r") as info:
            title,date,url,category,_ = info.readlines()
        with open(papers_path + "abstract.txt","r") as abst:
            abstract = abst.read()

        categories = category[1:-2]
        categories_list = categories.split(",")
        _show_paper(title=title,date=date,url=url,category=categories,abstract=abstract)

def show_sorted_papers():
    start_index = st.session_state["start_index"]
    end_index = st.session_state["end_index"]
    for dicted_paper in papers_dict[start_index:end_index]:
        papers_path = "papers/" + dicted_paper[0] + "/"
        with open(papers_path + "metainfo.txt","r") as info:
            try:
                title,date,url,category,_ = info.readlines()
            except ValueError:
                # save時に失敗して何も書き込まなかったファイルをスルー
                pass
        with open(papers_path + "abstract.txt","r") as abst:
            abstract = abst.read()

        categories = category[1:-2]
        _show_paper(title=title,date=date,url=url,category=categories,abstract=abstract)

def show_specific_category_papers(target):
    start_index = st.session_state["start_index"]
    end_index = st.session_state["end_index"]
    count = 0
    for dicted_paper in papers_dict:
        papers_path = "papers/" + dicted_paper[0] + "/"
        with open(papers_path + "metainfo.txt","r") as info:
            title,date,url,category,_ = info.readlines()
        with open(papers_path + "abstract.txt","r") as abst:
            abstract = abst.read()

        categories = category[1:-2]
        if target in categories:
            if start_index <= count < end_index:
                _show_paper(title=title,date=date,url=url,category=categories,abstract=abstract)
            count += 1

def main_page():
    init()
    side_bar()
    if select == "All":
        show_all_papers()
    elif select == "Sorted":
        show_sorted_papers()
    elif select == "cs.CV":
        show_specific_category_papers(target = "cs.CV")
    elif select == "cs.LG":
        show_specific_category_papers(target = "cs.LG")
    elif select == "cs":
        show_specific_category_papers(target = "cs")

main_page()
