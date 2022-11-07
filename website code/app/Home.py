import streamlit as st

st.set_page_config(
	page_title = "Indic Topic Tagger",
	page_icon = "😂 "
	)

st.title("Welcome to Indic Topic Tagger!")
st.sidebar.success("Select a page above")

# Start of 'About' section #################
st.header("About", anchor=None)

# text here
st.text("Fill in 'About' section here!!!")

# instructions for use here
st.subheader("How to Use", anchor=None)
st.text("Fill in 'Instructions' here!!!")
# End of 'About' section #################
