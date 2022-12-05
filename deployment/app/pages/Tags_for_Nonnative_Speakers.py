import streamlit as st
import json
import requests
from sample_if5 import top_5
from sample_if10 import top_10

st.title("Looking for topic tags and nothing more? You've come to the right place.") # i.e., Nonnative Users
#st.write("You have entered", st.session_state["my_input"])

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

# Top 5 button
if st.button('Get Top 5 Best Tags'):
    st.spinner(text="Please wait ... Retrieving Top 5 best tags ...")

    # Fetch top 5 best tags
    try:

        # do something here with text
        input = {"input_text": text}

        preds = top_5()
        #res = requests.post(url = "https://a13c-34-143-172-49.ngrok.io/predict",
    #          data = json.dumps(input))

        # Output top 5 best tags below
        st.text("Top 5 from prediction_hi_model_25:")
        st.text(preds[0])

        st.text("Top 5 from prediction_hi_model_50:")
        st.text(preds[1])

        st.text("Top 5 from prediction_en_model_25:")
        st.text(preds[2])

        st.text("Top 5 from prediction_en_model_50:")
        st.text(preds[3])

        #st.subheader(preds)

    except ValueError:
        st.text("Top 5 failed")


# Top 10 button
if st.button('Get Top 10 Best Tags'):
    st.spinner(text="Please wait ... Retrieving Top 10 best tags ...")

    # Fetch top 10 best tags
    try:
        # do something here with text
        input = { "input_text": text}
#        res = requests.post(url = "https://a13c-34-143-172-49.ngrok.io/predict",
#              data = json.dumps(input))

        preds = top_10()
        # Output top 10 best tags below

        # Output top 10 best tags below
        st.text("Top 10 from prediction_hi_model_25:")
        st.text(preds[0])

        st.text("Top 10 from prediction_hi_model_50:")
        st.text(preds[1])

        st.text("Top 10 from prediction_en_model_25:")
        st.text(preds[2])

        st.text("Top 10 from prediction_en_model_50:")
        st.text(preds[3])

    except ValueError:
        st.text("Top 10 failed")
