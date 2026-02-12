from config import client, MODEL_NAME
from prompts import DDR_PROMPT

def generate_ddr(observations):

    obs_text = "\n".join(
        [f"{o['area']} - {o['issue']} ({o['source']})"
         for o in observations]
    )

    response = client.responses.create(
        model=MODEL_NAME,
        input=f"{DDR_PROMPT}\n\nOBSERVATIONS:\n{obs_text}"
    )

    return response.output[0].content[0].text
