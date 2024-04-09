# 비디오 재생 예제

import streamlit as st

st.title("스트림릿의 비디오 재생 예")

# 유튜브 비디오 주소(URL)를 이용해 비디오 재생
st.subheader("2. 유튜브 비디오를 재생")

video_url = "https://www.youtube.com/watch?v=5VxYrmnwQiA"   # 유튜브 비디오 URL
st.text("MP4 파일. format='video/mp4'")
st.video(video_url, format='video/mp4')                     # st.video(video_url) 도 동일
