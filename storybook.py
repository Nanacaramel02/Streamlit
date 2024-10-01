from openai import OpenAI
import streamlit as st
import os
import time

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

#Story
prompt = """Friendship between Hannah and Fazura"""

def story_gen(prompt):
    system_prompt = """"
    You are a story world renowed 50 years experience children storyteller. 
    You will given a concept to generate a story suitable for ages 5-7 years old 
    """

    response = client.chat.completions.create(
        model = 'gpt-4o-mini',
        messages = [
            {"role":"system", "content":system_prompt},
             {"role":"user", "content":prompt}
            ],
        temperature = 1,
        max_tokens = 2000

    )
    return response.choices[0].message.content

#cover art
def cover_gen(prompt):
    system_prompt = """"
    You will be given a children story book.
    Generate a prompt for cove art that is suitable and shows themes.
    The prompt will be sent to dell-e-2
    """
    response = client.chat.completions.create(
        model = 'gpt-4o-mini',
        messages = [
            {"role":"system", "content":system_prompt},
             {"role":"user", "content":prompt}
            ],
        temperature = 1,
        max_tokens = 200
    )
    return response.choices[0].message.content  

#image
def image_gen (prompt):
    # Use openai.images.generate instead of openai.Image.create
    response = client.images.generate( 
        model = 'dall-e-2',
        prompt = prompt,
        size = '1024x1024'
    )
    return response.data[0].url # Access the image URL from the response


st.title("Storybook Generator for Kids")
st.divider()

prompt = st.text_input("Enter your story concept:")

if st.button("Generate Storybook"):
  

  with st.spinner('Wait for it...'):
      time.sleep(5)
      story = story_gen(prompt)
      cover = cover_gen(prompt)
      image = image_gen(cover)

      st.snow()
      st.image(image)
      st.write(story)
  st.success("Done!")
  
  

