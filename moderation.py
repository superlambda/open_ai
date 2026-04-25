from openai import OpenAI

client = OpenAI()

threaten = "你不听我的我就拿刀砍死你"
def moderation(text):
    response = client.moderations.create(input=text)
    output = response["results"][0]
    return output
print(moderation(threaten))
