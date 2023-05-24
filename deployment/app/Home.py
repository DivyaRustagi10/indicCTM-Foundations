import streamlit as st

st.set_page_config(
	page_title = "Indic Topic Tagger",
	page_icon = "😂 "
	)

st.title("Welcome to Indic Topic Tagger!")
st.sidebar.success("Select a page above")

st.header("Update # 1:", anchor = None)
st.subheader("Currently, our site is still under construction. All outputs return for the model-pulled sample case below:")
st.text("Sample Case: ਗੁਜਰਾਤ ਦੇ 50 ਮਹਿਲਾ ਮੋਟਰਸਾਈਕਲ ਸਵਾਰਾਂ ਦੇ ਗਰੁੱਪ ‘ਬਾਈਕਿੰਗ ਕਵੀਨਜ਼’ ਨੇ ਅੱਜ ਇੱਥੇ ਪ੍ਰਧਾਨ ਮੰਤਰੀ, ਸ਼੍ਰੀ ਨਰੇਂਦਰ ਮੋਦੀ ਨਾਲ ਮੁਲਾਕਾਤ ਕੀਤੀ।ਗਰੁੱਪ ਦਾ ਕਹਿਣਾ ਹੈ ਕਿ ਉਨ੍ਹਾਂ ਨੇ 13 ਰਾਜਾਂ / ਕੇਂਦਰ ਸ਼ਾਸਤ ਪ੍ਰਦੇਸ਼ਾਂ ’ਚ 10,000 ਕਿਲੋਮੀਟਰ ਦਾ ਸਫਰ ਤੈਅ ਕਰਦਿਆਂ ਰਾਹ ਵਿੱਚ ਬੇਟੀ ਬਚਾਓ, ਬੇਟੀ ਪੜ੍ਹਾਓ ਅਤੇ ਸਵੱਛ ਭਾਰਤਵਰਗੇ ਕਈ ਸਮਾਜਿਕ ਮੁੱਦਿਆਂ ’ਤੇ ਲੋਕਾਂ ਨਾਲ ਚਰਚਾ ਕੀਤੀ।ਉਨ੍ਹਾਂ ਨੇ 15 ਅਗਸਤ 2017 ਨੂੰ ਲੱਦਾਖ ਦੇ ਖਰਦੁੰਗਲਾ ਵਿੱਖੇ ਤਿਰੰਗਾ ਲਹਿਰਾਇਆ।ਪ੍ਰਧਾਨ ਮੰਤਰੀ ਨੇ ਉਨ੍ਹਾਂ ਦੇ ਯਤਨਾਂ ਦੀ ਪ੍ਰਸ਼ੰਸਾ ਕੀਤੀ ਅਤੇ ਉਨ੍ਹਾਂ ਦੇ ਚੰਗੇ ਭਵਿੱਖ ਦੀ ਕਾਮਨਾ ਕੀਤੀ।"
)

st.header("Update # 2:", anchor = None)
st.subheader("Currently, only word cloud for English-based models and Top 10 tag functions exist in our 'Advanced Users' section. Future updates are set to include the below additional functions:")

st.markdown("Topic Coherence score (NPMI)")
st.markdown("Topic Similarity")
st.markdown("Topic Matches")
st.markdown("KL Divergence")
st.markdown("Topic Quality Score by User")
st.markdown("Topic Distribution Charts")

st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    padding-left:80px;
}
</style>
''', unsafe_allow_html=True)

# Start of 'About' section #################
st.header("About", anchor=None)
st.subheader("We are a small team of Penn State students with a passion for topic modeling and NLP. Our online topic tagger was built for our DS440 capstone project, and has since evolved to be so much more.")

st.text("\n")

st.subheader("Please refer to the instructions below to guide you through the tagging process and to see how our topic model can be best fitted to your needs.")

st.subheader("\n")

st.subheader("Good luck tagging!")

st.text("\n")
st.text("\n")

st.markdown("![Alt Text](https://media.giphy.com/media/w9mHi4xjefrAwpDJAT/giphy.gif)")
# End of 'About' section #################


# Start of 'Instructions' section #################
st.header("How to Use", anchor=None)

st.subheader("Are you a nonnative speaker or just looking to get a few quick tags?")
st.subheader("Perhaps you're an NLP researcher or student looking to get more advanced stats alongside your topic tags?")

st.text("\n")

st.subheader("If you answered yes to the former, our 'Tags for Nonnative Speakers' page will get you tags without any of that extra fluff.")

st.subheader("\n")

st.subheader("If you happen to be a researcher, student, or are just interested in seeing a more detailed breakdown of your handpicked topic tags, please refer to our 'Tags for Researchers and Multilingual Speakers' page.")

st.text("\n")

st.text("\n")

# End of 'Instructions' section #################
