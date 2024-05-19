import streamlit as st
import requests
import json 
import re

# Fetching data from the API
response = requests.get('https://devapi.beyondchats.com/api/get_message_with_sources')
data = json.loads(response.text)

# Extracting main data section
messages = data['data']['data']
responses = [messages[i]['response'] for i in range(len(messages))]

# Streamlit's selectbox for user to choose a response
selected_response = st.selectbox('Navigate through the responses',
   (responses),
   index=0, 
   placeholder="Select Your Response")

# Selecting the index of the selected response
response_index = responses.index(selected_response)

citations = [] # Preparing citations for the selected response

for i in range(len(messages[response_index]['source'])):
    source_id = messages[response_index]['source'][i]['id']
    source_link = messages[response_index]['source'][i]['link']
    source_context = messages[response_index]['source'][i]['context']
    
    if not source_link:
        # Finding link in context if link is empty
        found_links = re.findall(r'https?://\S+', source_context)
        if found_links: 
            # If you want multiple links for same Id you can set found_links[0] to link
            citations.append({"id": source_id, "link": found_links[0]}) 
    else:
        citations.append({"id": source_id, "link": source_link})

# Displaying the final citations
st.write('Citations:', citations)
