import streamlit as st
import requests 
header={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
st.title("YouTube Thumbnail Downloder")
link =st.text_input('Paste YouTube Video Link',"Here")

def video_id(l):
    if '=' in l:
        linklist=l.split("=")
        return linklist[1]
    elif 'be/' in l :
        linklist=l.split("be/")
        return linklist[1] 
    else:
        st.header("Enter right link")
        return 'None'
        
videoid =video_id(link)



if videoid !="None" :
        
    with st.spinner('Wait for it...'):
    

        
        res=requests.get(f"https://i.ytimg.com/vi/{videoid}/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBDJPxmsT62J34dKnpQTuoiDmS5Bw",headers=header)
        if res.status_code ==200:
             # col1 = st.columns()
                # with col1:
                st.header("Your ThumbNail")
                st.image(res.content)
                btn = st.download_button(
                                label="Download Thumb",
                                data=res.content,
                                file_name="tumbnail.jpg",
                                mime="image/png")
        
