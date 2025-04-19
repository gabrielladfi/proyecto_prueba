import os
from openai import OpenAI

OPENAI_KEY="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"

def gentitle_landing(text):

    client = OpenAI(
        api_key=f"{OPENAI_KEY}"
    )

    
    prompt = f""" Eres experto en marketing, creación de Lading Pages, se creativo, nivel de pensamiento al estilo MBA, 
                  no des explicaciones sobre tus respuesta, solo genera el texto para copiar y pegarlo en la landing page,
            crea un Título de una landing page para una empresa que cumple las siguientes características:  : {text}"""

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


def gendescription_landing(text):

    client = OpenAI(
        api_key=f"{OPENAI_KEY}"
    )

    
    prompt = f""" Eres experto en marketing, creación de Lading Pages, debe ser una descripción breve, se creativo, nivel de pensamiento al estilo MBA, 
            no des explicaciones sobre tus respuesta, solo genera el texto para copiar y pegarlo en la landing page,
            crea una breve descripción sobre una empresa para que esté en una landing page para una empresa que 
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

def gencall_action(text):

    client = OpenAI(
        api_key=f"{OPENAI_KEY}"
    )
    
    
    prompt = f""" Eres experto en marketing, creación de Lading Pages, se creativo, nivel de pensamiento al estilo MBA, 
            crea una breve call to action, un call to action debe ser muy corto para colocarlo en un boton, 
            no des explicaciones sobre tus respuesta, solo genera el texto para copiar y pegarlo en la landing page,
            solo usa frases como 'contáctanos', 'agenda una llamada', 'compra ya', dependiendo del contexto de la empresa,
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
    

def gencall_action(text):

    client = OpenAI(
        api_key=f"{OPENAI_KEY}"
    )
    
    
    prompt = f""" Eres experto en marketing, creación de Lading Pages, se creativo, nivel de pensamiento al estilo MBA, 
            crea el texto que debería ir  'sobre nosotros' (about us en inglés),
            no des explicaciones sobre tus respuesta, solo genera el texto para copiar y pegarlo en la landing page,
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

def gen_benefits(text):

    client = OpenAI(
        api_key=f"{OPENAI_KEY}"
    )
    
    
    prompt = f""" Eres experto en marketing, creación de Lading Pages, se creativo, nivel de pensamiento al estilo MBA, 
            crea el texto que debería ir  en los beneficios que ofrece la compañia,
            no des explicaciones sobre tus respuesta, solo genera el texto para copiar y pegarlo en la landing page,
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
    
def gen_testimonials(text):

    client = OpenAI(
        api_key=f"{OPENAI_KEY}"
    )
    
    
    prompt = f""" Eres experto en marketing, creación de Lading Pages, se creativo, nivel de pensamiento al estilo MBA, 
            crea textos de ejemplo para los testimonios sobre la empresa, incluye nombres falsos y una descripción del testimonio,
            no des explicaciones sobre tus respuesta, solo genera el texto para copiar y pegarlo en la landing page,
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

def gen_faqs(text):

    client = OpenAI(
        api_key=f"{OPENAI_KEY}"
    )
    
    
    prompt = f""" Eres experto en marketing, creación de Lading Pages, se creativo, nivel de pensamiento al estilo MBA, 
            crea un texto de ejemplo sobre los FAQS, preguntas frecuentes,
            no des explicaciones sobre tus respuesta, solo genera el texto para copiar y pegarlo en la landing page,
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
    
    
    
company_context = "Empresa de consultoría financiera para pequeñas, startups, levantamiento de capital, llamada Delta Advisors"
gentitle_landing(company_context)
gendescription_landing(company_context)
gencall_action(company_context)
gencall_action(company_context)
gen_benefits(company_context)
gen_testimonials(company_context)
gen_faqs(company_context)