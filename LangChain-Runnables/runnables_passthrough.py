from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough

load_dotenv()

prompt = PromptTemplate(
    template = 'Write a joke about a {topic}',
    input_variables=['topic']
)

model = ChatGroq(model = 'llama-3.1-8b-instant')

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template = 'Explain the following joke {text}',
    input_variables=['text']
)

joke_gen_chain = RunnableSequence(prompt,model,parser)

parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'explain' : RunnableSequence(prompt2,model,parser)
})

final_chain = RunnableSequence(joke_gen_chain,parallel_chain)

result = final_chain.invoke({'topic':'AI'})\
    
print(result )