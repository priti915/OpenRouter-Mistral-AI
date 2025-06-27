from openai import OpenAI
from dotenv import load_dotenv
import os 

# initialize the env files
load_dotenv()

# access the api key
key = os.getenv("API_KEY")


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=key,
)

#user_input = input("Please provide a question? ")
#user_str=input("Enter your physics query? ")

#answer = f"""
    # Consider yourself as a physics teacher.
    # You will answer the questions and taught k-4 students.
    # Question is given below:
    # {user_str}
    # Just briefly explain it and answer should be in 4-5 lines.
#"""

#user_input=("How would you prompt GPT to  return an answer in JSON format")
user_input=input("What are the difference between temperature and top_p in prompt control")

# answer = f"""
# consider as a teacher
# you will answer in the 7 - 8 lines
# given answer in a brief and easily language to understand
# {user_input}
# """




completion = client.chat.completions.create(
  extra_headers={
    # "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    # "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  extra_body={},
  model="mistralai/mistral-small-3.2-24b-instruct:free",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": f"{answer}"
        },
        # {
        #   "type": "image_url",
        #   "image_url": {
        #     "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
        #   }
        # }
      ]
    }
  ]
)
# print(completion)
# print("*"*30)
# print(completion.choices)
# print("*"*30)
# print(completion.choices[0].message.content)
# print("*"*30)
# print(completion.choices[0].message)
# print("*"*30)
print(completion.choices[0].message.content)