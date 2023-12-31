from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ['API_KEY']
api_url = "https://api.openai.com/v1/moderations"

client = OpenAI(api_key=api_key)


def moderation_api(input_text):
    response = client.moderations.create(input=input_text)
    output = response.results
    # use results[0] for the categories and results[1] for the category scores
    return output


def ml_moderation(input):
    # decide which format our input will be
    response = moderation_api(input)[0]
    flag = response.flagged
    if not flag:
        return False
    flagged_vals = []
    for cat in response.categories:
        term = cat[0]
        if cat[1]:
            flagged_vals.append(term)
    return True, flagged_vals

    # SAMPLE RESPONSE [<OpenAIObject at 0x7ff49fd1a220> JSON: {


#   "flagged": true,
#   "categories": {
#     "sexual": false,
#     "hate": false,
#     "harassment": true,
#     "self-harm": false,
#     "sexual/minors": false,
#     "hate/threatening": false,
#     "violence/graphic": false,
#     "self-harm/intent": false,
#     "self-harm/instructions": false,
#     "harassment/threatening": false,
#     "violence": false
#   },
#   "category_scores": {
#     "sexual": 0.0005609678919427097,
#     "hate": 0.0829748660326004,
#     "harassment": 0.9900439977645874,
#     "self-harm": 1.256310966368801e-08,
#     "sexual/minors": 4.765902872350125e-07,
#     "hate/threatening": 5.0074504542863e-09,
#     "violence/graphic": 1.4420107330437304e-09,
#     "self-harm/intent": 8.518085126141273e-10,
#     "self-harm/instructions": 2.130169374225943e-10,
#     "harassment/threatening": 5.573383077717153e-06,
#     "violence": 3.4348780900472775e-05
#   }
# }]
# None
#
if __name__ == "__main__":
    text = "what is that white person doing over there."
    print(ml_moderation(text))












