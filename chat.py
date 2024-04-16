from openai import OpenAI
import csv
import pandas as pd
import openpyxl
client = OpenAI(api_key="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")

conversation_data=[]
 
def chatbot(question):
 response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "user", "content": question},
        {"role": "assistant", "content": ""}
        ],
        temperature=1,
        max_tokens=50,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
 )
 
 data =[]
 temp_array=[question,response.choices[0].message.content]
 data.append(temp_array)
 file_path = "conversation.csv"
 with open(file_path, mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
 
 output= response.choices[0].message.content
 print(output)
 return output
 
  
 


 # Convert the array to a pandas DataFrame
chatbot("hi")
 
 
 

 