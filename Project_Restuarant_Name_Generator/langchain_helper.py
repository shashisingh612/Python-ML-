import secret_key
import streamlit as st
import os
from langchain.llms import OpenAI

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def generate_restaurant_name_and_items(cuisine):

    os.environ['OPENAI_API_KEY']= st.secrets["api_key"]
    llm = OpenAI(temperature=0.9)

    prompt_template_name = PromptTemplate(
        input_variables = ['cuisine'],
        template = "I want to open a restaurant for {cuisine} food. Please suggest only one fancy name "
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    prompt_template_items = PromptTemplate(
        input_variables = ['restaurant_name'],
        template = "Suggest some menu items for {restaurant_name}. Return it in tabular form with 10 rows and 2 columns, name and description"
    )
    food_item_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key = "menu_items")

    from langchain.chains import SequentialChain

    chain = SequentialChain(
        chains= [name_chain, food_item_chain],
        input_variables = ['cuisine'],
        output_variables = ['restaurant_name','menu_items']
    )

    return(chain({'cuisine' :cuisine}))