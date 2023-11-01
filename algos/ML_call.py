import openai

api_key = "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"
api_url = "https://api.openai.com/v1/moderations"

openai.api_key = api_key


def moderation_api(input_text):
    response = openai.Moderation.create(
        input=input_text,
    )
    output = response["results"]
    # use results[0] for the categories and results[1] for the category scores
    return output


if __name__ == "__main__":
    text = "I hate you slut."
    print(moderation_api(text))
