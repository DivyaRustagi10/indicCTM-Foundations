import streamlit as st
import json
import requests

st.title("NLP researcher? Or just language savvy? Either way, add a little more flair to your topic tags.") # i.e., Multilingual/Research-oriented Users

# Start of 'Instructions' section #################
st.header("Instructions", anchor=None)

st.text("Copy and paste your text in the space below.")
st.text("Feel free to use as many or as few characters as you'd like.")
# End of 'Instructions' section #################

# input user text
text = st.text_area(
"Happy tagging!\n", value="",
height=None,
max_chars=None,
key=None,
help=None,
on_change=None,
args=None,
kwargs=None,
placeholder=None,
disabled=False,
label_visibility="visible")

if st.button('Submit'):
    st.spinner(text="Please wait ... Retrieving tags ...")

    # Fetch data and feed thru model
    try:
        # do something here with text
        input = text
#        res = requests.post(url = "https://a13c-34-143-172-49.ngrok.io/predict",
#              data = json.dumps(input))

        # Output Word Cloud visualization below

        # Start of 'Stats for Nerds' section
        st.header("Stats for Nerds", anchor=None)

        # Output request results below
        st.subheader(input)

    except ValueError:
        st.text("Submit failed")
