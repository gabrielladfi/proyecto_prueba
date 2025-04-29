from demo_canva import propuesta_valor 
from demo_canva import segmento_clientes 
from demo_canva import canales 
from demo_canva import relacion_clientes 
from demo_canva import fuentes_ingresos 
from demo_canva import relaciones_clave
from demo_canva import socios_clave
from demo_canva import actividades_clave
from demo_canva import estructura_costos

from demo_epitch import hook_elevator
from demo_epitch import problem_elevator
from demo_epitch import solución_elevator
from demo_epitch import market_elevator
from demo_epitch import modelbusiness_elevator
from demo_epitch import action_elevator

from demo_landing import gentitle_landing
from demo_landing import gendescription_landing
from demo_landing import gencall_action
from demo_landing import gencall_action
from demo_landing import gen_benefits
from demo_landing import gen_testimonials
from demo_landing import gen_faqs


import time







###### Flujo Canva
def generar_canva(company_name, problem, target_age, target_location, target_interest, differential_factor, communication_type, call_actions):
    context = f""" Nombre de la empresa: {company_name}  
                   Problema que soluciona: {problem},  
                   edad del target: {target_age},
                   ubicación del target: {target_location},
                   target_interest: {target_interest},
                   differential_factor: {differential_factor},
                   communication_type: {communication_type},
                   call_actions: {call_actions}
                   """
    
    generado_propuesta = propuesta_valor(context)
    generado_segmento = segmento_clientes(context)
    generado_canales = canales(context)
    generado_relacion = relacion_clientes(context)
    generado_fuentes = fuentes_ingresos(context)
    generado_relaciones_clave = relaciones_clave(context)
    generado_actividades_clave = actividades_clave(context)
    generado_socios_clave = socios_clave(context)
    generado_estructura_costos = estructura_costos(context)

    respuesta = {
        "propuesta_valor": generado_propuesta,
        "segmento_clientes": generado_segmento,
        "generado_canales": generado_canales, 
        "relacion_clientes":generado_relacion,
        "fuentes_ingresos": generado_fuentes,
        "relaciones_clave":generado_relaciones_clave,
        "actividades_clave": generado_actividades_clave,
        "socios_clave": generado_socios_clave,
        "estructura_costos": generado_estructura_costos
    }

    time.sleep(5)

    return respuesta



###### Flujo Elevator Pitch
def generar_epitch(company_name, problem, target_age, target_location, target_interest, differential_factor, communication_type, call_actions):
    context = f""" Nombre de la empresa: {company_name}  
                   Problema que soluciona: {problem},  
                   edad del target: {target_age},
                   ubicación del target: {target_location},
                   target_interest: {target_interest},
                   differential_factor: {differential_factor},
                   communication_type: {communication_type},
                   call_actions: {call_actions}
                   """
    
    generado_hook = hook_elevator(context)
    generado_problem = problem_elevator(context)
    generado_solution = solución_elevator(context)
    generado_market = market_elevator(context)
    generado_model = modelbusiness_elevator(context)
    generado_action = action_elevator(context)

    respuesta = {
        "hook_elevator": generado_hook,
        "problem_elevator": generado_problem,
        "solución_elevator": generado_solution, 
        "market_elevator":generado_market,
        "modelbusiness_elevator": generado_model,
        "action_elevator":generado_action
    }


    return respuesta



###### Flujo Canva
def generar_landing(company_name, problem, target_age, target_location, target_interest, differential_factor, communication_type, call_actions):
    context = f""" Nombre de la empresa: {company_name}  
                   Problema que soluciona: {problem},  
                   edad del target: {target_age},
                   ubicación del target: {target_location},
                   target_interest: {target_interest},
                   differential_factor: {differential_factor},
                   communication_type: {communication_type},
                   call_actions: {call_actions}
                   """
    
    
    generado_title = gentitle_landing(context)
    generado_description = gendescription_landing(context)
    generado_action = gencall_action(context)
    generado_benefits = gen_benefits(context)
    generado_testimonials = gen_testimonials(context)
    generado_faqs = gen_faqs(context)

    respuesta = {
        "gentitle_landing": generado_title,
        "gendescription_landing": generado_description,
        "gencall_action": generado_action, 
        "gen_benefits":generado_benefits,
        "gen_testimonials": generado_testimonials,
        "gen_faqs":generado_faqs,
    }

    return respuesta


###### Entradas del flujo

company_name = "Joyas Corleone"
problem = "Existen comunidades indigenas que tienen muchas artesanias con esmeraldas, usando hilos nativos, pero no tienen como venderlo"
target_age = "entre los 30 años a 50 años"
target_location = "Colombia"
target_interest = "Apoyar comunidades indigenas, crear canales de ventas entre las comunidades indigenas y comprandores, joyas innovadoras"
differential_factor = "Diseños de joyas nunca antes vistas"
communication_type = "e-commerce responsive, redes sociales"
call_actions = "comprar joyas"

data = {
    "company_name": company_name,
    "problem": problem,
    "target_age": target_age,
    "target_location": target_location,
    "target_interest": target_interest,
    "differential_factor": differential_factor,
    "communication_type": communication_type,
    "call_actions": call_actions
}

respuesta = generar_landing(
    data["company_name"],
    data["problem"],
    data["target_age"],
    data["target_location"],
    data["target_interest"],
    data["differential_factor"],
    data["communication_type"],
    data["call_actions"]
    )

print(respuesta)



