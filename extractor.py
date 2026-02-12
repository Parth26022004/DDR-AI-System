import json
from config import client, MODEL_NAME
from prompts import EXTRACTION_PROMPT

def extract_observations(text, source_name):

    response = client.responses.create(
        model=MODEL_NAME,
        input=f"{EXTRACTION_PROMPT}\n\nSOURCE:{source_name}\n\n{text}"
    )

    try:
        data = json.loads(response.output[0].content[0].text)
    except:
        data = []

    return data
