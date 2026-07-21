from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import HumanMessage

#chat template
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'), # all chats of customer and agent will be saved here
    ('human','{query}')
])

chat_history = []
# load chat history
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())
    
print(chat_history)

# create prompt
prompt = chat_template.invoke({'chat_history': chat_history,'query':HumanMessage(content='Where is my refund?')})
print(prompt)