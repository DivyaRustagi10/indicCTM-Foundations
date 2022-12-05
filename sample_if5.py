import json

def top_5():
    # Opening JSON file
    f = open('API_sample_response.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list

    key_array = []
    for i in data.keys():
        key_array.append(i)

    t = []
    for _ in key_array:
        t.append(data[_][:5])
    #print(data["prediction_hi_model_25"][:5])
    #print(data["prediction_hi_model_50"])

            # Closing file

    f.close()
    return t
