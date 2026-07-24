import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant") 
parser = JsonOutputParser()

template = PromptTemplate(
    template = 'Give me the name,age and city of a fictional person \n {format_instruction}',
    input_variables = [],
    partial_variables={'format_instruction':parser.get_format_instructions()}
    # ham format instructions ko partial variable isliye bol rahe kyuki ye runtime pe fill ni hota,runtime ke pehle hi fill ho jata hai 
)

'''prompt = template.format()

print(prompt)

result = model.invoke(prompt)

final_result = parser.parse(result.content)'''

chain = template | model | parser
result = chain.invoke({}) 
# chain.invoke() ke time aapko kuch input dena hoga if input variable hai toh theek else {} empty dictionary hi put kar dena hai
print(result)
print(type(result))