import streamlit as st
from PIL import Image
import os
dir_path = os.path.split(os.path.realpath(__file__))[0]
import sys
import base64
sys.path.append(dir_path)

st.set_page_config(
    page_title="音综战绩",
    page_icon=":Scroll:",
    layout='wide'
)

st.title('🎉 音综战绩')

def main_bg(main_bg):
    main_bg_ext = "jpg"
    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )
 
#调用
main_bg('./image/background2.png')


st.header('介绍')
st.markdown(
    """
    本页统计陈楚生近期参与的各个音综的成绩，欢迎文笔较好的姐妹填补介绍部分，主页有联系方式，也可留言。
    \n
    """
)
st.header('数据汇总')
st.markdown('请点击下方对应的音综选项')
st.markdown('\n')
tab1, tab2, tab3, tab4 = st.tabs(["披荆斩棘3", "声生不息家年华", "天赐的声音5","一起来看我们的演唱会"])

with tab1:
    st.subheader("1. 披荆斩棘成团哥哥 各平台数据汇总")
    a1, a2,a3 = st.columns([1,8,1])   
    a2.markdown('''<img src="https://github.com/Ulrica1620/ccs/blob/main/image/%E6%89%B9%E5%93%A5%E6%B1%87%E6%80%BB.jpg?raw=true" width="1000" style="margin: 0 auto;"/>''',unsafe_allow_html=True)
    with st.expander("查看具体数据 Cr.豆瓣 和雨玟🌱"):
        c1, c2,c3 = st.columns([1,8,1])        
        c2.markdown('''<img src="https://github.com/Ulrica1620/ccs/blob/main/image/%E6%89%B9%E5%93%A5_%E6%88%98%E7%BB%A91.jpg?raw=true" width="800"/>''', unsafe_allow_html=True)

        c4, c5,c6 = st.columns([1,8,1])
        c5.markdown('''<img src="https://github.com/Ulrica1620/ccs/blob/main/image/%E6%89%B9%E5%93%A5_%E6%88%98%E7%BB%A92.jpg?raw=true" width="800"/>''', unsafe_allow_html=True)

        c7, c8,c9 = st.columns([1,8,1])
        c5.markdown('''<img src="https://github.com/Ulrica1620/ccs/blob/main/image/%E6%89%B9%E5%93%A5_%E6%88%98%E7%BB%A93.jpg?raw=true" width="800"/>''', unsafe_allow_html=True)

        c10, c11,c12 = st.columns([1,8,1])
        c5.markdown('''<img src="https://github.com/Ulrica1620/ccs/blob/main/image/%E6%89%B9%E5%93%A5_%E6%88%98%E7%BB%A94.jpg?raw=true" width="800"/>''', unsafe_allow_html=True)
    st.markdown('\n')
    st.markdown('\n')
    st.subheader("2. 披荆斩棘官方&陈楚生战报")
    a1, a2,a3 = st.columns([1,8,1])   
    a2.markdown('''<img src="https://github.com/Ulrica1620/ccs/blob/main/image/%E6%89%B9%E5%93%A5_%E6%88%98%E7%BB%A99.jpg?raw=true" width="1000"/>''',unsafe_allow_html=True)
    st.markdown('\n')
    st.markdown('\n')
    a4,a5,a6 = st.columns(3) 
    with a4.expander("🧣 工作室战报（1/3） Cr.微博 陈楚生工作室"): 
        st.markdown('''<img src="https://github.com/Ulrica1620/ccs/blob/main/image/%E6%89%B9%E5%93%A5_%E6%88%98%E7%BB%A910.jpg?raw=true" width="400"/>''', unsafe_allow_html=True)
    with a5.expander("🧣 工作室战报（2/3） Cr.微博 陈楚生工作室"): 
        st.markdown('''<img src="https://github.com/Ulrica1620/ccs/blob/main/image/%E6%89%B9%E5%93%A5_%E6%88%98%E7%BB%A911.jpg?raw=true" width="400"/>''', unsafe_allow_html=True)
    with a6.expander("🧣 工作室战报（3/3） Cr.微博 陈楚生工作室"): 
        st.markdown('''<img src="https://github.com/Ulrica1620/ccs/blob/main/image/%E6%89%B9%E5%93%A5_%E6%88%98%E7%BB%A912.jpg?raw=true" width="400"/>''', unsafe_allow_html=True)
    st.markdown('\n')
    st.markdown('\n')
    st.subheader("3. 披荆斩棘前后，各平台涨粉情况")
    a4,a5 = st.columns(2)  
    with a4.expander("🧣 赛前&赛后，微博粉丝&铁粉数量变化 Cr.豆瓣 今天吃素🍖"):
        c1, c2,c3 = st.columns([1,8,1])        
        c2.markdown('''<img src="https://github.com/Ulrica1620/ccs/blob/main/image/%E6%89%B9%E5%93%A5_%E6%88%98%E7%BB%A95.jpg?raw=true" width="600"/>''', unsafe_allow_html=True)
    with a5.expander("🧣 赛前&赛后，微博超话数据变化 Cr.豆瓣 今天吃素🍖"):
        c1, c2,c3 = st.columns([1,8,1])        
        c2.markdown('''<img src="https://github.com/Ulrica1620/ccs/blob/main/image/%E6%89%B9%E5%93%A5_%E6%88%98%E7%BB%A96.jpg?raw=true" width="600"/>''', unsafe_allow_html=True)
    a4.markdown('\n')
    a5.markdown('\n')
    with a4.expander("🍠 赛前&赛后，小红书数据变化 Cr.豆瓣 今天吃素🍖"):
        st.markdown('''<img src="https://github.com/Ulrica1620/ccs/blob/main/image/%E6%89%B9%E5%93%A5_%E6%88%98%E7%BB%A97.jpg?raw=true" width="600"/>''', unsafe_allow_html=True)
    
    with a5.expander("🫘 赛前&赛后，抖音数据变化 Cr.豆瓣 今天吃素🍖"):
        st.markdown('''<img src="https://github.com/Ulrica1620/ccs/blob/main/image/%E6%89%B9%E5%93%A5_%E6%88%98%E7%BB%A98.jpg?raw=true" width="600"/>''', unsafe_allow_html=True)

with tab2:
    st.subheader("1. 声生不息家年华 各平台舞台数据汇总")
    c1, c2 = st.columns(2)
    with c1.expander("🎉 声生不息三季 b站百万舞台数据汇总 Cr.豆瓣 今天吃素🍖"):
        st.markdown('''<img src="https://github.com/Ulrica1620/ccs/blob/main/image/%E5%A3%B0%E7%94%9F%E4%B8%8D%E6%81%AF_%E6%88%98%E7%BB%A92.jpg?raw=true" width="600"/>''',unsafe_allow_html=True)
    with c2.expander("🎉 声生不息三季 b站百万舞台嘉宾统计汇总 Cr.豆瓣 今天吃素🍖"):
        st.markdown('''<img src="https://github.com/Ulrica1620/ccs/blob/main/image/%E5%A3%B0%E7%94%9F%E4%B8%8D%E6%81%AF_%E6%88%98%E7%BB%A91.jpg?raw=true" width="600"/>''',unsafe_allow_html=True)
    st.markdown('\n')
    with st.expander("🎵 声生不息家年华 Q音、网易云、酷狗统计汇总 Cr.豆瓣 今天吃素🍖"):
        a1, a2,a3 = st.columns([1,8,1])   
        a2.markdown('''<img src="https://github.com/Ulrica1620/ccs/blob/main/image/%E5%A3%B0%E7%94%9F%E4%B8%8D%E6%81%AF_%E6%88%98%E7%BB%A93.jpg?raw=true" width="1000"/>''',unsafe_allow_html=True)
    st.markdown('\n')
    st.markdown('\n')
    st.subheader("2. 声生不息家年华 嘉宾涨粉数据汇总")
    with st.expander("🎵 Q音、网易云、酷狗涨粉 数据汇总 Cr.豆瓣 今天吃素🍖"):
        a1, a2,a3 = st.columns([1,8,1])   
        a2.markdown('''<img src="https://github.com/Ulrica1620/ccs/blob/main/image/%E5%A3%B0%E7%94%9F%E4%B8%8D%E6%81%AF_%E6%88%98%E7%BB%A94.jpg?raw=true" width="800"/>''',unsafe_allow_html=True)
    with st.expander("🫘 抖音涨粉 数据汇总 Cr.豆瓣 今天吃素🍖"):
        a1, a2,a3 = st.columns([1,8,1])   
        a2.markdown('''<img src="https://github.com/Ulrica1620/ccs/blob/main/image/%E5%A3%B0%E7%94%9F%E4%B8%8D%E6%81%AF_%E6%88%98%E7%BB%A95.jpg?raw=true" width="800"/>''',unsafe_allow_html=True)

    st.markdown('\n')
    st.markdown('\n')
    st.subheader("3. 声生不息家年华 陈楚生工作室战报")
    c1, c2 = st.columns(2)
    with c1.expander("🧣 陈楚生工作室战报（1/2） Cr.微博 陈楚生工作室"):
        st.markdown('''<img src="https://github.com/Ulrica1620/ccs/blob/main/image/%E5%A3%B0%E7%94%9F%E4%B8%8D%E6%81%AF_%E6%88%98%E7%BB%A96.jpg?raw=true" width="600"/>''',unsafe_allow_html=True)
    with c2.expander("🧣 陈楚生工作室战报（2/2） Cr.微博 陈楚生工作室"):
        st.markdown('''<img src="https://github.com/Ulrica1620/ccs/blob/main/image/%E5%A3%B0%E7%94%9F%E4%B8%8D%E6%81%AF_%E6%88%98%E7%BB%A97.jpg?raw=true" width="600"/>''',unsafe_allow_html=True)


with tab3:
   st.header("天赐的声音5")
   # st.image("./image/批哥_战绩1.jpg", width=200)
