import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter 
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.llms import HuggingFaceHub
from langchain.llms import Ollama

# from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline

# import transformers
# import torch


load_dotenv()

    

def get_pdf_text(pdf_docs):
    text=""
    #extract text from given pdfs
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(raw_text):
   text_splitter = CharacterTextSplitter(
       #initialize text splitter
       separator='\n',
       chunk_size=1000,
       chunk_overlap=200,
       length_function=len
   )
   chunks= text_splitter.split_text(raw_text)    
   return chunks
    
def get_vector_store(text_chunks):
    # embeddings= OpenAIEmbeddings()
    embeddings= HuggingFaceEmbeddings(model_name='hkunlp/instructor-large')
    vector_store= FAISS.from_texts(
        texts=text_chunks,
        embedding=embeddings
    )
    return vector_store
 
def get_conversation_chain(vector_store):
    
    # llm=Ollama(model="llama3")
    llm=ChatOpenAI()
    # model_id = "meta-llama/Meta-Llama-3-8B"
    # hf = HuggingFacePipeline.from_model_id(
    #     model_id=model_id,
    #     task="text-generation",
    #     pipeline_kwargs={"max_new_tokens": 10},
    # )
    
    memory= ConversationBufferMemory(
        memory_key='chat_history',
        return_messages=True
    )
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=memory
    )
    return conversation_chain

def handle_user_input(user_question):
    response = st.session_state.conversation({'question':user_question})
    st.session_state.chat_history =response['chat_history']
    
    for i, message in enumerate(response['chat_history']):
        if i%2 ==0 :
            with st.chat_message("user"):
                st.write(message.content)
        else:
            with st.chat_message("ai"):
                st.write(message.content)
    
         
def main():
    st.set_page_config(page_title='PDF Chat', page_icon=':books:', layout='centered', initial_sidebar_state='auto')
    
    if "conversation" not in st.session_state:
        st.session_state.conversation= None
        
    if "chat_history" not in st.session_state:
        st.session_state.chat_history= None
    
    st.header('Chat with multiple PDFs :books:')
    
    user_question = st.chat_input("Ask something about your documents...")
    if user_question:
        handle_user_input(user_question)
    
    with st.sidebar:
        st.subheader('PDFs')
        st.write('Upload your PDFs here:')
        pdf_docs = st.file_uploader("Choose PDF files", type=['pdf'], accept_multiple_files=True)
        if st.button('Process PDFs'):
            with st.spinner('Processing PDFs...'): 
                # get the pdf text
                raw_text= get_pdf_text(pdf_docs)
                     
                # get the text chunks
                text_chunks= get_text_chunks(raw_text)
                # st.write(text_chunks)
                
                #create vector store
                vector_store= get_vector_store(text_chunks)
                
                # create conversation chain
                st.session_state.conversation= get_conversation_chain(vector_store)
    

if __name__ == '__main__':
    main()