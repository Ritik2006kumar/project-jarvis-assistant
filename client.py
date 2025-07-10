from openai import OpenAI


client = OpenAI(
    api_key=" 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"
)
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages =[
        {"role" :"stystem" ,"content":"you are a virtual assistant named jarvis skilling in gernal tasks like alexa ,google could"} ,
        {"role":"user" , "content":"what is python"}  
    ]
)
print(completion.choices[0].message.content)









