import uvicorn
from pydantic import BaseModel

# Create data class for input for data validation
class Document(BaseModel):
  input_text: str
  class Config:
    schema_extra = {
        "example": {
                "input_text": 
                "ਗੁਜਰਾਤ ਦੇ 50 ਮਹਿਲਾ ਮੋਟਰਸਾਈਕਲ ਸਵਾਰਾਂ ਦੇ ਗਰੁੱਪ ‘ਬਾਈਕਿੰਗ ਕਵੀਨਜ਼’ ਨੇ ਅੱਜ ਇੱਥੇ ਪ੍ਰਧਾਨ ਮੰਤਰੀ, ਸ਼੍ਰੀ ਨਰੇਂਦਰ ਮੋਦੀ ਨਾਲ ਮੁਲਾਕਾਤ ਕੀਤੀ।"\
                "ਗਰੁੱਪ ਦਾ ਕਹਿਣਾ ਹੈ ਕਿ ਉਨ੍ਹਾਂ ਨੇ 13 ਰਾਜਾਂ / ਕੇਂਦਰ ਸ਼ਾਸਤ ਪ੍ਰਦੇਸ਼ਾਂ ’ਚ 10,000 ਕਿਲੋਮੀਟਰ ਦਾ ਸਫਰ ਤੈਅ ਕਰਦਿਆਂ ਰਾਹ ਵਿੱਚ ਬੇਟੀ ਬਚਾਓ, ਬੇਟੀ ਪੜ੍ਹਾਓ ਅਤੇ ਸਵੱਛ ਭਾਰਤ"\
                "ਵਰਗੇ ਕਈ ਸਮਾਜਿਕ ਮੁੱਦਿਆਂ ’ਤੇ ਲੋਕਾਂ ਨਾਲ ਚਰਚਾ ਕੀਤੀ।"\
                "ਉਨ੍ਹਾਂ ਨੇ 15 ਅਗਸਤ 2017 ਨੂੰ ਲੱਦਾਖ ਦੇ ਖਰਦੁੰਗਲਾ ਵਿੱਖੇ ਤਿਰੰਗਾ ਲਹਿਰਾਇਆ।"\
                "ਪ੍ਰਧਾਨ ਮੰਤਰੀ ਨੇ ਉਨ੍ਹਾਂ ਦੇ ਯਤਨਾਂ ਦੀ ਪ੍ਰਸ਼ੰਸਾ ਕੀਤੀ ਅਤੇ ਉਨ੍ਹਾਂ ਦੇ ਚੰਗੇ ਭਵਿੱਖ ਦੀ ਕਾਮਨਾ ਕੀਤੀ।"
            }
        }

from starlette.responses import PlainTextResponse
# Create endpoint for serving requests using endpoint function
from fastapi import FastAPI, Response
from fastapi.responses import UJSONResponse
import joblib

app = FastAPI()


@app.on_event("startup")
def load_model():
  global hindi_model_25
  global hindi_model_50
  global tp
  # Load Indic Multilingual embeddings
  tp = TopicModelDataPreparation('ai4bharat/indic-bert')
  tp.max_seq_length = 200

  file = open("/content/models/z_ctm_25_HI.pkl", "rb")
  hindi_model_25 = joblib.load(file)
  hindi_model_50 = joblib.load(open("/content/models/z_ctm_50_HI.pkl", "rb"))
  file.close()

@app.get('/')
def index():
  return {'message': 'This is the homepage of the API '}

@app.post('/predict')
def get_topic_predictions(data: Document):
  received = data.dict()
  text = list(received['input_text'])
  input_text = tp.transform(text)

  document_index = 1
  models = {'model_25': hindi_model_25, 'model_50': hindi_model_50}
  output = {}
  for name, model in models.items():
    pred_name = model.get_thetas(input_text, n_samples = 10)
    topic_number = np.argmax(pred_name[1]) # get the topic id of the first document
    predicted_topics = model.get_topic_lists()[topic_number] 
    output['prediction_' + name] = predicted_topics

  return output


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)