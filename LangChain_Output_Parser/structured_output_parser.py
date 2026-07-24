import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser,ResponseSchema #overall library
# important reusable component in langchain_core


load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant") 

schema = [
    ResponseSchema(name='fact_1',description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2',description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3',description='Fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = 'Give me trhree fact about the {topic}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

#prompt = template.invoke({'topic' : 'Black Hole'}) now using chain

result = chain.invoke({'topic' : 'Black Hole'})

#final_result = parser.parse(result.content) now using chain

print(result)