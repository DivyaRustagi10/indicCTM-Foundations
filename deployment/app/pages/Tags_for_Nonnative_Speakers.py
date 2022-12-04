import streamlit as st

st.title("Looking for topic tags and nothing more? You've come to the right place.") # i.e., Nonnative Users
#st.write("You have entered", st.session_state["my_input"])

# Start of 'Instructions' section #################
st.header("Instructions", anchor=None)

st.text("Fill in 'Instructions' section here!!!")
# End of 'Instructions' section #################

# input user text
st.text_area(
"Paste your text below:", value="",
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
        st.text("Top 5 works fine")

    except ValueError:
        st.text("Top 5 failed")
    # Output top 5 best tags below

# Top 10 button
if st.button('Get Top 10 Best Tags'):
    st.spinner(text="Please wait ... Retrieving Top 10 best tags ...")

    # Fetch top 10 best tags
    try:
        st.text("Top 10 works fine")

    except ValueError:
        st.text("Top 10 failed")


    # Output top 10 best tags below
