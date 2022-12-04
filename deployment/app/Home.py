import streamlit as st

st.set_page_config(
	page_title = "Indic Topic Tagger",
	page_icon = "😂 "
	)

st.title("Welcome to Indic Topic Tagger!")
st.sidebar.success("Select a page above")

# Start of 'About' section #################
st.header("About", anchor=None)
st.text("We are a small team of Penn State students with a passion for topic modeling\nand NLP. Our online topic tagger was built")
st.text("for our DS440 capstone project, and has since evolved to be so much more.")

st.text("\n")

st.text("Please refer to the instructions below to guide you through the tagging process")
st.text("and to see how our topic model can be best fitted to your needs.")

st.text("\n")

st.text("Good luck tagging!")

st.text("\n")
st.text("\n")

st.markdown("![Alt Text](https://media.giphy.com/media/w9mHi4xjefrAwpDJAT/giphy.gif)")
# End of 'Instructions' section #################


# Start of 'Instructions' section #################
st.subheader("How to Use", anchor=None)

st.text("Are you a nonnative speaker or just looking to get a few quick tags?")
st.text("Perhaps you're an NLP researcher or student looking to get more advanced\n")
st.text("stats alongside your topic tags?")

st.text("\n")

st.text("If you answered yes to the former, our 'Tags for Nonnative Speakers' page\n")
st.text("will get you tags without any of that extra fluff.")

st.text("\n")

st.text("If you happen to be a researcher, student, or are just interested in\n")
st.text("seeing a more detailed breakdown of your handpicked topic tags, please\n")
st.text("refer to our 'Tags for Researchers and Multilingual Speakers'")

st.text("Multilingual Users and Researchers")

st.text("\n")

st.text("\n")

# End of 'Instructions' section #################
