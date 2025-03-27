import streamlit as st
from PIL.ImageOps import expand

from utils import generator_script

st.title("📹视频脚本生成器")

with st.sidebar:
    openai_aip_key = st.text_input("请输入OpenAI密钥",type="password")
    st.markdown("[获取OpenAi密钥](https://platform.openai.com/account/api-keys)")

subject = st.text_input("💡请输入视频主题")
video_length = st.number_input("请输入视频长度",min_value=0.1,step=0.1)
creativity = st.slider("⭐请输入视频的创造力",min_value=0.0,max_value=1.0,value=0.2,step=0.1)
submit = st.button("生成脚本")


if submit and not openai_aip_key:
    st.info("请输入openai密钥")
    st.stop()

if submit and not subject:
    st.info("请输入视频主题")
    st.stop()

if submit and not video_length >= 0.1:
    st.info("请输大于0.1的视频长度")
    st.stop()

if submit:
    with st.spinner(("ai正在思考，请稍后")):
        search_result, title, script = generator_script(subject,video_length,creativity,openai_aip_key)
    st.success("视频脚本已生成！")
    st.subheader("🔥 标题：")
    st.write(title)
    st.subheader("📜 脚本：")
    st.write(script)
    with st.expander("维基百科搜索结果 👀"):
        st.info(search_result)

