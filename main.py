
import http.client
import json
import base64
import requests
def image_to_data_uri(file_path):
    with open(file_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
        return f"data:image/jpeg;base64,{encoded_image}"


def get_image_title(local_image_path):
    YOUR_GENERATED_SECRET = "0sRJjvasLSXPt6JkpiY1:97929f1a998c05797fb763c145b2281441d9242e25dbd0198593347ec64ee696"
    data = {
        "data": [
            {"image": image_to_data_uri(local_image_path), "features": []}
        ]
    }
    scenex_api_url: str = "https://api.scenex.jina.ai/v1/describe"
    headers = {
        "x-api-key": f"token {YOUR_GENERATED_SECRET}",
        "content-type": "application/json",
    }

    response = requests.post(scenex_api_url, headers=headers, json=data)
    response.raise_for_status()
    result = response.json().get("result", [])
    img = result[0] if result else {}

    return img.get("text", "")
