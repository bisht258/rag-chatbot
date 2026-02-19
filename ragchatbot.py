import pdfplumber
import os
import streamlit as st
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") #KEEP IT SECURE
st.header("My First RagChatbot")

with st.sidebar:
    st.title("Your Documents")
    file=st.file_uploader("Upload your PDF document here",type="pdf")

#extract the content from PDF

if file is not None:
    with pdfplumber.open(file) as pdf:
        text = ""

        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:   # prevents None error
                text += page_text + "\n"

                # st.write(text)

    # split into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ". ", ","],
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_text(text)
    #st.write(chunks)


#generate embeddings
    embeddings=OpenAIEmbeddings(model="text-embedding-3-small", openai_api_key = OPENAI_API_KEY)

#store embeddings in vector db
    vector_store=FAISS.from_texts(chunks,embeddings)

    #get user question
    user_question=st.text_input("Type your question here")

    #generate answer
    #question->embeddings->similarity search->results to LLM->response(CHAIN)

    def format_docs(docs):
        return "\n\n".join([doc.page_content for doc in docs])

    #retrieving
    retriever=vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={"k":4} #no. of closest searches to retrieve
    )

    #define LLM and prompts

    llm=ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.3, #more randomness, at lesser values it gets more deterministic, while at bigger values it becomes more creative and random
        max_tokens=1000,
        openai_api_key=OPENAI_API_KEY #authentication
    )

    #provide prompts, set of instructions to llm
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a helpful assistant answering questions about a PDF document.\n\n"
            "Guidelines:\n"
            "1. Provide complete, well-explained answers using the context below.\n"
            "2. Include relevant details, numbers, and explanations.\n"
            "3. If related information appears, include it for better understanding.\n"
            "4. Only use information from the provided context — do not use outside knowledge.\n"
            "5. Summarize long information in bullets when helpful.\n"
            "6. If the answer is not in the context, say so politely.\n\n"
            "Context:\n{context}"
        ),
        ("human", "{question}")
    ])

    chain=(
          {"context": retriever | format_docs, "question": RunnablePassthrough() }
          | prompt
          | llm
          | StrOutputParser()

    )

    if user_question:
         response=chain.invoke(user_question)
         st.write(response)

