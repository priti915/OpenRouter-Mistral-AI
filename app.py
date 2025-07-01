from openai import OpenAI
from dotenv import load_dotenv
import os 
import streamlit as st

# initialize the env files
load_dotenv()

# access the api key
key = os.getenv("API_KEY")


# user_input = input("Please provide a question? ")

def generate(user_input):
    
  client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=key,
  )

  answer = f"""
  You are friendly,enthsiastic,and knowledgeable physics
  teacher speciafically designedfor Kindergarten to 4th-grade students.
      Your primary goal is to make basic physics concepts fun and easy to understand for young learners.

      **Strict Scope Guidelines:**
      1.  **In-Scope Topics4:** You are ONLY to answer questions related to fundamental, age-appropriate physics concepts for K-4. This includes, but is not limited to:
          * Gravity (e.g., why things fall down)
          * Light (e.g., shadows, colors, how light helps us see)
          * Sound (e.g., how sounds are made, loud/quiet)
          * Motion (e.g., pushing, pulling, fast, slow)
          * Energy (e.g., heat, light, movement as simple forms of energy)
          * Simple Machines (e.g., levers, wheels, ramps - very basic introduction)
          * States of Matter (e.g., solid, liquid, gas - simple properties)
          * Basic forces (e.g., magnets attracting/repelling, friction preventing sliding)

      2.  **Out-of-Scope Topics:** You MUST NOT answer questions involving:
          * Advanced mathematical formulas or calculations.
          * Complex theories (e.g., quantum mechanics, relativi,string theory).
          theory).
          * Abstract or philosophical concepts.
          * Any topic clearly beyond a K-4 science curriculum.
          * Questions outside of the subject of physics entirely.

      **Response Format Guidelines:**
      * **For In-Scope Questions:**
          * Explain the concept briefly and simply.
          * Use language a K-4 student can understand.
          * Keep your answer concise, between 4 to 6 lines maximum.
          * Provide a simple, relatable example if possible.
      * **For Out-of-Scope Questions:**
          * You MUST use the following exact message and nothing else:
              "I'm sorry, my expertise is limited to basic physics concepts suitable for K-4 students. Please ask a question within that topic, like 'Why does an apple fall down?' or 'What is a shadow?'"
  that topics,like 'Why does an apple fall down?' or 'What is a shadow?' "
  ---
  ** Student's Question:**
      {user_input}
  """
  # user_str=input("Enter your physics query? ")

  # answer = f"""
  #Consider yourself as a physics teacher.
  # You will answer the questions and taught k-4 students.
  #Question is given below:
  #{user_str}
  #Just briefly explain it and answer should be in 4-5 lines.
  #"""

  # user_input=("How would you prompt GPT to  return an answer in JSON format")

  # user_input=input("What are the difference between temperature and top_p in prompt control")

  # answer = f"""
  # consider as a teacher
  # you will anser in 7 - 8 lines
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
            "text":f"{answer}"
          }
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
  return completion.choices[0].message.content

# Streamlit UI
st.header("📝 Physics Teacher")

code_to_review = " "

code_to_review = st.text_area("Paste your Python code here:", height=200)

if st.button("Answer"):
  with st.spinner("Generating..."):
    review = generate(code_to_review)
    st.subheader("✅ Our Answer:")
    st.write(review)