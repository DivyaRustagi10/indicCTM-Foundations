import json

def top_5():
    # Opening JSON file
    f = open('API_sample_response.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    t = [
    data["prediction_hi_model_25"][:5],
    data["prediction_hi_model_50"][:5],
    data["prediction_en_model_25"][:5],
    data["prediction_en_model_50"][:5]
    ]

    #print(data["prediction_hi_model_25"][:5])
    #print(data["prediction_hi_model_50"])

            # Closing file

    f.close()
    return t
