import streamlit as st
import json
import requests

import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

from sample_if10 import top_10

st.title("NLP researcher? Or just language savvy? Either way, add a little more flair to your topic tags.") # i.e., Multilingual/Research-oriented Users

st.subheader("Note # 1:")
st.text("Current functions include Top 10 best tags and word cloud for English-based models. These outputs are set to return for the sample output below:")
st.text("Sample Case: ਗੁਜਰਾਤ ਦੇ 50 ਮਹਿਲਾ ਮੋਟਰਸਾਈਕਲ ਸਵਾਰਾਂ ਦੇ ਗਰੁੱਪ ‘ਬਾਈਕਿੰਗ ਕਵੀਨਜ਼’ ਨੇ ਅੱਜ ਇੱਥੇ ਪ੍ਰਧਾਨ ਮੰਤਰੀ, ਸ਼੍ਰੀ ਨਰੇਂਦਰ ਮੋਦੀ ਨਾਲ ਮੁਲਾਕਾਤ ਕੀਤੀ।ਗਰੁੱਪ ਦਾ ਕਹਿਣਾ ਹੈ ਕਿ ਉਨ੍ਹਾਂ ਨੇ 13 ਰਾਜਾਂ / ਕੇਂਦਰ ਸ਼ਾਸਤ ਪ੍ਰਦੇਸ਼ਾਂ ’ਚ 10,000 ਕਿਲੋਮੀਟਰ ਦਾ ਸਫਰ ਤੈਅ ਕਰਦਿਆਂ ਰਾਹ ਵਿੱਚ ਬੇਟੀ ਬਚਾਓ, ਬੇਟੀ ਪੜ੍ਹਾਓ ਅਤੇ ਸਵੱਛ ਭਾਰਤਵਰਗੇ ਕਈ ਸਮਾਜਿਕ ਮੁੱਦਿਆਂ ’ਤੇ ਲੋਕਾਂ ਨਾਲ ਚਰਚਾ ਕੀਤੀ।ਉਨ੍ਹਾਂ ਨੇ 15 ਅਗਸਤ 2017 ਨੂੰ ਲੱਦਾਖ ਦੇ ਖਰਦੁੰਗਲਾ ਵਿੱਖੇ ਤਿਰੰਗਾ ਲਹਿਰਾਇਆ।ਪ੍ਰਧਾਨ ਮੰਤਰੀ ਨੇ ਉਨ੍ਹਾਂ ਦੇ ਯਤਨਾਂ ਦੀ ਪ੍ਰਸ਼ੰਸਾ ਕੀਤੀ ਅਤੇ ਉਨ੍ਹਾਂ ਦੇ ਚੰਗੇ ਭਵਿੱਖ ਦੀ ਕਾਮਨਾ ਕੀਤੀ।"
)

st.subheader("Note # 2:")

st.text("Currently, only word cloud for English-based models and Top 10 tag functions exist in our 'Advanced Users' section. Future updates are set to include the below additional functions:")

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
    if text == '':
        st.text("Please input text before hitting submit.")

    else:
        st.spinner(text="Please wait ... Retrieving tags ...")

    # Fetch data and feed thru model
        try:

        # do something here with text
            input = {"input_text": text}
#        res = requests.post(url = "https://a13c-34-143-172-49.ngrok.io/predict",
#              data = json.dumps(input))


        # Start of 'Stats for Nerds' section
            st.header("Stats for Nerds", anchor=None)

        # Output Word Cloud visualization below

        # get sample text
            preds = top_10()

        # Output top 10 best tags
            st.text("Top 10 from prediction_hi_model_25:")
            st.text(preds[0])

        # Create and generate a word cloud image:
            hi_25 = preds[0]
            hi_25_str = ','.join(str(item) for item in hi_25)

        #wordcloud = WordCloud().generate(hi_25_str)

        #fig, ax = plt.subplots(figsize = (12, 8))
        #ax.imshow(wordcloud)
        #plt.axis("off")
        #st.pyplot(fig)

        # Output top 10 best tags
            hi_50 = preds[1]
            hi_50_str = ','.join(str(item) for item in hi_50)

            st.text("Top 10 from prediction_hi_model_50:")
            st.text(preds[1])

        #wordcloud = WordCloud().generate(hi_50_str)

        #fig, ax = plt.subplots(figsize = (12, 8))
        #ax.imshow(wordcloud)
        #plt.axis("off")
        #st.pyplot(fig)

        # Output top 10 best tags
            st.text("Top 10 from prediction_en_model_25:")
            st.text(preds[2])

            en_25 = preds[2]
            en_25_str = ','.join(str(item) for item in en_25)

            cloud = WordCloud().generate(en_25_str)

            fig, ax = plt.subplots(figsize = (12, 8))
            ax.imshow(cloud)
            plt.axis("off")
            st.pyplot(fig)

        # Output top 10 best tags
            en_50 = preds[3]
            en_50_str = ','.join(str(item) for item in en_50)

            st.text("Top 10 from prediction_en_model_50:")
            st.text(preds[3])

            cloud = WordCloud().generate(en_50_str)

            fig, ax = plt.subplots(figsize = (12, 8))
            ax.imshow(cloud)
            plt.axis("off")
            st.pyplot(fig)

        # Output request results below
        #st.subheader(input)

        except ValueError:
            st.text("Submit failed")
