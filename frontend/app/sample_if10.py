import json

def top_10():
    # Opening JSON file
    f = open('API_sample_response.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Opening JSON file
    f = open('API_sample_response.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    t = [
    data["prediction_hi_model_25"][:10],
    data["prediction_hi_model_50"][:10],
    data["prediction_en_model_25"][:10],
    data["prediction_en_model_50"][:10]
    ]


            # Closing file

    f.close()
    return t
