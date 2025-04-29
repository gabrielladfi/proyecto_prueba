import os
from openai import OpenAI

OPENAI_KEY="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"

def hook_elevator(text):

    client = OpenAI(
        api_key=f"{OPENAI_KEY}"
    )
    
    
    prompt = f""" Eres experto en creación de elevator pitch para levantamiento de capital,  
            se creativo, nivel de pensamiento al estilo MBA, 
            redacta el gancho (hook) ideal para un elevator pitch, 
            el gancho (hook) debe ser muy breve para llamar la atención, el hook es para llamar la atención del público,
            no des explicaciones sobre tus respuesta, solo genera el texto para copiar y pegarlo en un documento,
            sobre una empresa para que esté en una landing page para una empresa que 
            cumple las siguientes características:  : {text}"""

    response = client.responses.create(
        model="gpt-3.5-turbo",
        input=prompt
    )

    try:
        print(response.output_text)
        return response.output_text
    except Exception as e:
        print(e)
        return ""

def problem_elevator(text):

    client = OpenAI(
        api_key=f"{OPENAI_KEY}"
    )
    
    
    prompt = f""" Eres experto en creación de elevator pitch para levantamiento de capital,  
            se creativo, nivel de pensamiento al estilo MBA, 
            redacta el problema a solucionar (problem) ideal para un elevator pitch,
            se breve, 
            no des explicaciones sobre tus respuesta, solo genera el texto para copiar y pegarlo en un documento,
            sobre una empresa que
            cumple las siguientes características:  : {text}"""

    response = client.responses.create(
        model="gpt-3.5-turbo",
        input=prompt
    )

    try:
        print(response.output_text)
        return response.output_text
    except Exception as e:
        print(e)
        return ""


def solución_elevator(text):

    client = OpenAI(
        api_key=f"{OPENAI_KEY}"
    )
    
    
    prompt = f""" Eres experto en creación de elevator pitch para levantamiento de capital,  
            se creativo, nivel de pensamiento al estilo MBA, 
            redacta la solución, vende la empresa como una solución,
            se breve, 
            no des explicaciones sobre tus respuesta, solo genera el texto para copiar y pegarlo en un documento,
            sobre una empresa que
            cumple las siguientes características:  : {text}"""

    response = client.responses.create(
        model="gpt-3.5-turbo",
        input=prompt
    )

    try:
        print(response.output_text)
        return response.output_text
    except Exception as e:
        print(e)
        return ""

def market_elevator(text):

    client = OpenAI(
        api_key=f"{OPENAI_KEY}"
    )
    
    
    prompt = f""" Eres experto en creación de elevator pitch para levantamiento de capital,  
            se creativo, nivel de pensamiento al estilo MBA, 
            redacta la descripción del mercado, el mercado objetivo de la empresa,
            se breve, 
            no des explicaciones sobre tus respuesta, solo genera el texto para copiar y pegarlo en un documento,
            sobre una empresa que
            cumple las siguientes características:  : {text}"""

    response = client.responses.create(
        model="gpt-3.5-turbo",
        input=prompt
    )

    try:
        print(response.output_text)
        return response.output_text
    except Exception as e:
        print(e)
        return ""

def modelbusiness_elevator(text):

    client = OpenAI(
        api_key=f"{OPENAI_KEY}"
    )
    
    
    prompt = f""" Eres experto en creación de elevator pitch para levantamiento de capital,  
            se creativo, nivel de pensamiento al estilo MBA, 
            redacta el modelo de negocio, el modelo de negocio de la empresa para el elevator pitch,
            se breve, 
            no des explicaciones sobre tus respuesta, solo genera el texto para copiar y pegarlo en un documento,
            sobre una empresa que
            cumple las siguientes características:  : {text}"""

    response = client.responses.create(
        model="gpt-3.5-turbo",
        input=prompt
    )

    try:
        print(response.output_text)
        return response.output_text
    except Exception as e:
        print(e)
        return ""

def action_elevator(text):

    client = OpenAI(
        api_key=f"{OPENAI_KEY}"
    )
    
    
    prompt = f""" Eres experto en creación de elevator pitch para levantamiento de capital,  
            se creativo, nivel de pensamiento al estilo MBA, 
            redacta el call to action (llamado a la acción) del negocio, redacta únicamente el call to action  elevator pitch,
            se breve, 
            no des explicaciones sobre tus respuesta, solo genera el texto para copiar y pegarlo en un documento,
            sobre una empresa que
            cumple las siguientes características:  : {text}"""

    response = client.responses.create(
        model="gpt-3.5-turbo",
        input=prompt
    )

    try:
        print(response.output_text)
        return response.output_text
    except Exception as e:
        print(e)
        return ""
