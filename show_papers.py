"""
streamlitを使って取得してあるpaparsを表示する
"""
import os 
import streamlit as st

# とりあえず全部表示させてみるか
papers = os.listdir("papers")
for paper in papers:
    papers_path = "papers/" + paper + "/" 
    with open(papers_path + "metainfo.txt","r") as info:
        title,date,url,_ = info.readlines()
        print(title)
        print(date)
    with open(papers_path + "abstract.txt","r") as abst:
        abstract = abst.read()
    
    st.title(title)
    st.write(date)
    st.write(url)
    st.write(abstract)