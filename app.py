import streamlit as st
import requests
import json
import pandas as pd

page=st.sidebar.selectbox("choose your page",["ナレッジ検索","登録画面","登録内容"])
if page=="登録内容":

    url_clouds = "http://172.25.75.45:8000/clouds"
    res =requests.get(url_clouds)
    clouds = res.json()
    df_clouds = pd.DataFrame(clouds)
    st.write("")
    st.table(df_clouds)

if page=="登録画面":
    st.write("## クラウド障害管理システム")

    with st.form(key="cloud"):
        # booking_id: int =random.randint(0,10)
        title: str = st.text_input("題名")
        cloud_service: str = st.selectbox("クラウド情報",["AWS","Pega","Azure"])
        user_name: str =st.text_input("報告者")
        desc : str = st.text_area("内容")
    
        submit_button = st.form_submit_button(label="ナレッジ登録")

    if submit_button:
        data={
            # "booking_id": booking_id,
            "title": title,
            "cloud_service": cloud_service,
            "user_name": user_name,
            "desc" : desc
            

        }
        st.write("## 送信データ")
        st.json(data)
        st.write("## レスポンス結果")
        url="http://172.25.75.45:8000/clouds"
        res=requests.post(
            url,
            data=json.dumps(data)
        )
        if res.status_code == 200:
            st.write(res.json())
            st.success("予約が成功しました")
        st.write(res.status_code)
        st.json(res.json())

# if page=="ナレッジ検索":
#     st.write("## ナレッジ検索")

#     with st.form(key="cloud"):
#         # booking_id: int =random.randint(0,10)
#         title: str = st.text_input("検索ワード")
#         submit_button = st.form_submit_button(label="検索")
#     if submit_button:
#         url_clouds = "http://172.25.75.45:8000/clouds"
#         res =requests.get(url_clouds)
#         clouds = res.json()
        
#         i=0
#         for t in clouds:
#             a=(clouds[i]["title"])
#             b=(clouds[i]["cloud_service"])
#             c=(clouds[i]["user_name"])
#             d=(clouds[i]["desc"])
#             e=(clouds[i]["cloud_id"])
#             i=i+1
#             if title in a or title in b or title in c or title in d:
#                 # st.write(clouds[e-1])
#                 clouds[e-1]

if page=="ナレッジ検索":
    st.write("## ナレッジ検索")

    with st.form(key="cloud"):
        # booking_id: int =random.randint(0,10)
        title: str = st.text_input("検索ワード")
        submit_button = st.form_submit_button(label="検索")
    if submit_button:
        url_clouds = "http://172.25.75.45:8000/clouds/" +title
        res =requests.get(url_clouds)
        # st.write(res.status_code)
        clouds = res.json()
        # st.write(clouds)
        df_clouds = pd.DataFrame(clouds)
        st.write("")
        st.table(df_clouds)
        
        