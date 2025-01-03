import json
import requests

def emotion_detector(text_to_analyze: str):
    # Get information from the server
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    params = {"raw_document": {"text": text_to_analyze }}
    response = requests.post(url, json=params, headers=headers)
    
    # Format the response
    formatted_response = json.loads(response.text)
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    # Find the dominant emotion
    best_score = 0
    dominant_emotion = ""
    for key, value in emotions.items():
        if value > best_score:
            best_score = value
            dominant_emotion = key
    emotions["dominant_emotion"] = dominant_emotion
    
    return emotions


if __name__ == "__main__":
    print(emotion_detector("I love this new technology"))