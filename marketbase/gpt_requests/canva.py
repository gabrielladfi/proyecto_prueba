import os
from openai import OpenAI

OPENAI_KEY="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"


def propuesta_valor(text):

    client = OpenAI(
        api_key=f"{OPENAI_KEY}"
    )
    
    
    prompt = f""" Eres experto en creación de empresas,  se creativo, nivel de pensamiento al estilo MBA, estás creando el modelo canvas para emprededores, 
            crea la propuesta de valor del modelo canvas,
            no incluyas la frase la propuesta de valor,
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

def segmento_clientes(text):

    client = OpenAI(
        api_key=f"{OPENAI_KEY}"
    )
    
    
    prompt = f""" Eres experto en creación de empresas,  se creativo, nivel de pensamiento al estilo MBA, estás creando el modelo canvas para emprededores, 
            crea la segmento clientes del modelo canvas,
            no incluyas la frase la segmento clientes,
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

def canales(text):

    client = OpenAI(
        api_key=f"{OPENAI_KEY}"
    )
    
    
    prompt = f""" Eres experto en creación de empresas,  se creativo, nivel de pensamiento al estilo MBA, estás creando el modelo canvas para emprededores, 
            crea los canales del modelo canvas,
            no incluyas la frase canales de comunicación,
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

def relacion_clientes(text):

    client = OpenAI(
        api_key=f"{OPENAI_KEY}"
    )
    
    
    prompt = f""" Eres experto en creación de empresas,  se creativo, nivel de pensamiento al estilo MBA, estás creando el modelo canvas para emprededores, 
            crea la relación con los clientes del modelo canvas,
            no incluyas la frase la clientes,
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

def fuentes_ingresos(text):

    client = OpenAI(
        api_key=f"{OPENAI_KEY}"
    )
    
    
    prompt = f""" Eres experto en creación de empresas,  se creativo, nivel de pensamiento al estilo MBA, estás creando el modelo canvas para emprededores, 
            crea la fuentes de ingresos del modelo canvas,
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

def relaciones_clave(text):

    client = OpenAI(
        api_key=f"{OPENAI_KEY}"
    )
    
    
    prompt = f""" Eres experto en creación de empresas,  se creativo, nivel de pensamiento al estilo MBA, estás creando el modelo canvas para emprededores, 
            crea las relaciones clave del modelo canvas,
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

def socios_clave(text):

    client = OpenAI(
        api_key=f"{OPENAI_KEY}"
    )
    
    
    prompt = f""" Eres experto en creación de empresas,  se creativo, nivel de pensamiento al estilo MBA, estás creando el modelo canvas para emprededores, 
            crea los socios clave del modelo canvas,
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

def actividades_clave(text):

    client = OpenAI(
        api_key=f"{OPENAI_KEY}"
    )
    
    
    prompt = f""" Eres experto en creación de empresas,  se creativo, nivel de pensamiento al estilo MBA, estás creando el modelo canvas para emprededores, 
            crea los actividades clave del modelo canvas,
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
    

def estructura_costos(text):

    client = OpenAI(
        api_key=f"{OPENAI_KEY}"
    )
    
    
    prompt = f""" Eres experto en creación de empresas,  se creativo, nivel de pensamiento al estilo MBA, estás creando el modelo canvas para emprededores, 
            crea la estructura de costos clave del modelo canvas,
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
    
    
    
    