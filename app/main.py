"""# FastAPI Setup

    **What is FastApi?**

    FastAPI offers automatic docs generation functionality, authentication, data validation via pydantic models.

    **Colab Code**

    It is a Python package that allows you to start a code server right from your Colab notebooks without setting up anything locally on your system. 
    It can be used to start a VS Code environment, Jupyter Lab server, or tunnel the FastAPI server to the web, all in the colab notebook. 

    This can be a great plus point for the enthusiast coders who train their models on the cloud and now want to share their findings with the world in the form of APIs. 
"""
# Imports
import os
from contextualized_topic_models.utils.data_preparation import TopicModelDataPreparation
import numpy as np
import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI
import joblib

# Create data class for input for data validation
class Document(BaseModel):
    '''
    Class for data 
    '''
    input_text: str

    class Config:
        schema_extra = {
            "example": {
                "input_text":
                    "ਗੁਜਰਾਤ ਦੇ 50 ਮਹਿਲਾ ਮੋਟਰਸਾਈਕਲ ਸਵਾਰਾਂ ਦੇ ਗਰੁੱਪ ‘ਬਾਈਕਿੰਗ ਕਵੀਨਜ਼’ ਨੇ ਅੱਜ ਇੱਥੇ ਪ੍ਰਧਾਨ ਮੰਤਰੀ, ਸ਼੍ਰੀ ਨਰੇਂਦਰ ਮੋਦੀ ਨਾਲ ਮੁਲਾਕਾਤ ਕੀਤੀ।"
                    "ਗਰੁੱਪ ਦਾ ਕਹਿਣਾ ਹੈ ਕਿ ਉਨ੍ਹਾਂ ਨੇ 13 ਰਾਜਾਂ / ਕੇਂਦਰ ਸ਼ਾਸਤ ਪ੍ਰਦੇਸ਼ਾਂ ’ਚ 10,000 ਕਿਲੋਮੀਟਰ ਦਾ ਸਫਰ ਤੈਅ ਕਰਦਿਆਂ ਰਾਹ ਵਿੱਚ ਬੇਟੀ ਬਚਾਓ, ਬੇਟੀ ਪੜ੍ਹਾਓ ਅਤੇ ਸਵੱਛ ਭਾਰਤ"
                    "ਵਰਗੇ ਕਈ ਸਮਾਜਿਕ ਮੁੱਦਿਆਂ ’ਤੇ ਲੋਕਾਂ ਨਾਲ ਚਰਚਾ ਕੀਤੀ।"
                    "ਉਨ੍ਹਾਂ ਨੇ 15 ਅਗਸਤ 2017 ਨੂੰ ਲੱਦਾਖ ਦੇ ਖਰਦੁੰਗਲਾ ਵਿੱਖੇ ਤਿਰੰਗਾ ਲਹਿਰਾਇਆ।"
                    "ਪ੍ਰਧਾਨ ਮੰਤਰੀ ਨੇ ਉਨ੍ਹਾਂ ਦੇ ਯਤਨਾਂ ਦੀ ਪ੍ਰਸ਼ੰਸਾ ਕੀਤੀ ਅਤੇ ਉਨ੍ਹਾਂ ਦੇ ਚੰਗੇ ਭਵਿੱਖ ਦੀ ਕਾਮਨਾ ਕੀਤੀ।"
            }
        }


# Create endpoint for serving requests using endpoint function
app = FastAPI()

@app.on_event("startup")
def load_model():
    global HINDI_MODEL_25
    global HINDI_MODEL_50
    global ENG_MODEL_25
    global ENG_MODEL_50
    global TP
    # Load Indic Multilingual embeddings
    TP = TopicModelDataPreparation('ai4bharat/indic-bert')
    TP.max_seq_length = 200

    file = open("models\z_ctm_25_HI.pkl", "rb")
    HINDI_MODEL_25 = joblib.load(file)
    HINDI_MODEL_50 = joblib.load(open("models\z_ctm_50_HI.pkl", "rb"))
    ENG_MODEL_25 = joblib.load(open("models\z_ctm_25_EN.pkl", "rb"))
    ENG_MODEL_50 = joblib.load(open("models\z_ctm_50_EN.pkl", "rb"))

    file.close()


@app.get('/')
def index():
    return {'message': 'This is the homepage of the API '}

@app.post('/predict')
def get_topic_predictions(data: Document):
    received = data.dict()
    text = list(received['input_text'])
    input_text = TP.transform(text)

    models = {'hi_model_25': HINDI_MODEL_25, 'hi_model_50': HINDI_MODEL_50,
              'en_model_25': ENG_MODEL_25, 'en_model_50': ENG_MODEL_50}
    output = {}
    for name, model in models.items():
        pred_name = model.get_thetas(input_text, n_samples=10)
        # get the topic id of the first document
        topic_number = np.argmax(pred_name[1])
        predicted_topics = model.get_topic_lists()[topic_number]
        output['prediction_' + name] = predicted_topics

    return output

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)