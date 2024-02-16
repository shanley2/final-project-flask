import json
import requests
import math

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyze } }
    res = requests.post(url, json = obj, headers = headers, timeout = 10)
    formatted_res = json.loads(res.text)

    # initializing  variables to use in loop
    emotions = formatted_res['emotionPredictions'][0]['emotion']
    dominantVal = 0
    dominantName = ''
    ret = {}

    for emotion in emotions:
        ret[emotion] = emotions[emotion]
        if abs(dominantVal) < abs(emotions[emotion]):
            dominantVal = emotions[emotion]
            dominantName = emotion

    ret['dominant_emotion'] = dominantName
    return ret
