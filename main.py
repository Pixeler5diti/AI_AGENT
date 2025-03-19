from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()

llm= ChatOpenAI(model="gpt-4o-mini")
response =llm.invoke("what is the meaning of life?")
print(response)