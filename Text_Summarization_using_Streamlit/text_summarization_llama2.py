import locale
locale.getpreferredencoding = lambda: "UTF-8"


import os
import torch
import math, nltk
import transformers
import PyPDF2
# from transformers import AutoTokenizer
# from langchain_community.llms import HuggingFacePipeline
# from langchain.chains import ConversationChain
# from langchain import LLMChain, HuggingFacePipeline, PromptTemplate
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import streamlit as st
import numpy as np

import warnings
warnings.filterwarnings('ignore')


st.set_page_config(layout = 'wide')

input_file = st.file_uploader("Upload your RSA Document here.", type = ['pdf'])
if input_file is not None:

  with open('document.pdf', 'wb') as f:
    f.write(input_file.getbuffer())

  col1, col2 = st.columns([1, 1])
  
  #PDF to Text Conversion
  text_document = ''
  
        # Open the PDF file
  with open('document.pdf', 'rb') as file:
      # Create a PDF reader object
      reader = PyPDF2.PdfReader(file)

      # Extract text from each page
      text = ''
      for page in reader.pages:
          text += page.extract_text()

      text_document = text
  
  with col1:
    st.info('File uploaded successfully!')
    st.markdown('*** Extracted text is below: ***')
    st.info(text_document)

  with col2:
    #Llama-2 Model Initialization using Hugging Face and Langchain
    # model="meta-llama/Llama-2-7b-chat-hf"
    # tokenizer=AutoTokenizer.from_pretrained(model)

    # pipeline=transformers.pipeline(
    #   "text-generation",
    #   model=model,
    #   tokenizer=tokenizer,
    #   torch_dtype=torch.bfloat16,
    #   trust_remote_code=True,
    #   device_map="auto",
    #   max_length=3000,
    #   do_sample=True,
    #   top_k=10,
    #   num_return_sequences=1,
    #   eos_token_id=tokenizer.eos_token_id
    #   )

    # llm=HuggingFacePipeline(pipeline=pipeline, model_kwargs={'temperature': 0.7})

    # template = """
    #             Write a summary of the following text delimited by triple backticks.
    #             Return your response which covers the key points of the text.
    #             ```{text}```
    #             SUMMARY:
    #           """

    # prompt = PromptTemplate(template=template, input_variables=["text"])
    # llm_chain = LLMChain(prompt=prompt, llm=llm)

    # #LSA Optimization to remove Redundant Data
    # article_number_of_tokens = len(tokenizer.encode(text))
    # prompt_number_of_tokens= len(tokenizer.encode(template))
    # max_tokens = 4096
    # output_tokens = 3000
    # article_ideal_number_of_token = (max_tokens - output_tokens - prompt_number_of_tokens)

    # #print(f"Number of tokens in the prompt {prompt_number_of_tokens}")
    # #print(f"Maximum tokens the article can have {article_ideal_number_of_token}")
    # #print(f"Number of tokens in the article has is {article_number_of_tokens}")

    # nltk.download('punkt')

    # def truncate_text(
    #   text: str, llm_max_tokens: int, hf_tokenizer: AutoTokenizer, LANGUAGE="english"
    # ) -> str:
    #   """
    #   Truncate_text using LSA summarization to reduce the text using the number of input token the LLM
    #   accept.


    #   Args:
    #       text (str): The text that need to be truncate
    #       llm_max_tokens (int): Maximum number of tokens the LLM support.
    #       hf_tokenizer (AutoTokenizer): HuggingFace tokenizer. Use to calculate number of tokens.


    #   Retruns:
    #       Summary (str)
    #   """

    #   summarizer = LsaSummarizer()

    #   # How many toke the text have?
    #   num_tokens = len(hf_tokenizer.encode(text))


    #   if num_tokens > llm_max_tokens:
    #       #print(f"Text is too long. Splitting into chunks of {llm_max_tokens} tokens")
    #       parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))
    #       num_sentences = len(parser.document.sentences)
    #       avg_tokens_per_sentence = int(num_tokens / num_sentences)
    #       excess_tokens = num_tokens - llm_max_tokens
    #       num_sentences_to_summarize = num_sentences - (
    #           math.ceil(excess_tokens / avg_tokens_per_sentence)
    #       )


    #       #print(f"Number of tokens: {num_tokens}.")
    #       #print(f"Number of sentences: {num_sentences}.")
    #       #print(f"Average tokens per sentence: {avg_tokens_per_sentence}.")
    #       #print(f"Excess tokens: {excess_tokens}.")
    #       #print(f"Number of sentences to summarize: {num_sentences_to_summarize}")


    #       summary = summarizer(parser.document, num_sentences_to_summarize)
    #       summary_text = "\n".join([sentence._text for sentence in summary])
    #       return truncate_text(summary_text, llm_max_tokens, hf_tokenizer)


    #   else:
    #       #print("Text is short enough. No need to summarizing.")
    #       return text

    # short_article = truncate_text(text=text, llm_max_tokens=article_ideal_number_of_token, hf_tokenizer=tokenizer)

    # #print(f"Short article number of tokens {len(tokenizer.encode(short_article))}")
    # #print("\n"+short_article)

    # output = llm_chain.run(short_article)

    st.markdown('*** Summarized Test: ***')
    # st.info(output)