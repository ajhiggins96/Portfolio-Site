import os
import openai
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.core.llms import ChatMessage
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI

# load the file
documents = SimpleDirectoryReader(input_files=["bio.txt"]).load_data()

def ask_bot(input_text, openai_api_key):
    # define key
    os.environ["OPENAI_API_KEY"] = openai_api_key
    openai.api_key = os.environ["OPENAI_API_KEY"]

    # define LLM
    # llm = OpenAI(
    #     model_name="gpt-3.5-turbo",
    #     temperature=0
    # )
    try:
        Settings.embed_model = OpenAIEmbedding()
        # load index
        index = VectorStoreIndex.from_documents(documents)    
        
        # query LlamaIndex and GPT-3.5 for the AI's response
        messages = [
            ChatMessage(
                role='system', content="""You are Buddy, an AI assistant dedicated to assisting Andrew in his job search by providing recruiters with relevant and concise information. 
        If you do not know the answer, politely admit it and let recruiters know how to contact Andrew to get more information directly from {pronoun}. 
        Don't put "Buddy" or a breakline in the front of your answer."""
            ),
            ChatMessage(role='user', content=input_text)
        ]
        
        output = index.as_query_engine().query(messages)
        print(f"output: {output}")
        return output.response
    
    except Exception as e:
        raise(e)