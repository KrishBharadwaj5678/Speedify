import streamlit as st
import subprocess

st.set_page_config(
    page_title="Speedify",
    page_icon="icon.png",
    menu_items={
        "About":"Speedify offers a quick and accurate way to measure your internet speed. Test your download, upload, and ping speeds with ease!"
    }
)

st.write("<h2 style='color:#6CB3FF;'>Test Your Internet Speed Instantly</h2>",unsafe_allow_html=True)

result=subprocess.run(["speedtest-cli","--share"],capture_output=True,text=True)
output=result.stdout
link=output.split("results:")[1].strip()
btn=st.button("Test Speed")
if btn:
    st.image(link)
