import streamlit as st

st.set_page_config(page_title="Manual", page_icon="📘")

st.title("📘 Manual")
st.write("Περιεχόμενο manual εδώ...")

if st.button("🔙 Επιστροφή στην αρχική", use_container_width=True):
    st.switch_page("app.py")
