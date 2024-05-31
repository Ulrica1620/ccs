import streamlit as st
from PIL import Image
import os
dir_path = os.path.split(os.path.realpath(__file__))[0]
import sys
sys.path.append(dir_path)

st.set_page_config(
    page_title="音综战绩",
    page_icon=":Scroll:",
    layout='wide'
)

st.title('🎉 音综战绩')

st.subheader('Introduction')
st.markdown(
    """
    DeepFloyd IF is a state-of-the-art text-to-image model released by StabilityAI in late April, 2023 that achieves a high degree of photorealism and language understanding. DeepFloyd is built with multiple neural modules (independent neural networks that tackle specific tasks), and generates high-resolution images in a cascading approach. The model is composed of a frozen text encoder and three cascaded pixel diffusion modules: a base model that generates 64x64 pixel image based on the input text prompt and two super-resolution models that generates images with resolution 256x256 pixel and 1024x1024 pixel. All stages of the model utilize a frozen text encoder based on the T5-XXL to extract text embeddings, which are then fed into a UNet architecture enhanced with cross-attention and attention pooling. 
    \n
    As a result, DeepFloyd achieves a zero-shot Frechet Inception Distance (FID) score of 6.66 on the COCO dataset, which outperforms other novel text-to-image models including DALL-E 2 (10.39), Imagen (7.27), and eDiff-I (6.95).

    **The following generation flowchart demonstrates the three-stage process**:
    \n

    - A **text prompt** is passed through the frozen T5-XXL language model to convert into a qualitative text representation
    \n
    - **Stage 1**: A base diffusion model transforms the qualitative text into a 64x64 image. There are three versions of the base model each with different number of parameters: 400M, 900M, and 4.3B. 
    \n
    - **Stage 2**: To upscale the image, two text-conditional super-resolution models are applied to the output of the base model. The first super-resolution model upscales the 64x64 image to 256x256. 
    \n
    - **Stage 3**: The second super-resolution diffusion model is applied and produces a 1024x1024 image.
    """
)

tab1, tab2, tab3, tab4 = st.tabs(["披荆斩棘3", "声生不息家年华", "天赐的声音5","一起来看我们的演唱会"])



with tab1:
    st.subheader("1. 披荆斩棘成团哥哥 各平台数据汇总")
    a1, a2,a3 = st.columns([1,8,1])   
    a2.markdown('''<img src="https://github.com/Ulrica1620/ccs/blob/main/image/%E6%89%B9%E5%93%A5%E6%B1%87%E6%80%BB.jpg?raw=true" width="1000"/>''',unsafe_allow_html=True)
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
        c1, c2,c3 = st.columns([1,8,1])        
        c2.markdown('''<img src="https://github.com/Ulrica1620/ccs/blob/main/image/%E6%89%B9%E5%93%A5_%E6%88%98%E7%BB%A97.jpg?raw=true" width="600"/>''', unsafe_allow_html=True)
    
    with a5.expander("🫘 赛前&赛后，抖音数据变化 Cr.豆瓣 今天吃素🍖"):
        c1, c2,c3 = st.columns([1,8,1])        
        c2.markdown('''<img src="https://github.com/Ulrica1620/ccs/blob/main/image/%E6%89%B9%E5%93%A5_%E6%88%98%E7%BB%A98.jpg?raw=true" width="600"/>''', unsafe_allow_html=True)

with tab2:
    st.subheader("1. 声生不息家年华 各平台舞台数据汇总")
    c1, c2 = st.columns(2)
    with c1.expander("🎉 声生不息三季 b站百万舞台数据汇总 Cr.豆瓣 今天吃素🍖"):
        a1, a2,a3 = st.columns([1,8,1])   
        a2.markdown('''<img src="https://github.com/Ulrica1620/ccs/blob/main/image/%E5%A3%B0%E7%94%9F%E4%B8%8D%E6%81%AF_%E6%88%98%E7%BB%A92.jpg?raw=true" width="800"/>''',unsafe_allow_html=True)
    with c2.expander("🎉 声生不息三季 b站百万舞台嘉宾统计汇总 Cr.豆瓣 今天吃素🍖"):
        a1, a2,a3 = st.columns([1,8,1])   
        a2.markdown('''<img src="https://github.com/Ulrica1620/ccs/blob/main/image/%E5%A3%B0%E7%94%9F%E4%B8%8D%E6%81%AF_%E6%88%98%E7%BB%A91.jpg?raw=true" width="800"/>''',unsafe_allow_html=True)
    st.markdown('\n')
    with st.expander("🎉 声生不息家年华 Q音、网易云、酷狗统计汇总 Cr.豆瓣 今天吃素🍖"):
        a1, a2,a3 = st.columns([1,8,1])   
        a2.markdown('''<img src="https://github.com/Ulrica1620/ccs/blob/main/image/%E5%A3%B0%E7%94%9F%E4%B8%8D%E6%81%AF_%E6%88%98%E7%BB%A93.jpg?raw=true" width="1000"/>''',unsafe_allow_html=True)
    st.markdown('\n')
    st.markdown('\n')
    st.subheader("2. 声生不息家年华 嘉宾涨粉数据汇总")
    c1, c2 = st.columns(2)
    with c1.expander("🎉 Q音、网易云、酷狗涨粉 数据汇总 Cr.豆瓣 今天吃素🍖"):
        a1, a2,a3 = st.columns([1,8,1])   
        a2.markdown('''<img src="https://github.com/Ulrica1620/ccs/blob/main/image/%E5%A3%B0%E7%94%9F%E4%B8%8D%E6%81%AF_%E6%88%98%E7%BB%A94.jpg?raw=true" width="800"/>''',unsafe_allow_html=True)
    with c2.expander("🎉 抖音涨粉 数据汇总 Cr.豆瓣 今天吃素🍖"):
        a1, a2,a3 = st.columns([1,8,1])   
        a2.markdown('''<img src="https://github.com/Ulrica1620/ccs/blob/main/image/%E5%A3%B0%E7%94%9F%E4%B8%8D%E6%81%AF_%E6%88%98%E7%BB%A95.jpg?raw=true" width="800"/>''',unsafe_allow_html=True)

    st.markdown('\n')
    st.markdown('\n')
    st.subheader("3. 声生不息家年华 陈楚生工作室战报")
    c1, c2 = st.columns(2)
    with c1.expander("🧣 陈楚生工作室战报（1/2） Cr.微博 陈楚生工作室"):
        a1, a2,a3 = st.columns([1,8,1])   
        a2.markdown('''<img src="https://github.com/Ulrica1620/ccs/blob/main/image/%E5%A3%B0%E7%94%9F%E4%B8%8D%E6%81%AF_%E6%88%98%E7%BB%A96.jpg?raw=true" width="800"/>''',unsafe_allow_html=True)
    with c2.expander("🧣 陈楚生工作室战报（2/2） Cr.微博 陈楚生工作室"):
        a1, a2,a3 = st.columns([1,8,1])   
        a2.markdown('''<img src="https://github.com/Ulrica1620/ccs/blob/main/image/%E5%A3%B0%E7%94%9F%E4%B8%8D%E6%81%AF_%E6%88%98%E7%BB%A97.jpg?raw=true" width="800"/>''',unsafe_allow_html=True)


with tab3:
   st.header("An owl")
   st.image("./image/批哥_战绩1.jpg", width=200)
