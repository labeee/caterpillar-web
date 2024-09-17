import math
import streamlit as st

def ort_ff(a: float, b: float, c: float) -> float:
    """
    Calculates the orthogonal form factor.

    Args:
        a (float): The perpendicular measurement from c.
        b (float): The rest.
        c (float): The distance from the center of the plain to the reference point.

    Returns:
        form_factor (float): The orthogonal form factor.
    """

    x = a / b
    y = c / b

    form_factor = (1 / (2 * math.pi)) * (math.atan(1 / y) - (y / math.sqrt(x**2 + y**2)) * math.atan(1 / math.sqrt(x**2 + y**2)))
    return round(form_factor, 14)

def par_ff(a: float, b: float, c: float) -> float:
    """
    Calculates the paralel form factor.

    Args:
        a (float): The perpendicular measurement from c.
        b (float): The rest.
        c (float): The distance from the center of the plain to the reference point.

    Returns:
        form_factor (float): The paralel form factor.
    """
    x = a / c
    y = b / c

    form_factor = (1 / (2 * math.pi)) * ((x / math.sqrt(1 + x**2)) * math.atan(y / math.sqrt(1 + x**2)) + (y / math.sqrt(1 + y**2)) * math.atan(x / math.sqrt(1 + y**2)))
    return round(form_factor, 14)

def assimetry(largura, comprimento, altura, x, y, z, frontal, posterior, teto, piso, lat_dir, lat_esq):

    temp_frontal = frontal
    temp_posterior = posterior
    temp_teto = teto
    temp_piso = piso
    temp_lat_dir = lat_dir
    temp_lat_esq = lat_esq
    largura = largura
    comprimento = comprimento
    altura = altura
    x = x
    y = y
    z = z

    inputs = f"""
---
## Inputs
    {temp_frontal=}
    {temp_posterior=}
    {temp_teto=}
    {temp_piso=}
    {temp_lat_dir=}
    {temp_lat_esq=}
    {largura=}
    {comprimento=}
    {altura=}
    {x=}
    {y=}
    {z=}
"""

    temps = {
    'temp_frontal': temp_frontal,
    'temp_posterior': temp_posterior,
    'temp_teto': temp_teto,
    'temp_piso': temp_piso,
    'temp_lat_direita': temp_lat_dir,
    'temp_lat_esquerda': temp_lat_esq
    }

    for key in temps:
        temps[key] += 273.15

    room = {
        'largura': largura,
        'comprimento': comprimento,
        'altura': altura,
        'pos_x': x,
        'pos_y': y,
        'pos_z': z
    }

    coordinates = {
        'dist_frontal': room['pos_y'],
        'dist_posterior': room['comprimento'] - room['pos_y'],
        'dist_piso': room['pos_z'],
        'dist_teto': room['altura'] - room['pos_z'],
        'dist_lat_direita': room['pos_x'],
        'dist_lat_esquerda': room['largura'] - room['pos_x'],
    }


    ## CÁLCULO FRONTAL E POSTERIOR
    ort_ff_frontal_dict = {
        'ff_teto_dir': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_lat_direita'], c=coordinates['dist_teto']),
        'ff_teto_esq': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_lat_esquerda'], c=coordinates['dist_teto']),
        'ff_piso_dir': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_lat_direita'], c=coordinates['dist_piso']),
        'ff_piso_esq': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_lat_esquerda'], c=coordinates['dist_piso']),
        'ff_lat_dir_baixo': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_piso'], c=coordinates['dist_lat_direita']),
        'ff_lat_dir_cima': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_teto'], c=coordinates['dist_lat_direita']),
        'ff_lat_esq_baixo': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_piso'], c=coordinates['dist_lat_esquerda']),
        'ff_lat_esq_cima': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_teto'], c=coordinates['dist_lat_esquerda'])
    }

    ort_ff_posterior_dict = {
        'ff_teto_esq': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_lat_esquerda'], c=coordinates['dist_teto']),
        'ff_teto_dir': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_lat_direita'], c=coordinates['dist_teto']),
        'ff_piso_esq': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_lat_esquerda'], c=coordinates['dist_piso']),
        'ff_piso_dir': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_lat_direita'], c=coordinates['dist_piso']),
        'ff_lat_esq_baixo': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_piso'], c=coordinates['dist_lat_esquerda']),
        'ff_lat_esq_cima': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_teto'], c=coordinates['dist_lat_esquerda']),
        'ff_lat_dir_baixo': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_piso'], c=coordinates['dist_lat_direita']),
        'ff_lat_dir_cima': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_teto'], c=coordinates['dist_lat_direita'])
    }

    par_ff_dict = {
        'ff_frontal_quad_1': par_ff(b=coordinates['dist_teto'], a=coordinates['dist_lat_direita'], c=coordinates['dist_frontal']),
        'ff_frontal_quad_2': par_ff(b=coordinates['dist_teto'], a=coordinates['dist_lat_esquerda'], c=coordinates['dist_frontal']),
        'ff_frontal_quad_3': par_ff(b=coordinates['dist_piso'], a=coordinates['dist_lat_esquerda'], c=coordinates['dist_frontal']),
        'ff_frontal_quad_4': par_ff(b=coordinates['dist_piso'], a=coordinates['dist_lat_direita'], c=coordinates['dist_frontal']),
        'ff_posterior_quad_1': par_ff(b=coordinates['dist_teto'], a=coordinates['dist_lat_esquerda'], c=coordinates['dist_posterior']),
        'ff_posterior_quad_2': par_ff(b=coordinates['dist_teto'], a=coordinates['dist_lat_direita'], c=coordinates['dist_posterior']),
        'ff_posterior_quad_3': par_ff(b=coordinates['dist_piso'], a=coordinates['dist_lat_direita'], c=coordinates['dist_posterior']),
        'ff_posterior_quad_4': par_ff(b=coordinates['dist_piso'], a=coordinates['dist_lat_esquerda'], c=coordinates['dist_posterior'])
    }

    conferencia = {
        'sum_ff_frontal': round((sum(ort_ff_frontal_dict.values()) + par_ff_dict['ff_frontal_quad_1'] + par_ff_dict['ff_frontal_quad_2'] + par_ff_dict['ff_frontal_quad_3'] + par_ff_dict['ff_frontal_quad_4']), 14),
        'sum_ff_posterior': round((sum(ort_ff_posterior_dict.values()) + par_ff_dict['ff_posterior_quad_1'] + par_ff_dict['ff_posterior_quad_2'] + par_ff_dict['ff_posterior_quad_3'] + par_ff_dict['ff_posterior_quad_4']), 14)
    }

    ajuste_frontal = 0
    ajuste_posterior = 0

    if conferencia['sum_ff_frontal'] != 1:
        ajuste_frontal = conferencia['sum_ff_frontal']
        ajuste_frontal = 1 - ajuste_frontal
        ajuste_frontal = ajuste_frontal / 4

    if conferencia['sum_ff_posterior'] != 1:
        ajuste_posterior = conferencia['sum_ff_posterior']
        ajuste_posterior = 1 - ajuste_posterior
        ajuste_posterior = ajuste_posterior / 4

    result_data = {
        'ff_frontal_total': round((par_ff_dict['ff_frontal_quad_1'] + par_ff_dict['ff_frontal_quad_2'] + par_ff_dict['ff_frontal_quad_3'] + par_ff_dict['ff_frontal_quad_4']), 14),
        'ff_posterior_total': round((par_ff_dict['ff_posterior_quad_1'] + par_ff_dict['ff_posterior_quad_2'] + par_ff_dict['ff_posterior_quad_3'] + par_ff_dict['ff_posterior_quad_4']), 14),
        'ff_frontal_lat_dir_total': round(((ort_ff_frontal_dict['ff_lat_dir_baixo'] + ort_ff_frontal_dict['ff_lat_dir_cima']) + ajuste_frontal), 14),
        'ff_frontal_lat_esq_total': round(((ort_ff_frontal_dict['ff_lat_esq_baixo'] + ort_ff_frontal_dict['ff_lat_esq_cima']) + ajuste_frontal), 14),
        'ff_posterior_lat_dir_total': round(((ort_ff_posterior_dict['ff_lat_dir_baixo'] + ort_ff_posterior_dict['ff_lat_dir_cima']) + ajuste_posterior), 14),
        'ff_posterior_lat_esq_total': round(((ort_ff_posterior_dict['ff_lat_esq_baixo'] + ort_ff_posterior_dict['ff_lat_esq_cima']) + ajuste_posterior), 14),
        'ff_frontal_teto_total': round(((ort_ff_frontal_dict['ff_teto_dir'] + ort_ff_frontal_dict['ff_teto_esq']) + ajuste_frontal), 14),
        'ff_frontal_piso_total': round(((ort_ff_frontal_dict['ff_piso_dir'] + ort_ff_frontal_dict['ff_piso_esq']) + ajuste_frontal), 14),
        'ff_posterior_teto_total': round(((ort_ff_posterior_dict['ff_teto_dir'] + ort_ff_posterior_dict['ff_teto_esq']) + ajuste_posterior), 14),
        'ff_posterior_piso_total': round(((ort_ff_posterior_dict['ff_piso_dir'] + ort_ff_posterior_dict['ff_piso_esq']) + ajuste_posterior), 14)
    }

    radiant_temperatures = {
        'frontal': round((((temps['temp_frontal']**4)*result_data['ff_frontal_total']) + ((temps['temp_lat_direita']**4)*result_data['ff_frontal_lat_dir_total']) + ((temps['temp_lat_esquerda']**4)*result_data['ff_frontal_lat_esq_total']) + ((temps['temp_teto']**4)*result_data['ff_frontal_teto_total']) + ((temps['temp_piso']**4)*result_data['ff_frontal_piso_total']))**0.25, 14),
        'posterior': round((((temps['temp_posterior']**4)*result_data['ff_posterior_total']) + ((temps['temp_lat_direita']**4)*result_data['ff_posterior_lat_dir_total']) + ((temps['temp_lat_esquerda']**4)*result_data['ff_posterior_lat_esq_total']) + ((temps['temp_teto']**4)*result_data['ff_posterior_teto_total']) + ((temps['temp_piso']**4)*result_data['ff_posterior_piso_total']))**0.25, 14)
    }

    radiant_temperatures['frontal_celsius'] = round((radiant_temperatures['frontal'] - 273.15), 14)
    radiant_temperatures['posterior_celsius'] = round((radiant_temperatures['posterior'] - 273.15), 14)
    radiant_temperatures['assimetry'] = round(abs(radiant_temperatures['frontal'] - radiant_temperatures['posterior']), 14)

    resultados_frontal = f"""
## FRONTAL E POSTERIOR

### TEMPERATURAS RADIANTES

- Frontal: {round(radiant_temperatures['frontal_celsius'], 2)}°C
- Posterior: {round(radiant_temperatures['posterior_celsius'], 2)}°C
- Assimetria: {round(radiant_temperatures['assimetry'], 2)}°C

### FATORES DE FORMA FRONTAIS

- Parede frontal: {result_data['ff_frontal_total']}
- Lateral direita: {result_data['ff_frontal_lat_dir_total']}
- Lateral esquerda: {result_data['ff_frontal_lat_esq_total']}
- Teto: {result_data['ff_frontal_teto_total']}
- Piso: {result_data['ff_frontal_piso_total']}

### FATORES DE FORMA POSTERIORES

- Parede posterior: {result_data['ff_posterior_total']}
- Lateral direita: {result_data['ff_posterior_lat_dir_total']}
- Lateral esquerda: {result_data['ff_posterior_lat_esq_total']}
- Teto: {result_data['ff_posterior_teto_total']}
- Piso: {result_data['ff_posterior_piso_total']}"""

    ## CÁLCULO ESQUERDA E DIREITA
    temps = {
    'temp_frontal': temp_lat_esq,
    'temp_posterior': temp_lat_dir,
    'temp_teto': temp_teto,
    'temp_piso': temp_piso,
    'temp_lat_direita': temp_frontal,
    'temp_lat_esquerda': temp_posterior
    }

    for key in temps:
        temps[key] += 273.15

    coordinates = {
        'dist_frontal': room['largura'] - room['pos_x'],
        'dist_posterior': room['pos_x'],
        'dist_piso': room['pos_z'],
        'dist_teto': room['altura'] - room['pos_z'],
        'dist_lat_direita': room['pos_y'],
        'dist_lat_esquerda': room['comprimento'] - room['pos_y'],
    }

    ort_ff_frontal_dict = {
        'ff_teto_dir': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_lat_direita'], c=coordinates['dist_teto']),
        'ff_teto_esq': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_lat_esquerda'], c=coordinates['dist_teto']),
        'ff_piso_dir': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_lat_direita'], c=coordinates['dist_piso']),
        'ff_piso_esq': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_lat_esquerda'], c=coordinates['dist_piso']),
        'ff_lat_dir_baixo': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_piso'], c=coordinates['dist_lat_direita']),
        'ff_lat_dir_cima': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_teto'], c=coordinates['dist_lat_direita']),
        'ff_lat_esq_baixo': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_piso'], c=coordinates['dist_lat_esquerda']),
        'ff_lat_esq_cima': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_teto'], c=coordinates['dist_lat_esquerda'])
    }

    ort_ff_posterior_dict = {
        'ff_teto_esq': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_lat_esquerda'], c=coordinates['dist_teto']),
        'ff_teto_dir': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_lat_direita'], c=coordinates['dist_teto']),
        'ff_piso_esq': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_lat_esquerda'], c=coordinates['dist_piso']),
        'ff_piso_dir': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_lat_direita'], c=coordinates['dist_piso']),
        'ff_lat_esq_baixo': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_piso'], c=coordinates['dist_lat_esquerda']),
        'ff_lat_esq_cima': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_teto'], c=coordinates['dist_lat_esquerda']),
        'ff_lat_dir_baixo': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_piso'], c=coordinates['dist_lat_direita']),
        'ff_lat_dir_cima': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_teto'], c=coordinates['dist_lat_direita'])
    }

    par_ff_dict = {
        'ff_frontal_quad_1': par_ff(b=coordinates['dist_teto'], a=coordinates['dist_lat_direita'], c=coordinates['dist_frontal']),
        'ff_frontal_quad_2': par_ff(b=coordinates['dist_teto'], a=coordinates['dist_lat_esquerda'], c=coordinates['dist_frontal']),
        'ff_frontal_quad_3': par_ff(b=coordinates['dist_piso'], a=coordinates['dist_lat_esquerda'], c=coordinates['dist_frontal']),
        'ff_frontal_quad_4': par_ff(b=coordinates['dist_piso'], a=coordinates['dist_lat_direita'], c=coordinates['dist_frontal']),
        'ff_posterior_quad_1': par_ff(b=coordinates['dist_teto'], a=coordinates['dist_lat_esquerda'], c=coordinates['dist_posterior']),
        'ff_posterior_quad_2': par_ff(b=coordinates['dist_teto'], a=coordinates['dist_lat_direita'], c=coordinates['dist_posterior']),
        'ff_posterior_quad_3': par_ff(b=coordinates['dist_piso'], a=coordinates['dist_lat_direita'], c=coordinates['dist_posterior']),
        'ff_posterior_quad_4': par_ff(b=coordinates['dist_piso'], a=coordinates['dist_lat_esquerda'], c=coordinates['dist_posterior'])
    }

    conferencia = {
        'sum_ff_frontal': round((sum(ort_ff_frontal_dict.values()) + par_ff_dict['ff_frontal_quad_1'] + par_ff_dict['ff_frontal_quad_2'] + par_ff_dict['ff_frontal_quad_3'] + par_ff_dict['ff_frontal_quad_4']), 14),
        'sum_ff_posterior': round((sum(ort_ff_posterior_dict.values()) + par_ff_dict['ff_posterior_quad_1'] + par_ff_dict['ff_posterior_quad_2'] + par_ff_dict['ff_posterior_quad_3'] + par_ff_dict['ff_posterior_quad_4']), 14)
    }

    ajuste_frontal = 0
    ajuste_posterior = 0

    if conferencia['sum_ff_frontal'] != 1:
        ajuste_frontal = conferencia['sum_ff_frontal']
        ajuste_frontal = 1 - ajuste_frontal
        ajuste_frontal = ajuste_frontal / 4

    if conferencia['sum_ff_posterior'] != 1:
        ajuste_posterior = conferencia['sum_ff_posterior']
        ajuste_posterior = 1 - ajuste_posterior
        ajuste_posterior = ajuste_posterior / 4

    result_data = {
        'ff_frontal_total': round((par_ff_dict['ff_frontal_quad_1'] + par_ff_dict['ff_frontal_quad_2'] + par_ff_dict['ff_frontal_quad_3'] + par_ff_dict['ff_frontal_quad_4']), 14),
        'ff_posterior_total': round((par_ff_dict['ff_posterior_quad_1'] + par_ff_dict['ff_posterior_quad_2'] + par_ff_dict['ff_posterior_quad_3'] + par_ff_dict['ff_posterior_quad_4']), 14),
        'ff_frontal_lat_dir_total': round(((ort_ff_frontal_dict['ff_lat_dir_baixo'] + ort_ff_frontal_dict['ff_lat_dir_cima']) + ajuste_frontal), 14),
        'ff_frontal_lat_esq_total': round(((ort_ff_frontal_dict['ff_lat_esq_baixo'] + ort_ff_frontal_dict['ff_lat_esq_cima']) + ajuste_frontal), 14),
        'ff_posterior_lat_dir_total': round(((ort_ff_posterior_dict['ff_lat_dir_baixo'] + ort_ff_posterior_dict['ff_lat_dir_cima']) + ajuste_posterior), 14),
        'ff_posterior_lat_esq_total': round(((ort_ff_posterior_dict['ff_lat_esq_baixo'] + ort_ff_posterior_dict['ff_lat_esq_cima']) + ajuste_posterior), 14),
        'ff_frontal_teto_total': round(((ort_ff_frontal_dict['ff_teto_dir'] + ort_ff_frontal_dict['ff_teto_esq']) + ajuste_frontal), 14),
        'ff_frontal_piso_total': round(((ort_ff_frontal_dict['ff_piso_dir'] + ort_ff_frontal_dict['ff_piso_esq']) + ajuste_frontal), 14),
        'ff_posterior_teto_total': round(((ort_ff_posterior_dict['ff_teto_dir'] + ort_ff_posterior_dict['ff_teto_esq']) + ajuste_posterior), 14),
        'ff_posterior_piso_total': round(((ort_ff_posterior_dict['ff_piso_dir'] + ort_ff_posterior_dict['ff_piso_esq']) + ajuste_posterior), 14)
    }

    radiant_temperatures = {
        'frontal': round((((temps['temp_frontal']**4)*result_data['ff_frontal_total']) + ((temps['temp_lat_direita']**4)*result_data['ff_frontal_lat_dir_total']) + ((temps['temp_lat_esquerda']**4)*result_data['ff_frontal_lat_esq_total']) + ((temps['temp_teto']**4)*result_data['ff_frontal_teto_total']) + ((temps['temp_piso']**4)*result_data['ff_frontal_piso_total']))**0.25, 14),
        'posterior': round((((temps['temp_posterior']**4)*result_data['ff_posterior_total']) + ((temps['temp_lat_direita']**4)*result_data['ff_posterior_lat_dir_total']) + ((temps['temp_lat_esquerda']**4)*result_data['ff_posterior_lat_esq_total']) + ((temps['temp_teto']**4)*result_data['ff_posterior_teto_total']) + ((temps['temp_piso']**4)*result_data['ff_posterior_piso_total']))**0.25, 14)
    }

    radiant_temperatures['frontal_celsius'] = round((radiant_temperatures['frontal'] - 273.15), 14)
    radiant_temperatures['posterior_celsius'] = round((radiant_temperatures['posterior'] - 273.15), 14)
    radiant_temperatures['assimetry'] = round(abs(radiant_temperatures['frontal'] - radiant_temperatures['posterior']), 14)

    resultados_direita = f"""
---

## ESQUERDA E DIREITA

### TEMPERATURAS RADIANTES

- Esquerda: {round(radiant_temperatures['frontal_celsius'], 2)}°C
- Direita: {round(radiant_temperatures['posterior_celsius'], 2)}°C
- Assimetria: {round(radiant_temperatures['assimetry'], 2)}°C

### FATORES DE FORMA ESQUERDOS

- Lateral esquerda: {result_data['ff_frontal_total']}
- Parede frontal: {result_data['ff_frontal_lat_dir_total']}
- Parede posterior: {result_data['ff_frontal_lat_esq_total']}
- Teto: {result_data['ff_frontal_teto_total']}
- Piso: {result_data['ff_frontal_piso_total']}

### FATORES DE FORMA DIREITOS
- Lateral direita: {result_data['ff_posterior_total']}
- Parede frontal: {result_data['ff_posterior_lat_dir_total']}
- Parede posterior: {result_data['ff_posterior_lat_esq_total']}
- Teto: {result_data['ff_posterior_teto_total']}
- Piso: {result_data['ff_posterior_piso_total']}"""

    ## CÁLCULO TETO E PISO
    temps = {
    'temp_frontal': temp_teto,
    'temp_posterior': temp_piso,
    'temp_teto': temp_posterior,
    'temp_piso': temp_frontal,
    'temp_lat_direita': temp_lat_dir,
    'temp_lat_esquerda': temp_lat_esq
    }

    for key in temps:
        temps[key] += 273.15

    coordinates = {
        'dist_frontal': room['altura'] - room['pos_z'],
        'dist_posterior': room['pos_z'],
        'dist_piso': room['pos_y'],
        'dist_teto': room['comprimento'] - room['pos_y'],
        'dist_lat_direita': room['pos_x'],
        'dist_lat_esquerda': room['largura'] - room['pos_x'],
    }

    ort_ff_frontal_dict = {
        'ff_teto_dir': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_lat_direita'], c=coordinates['dist_teto']),
        'ff_teto_esq': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_lat_esquerda'], c=coordinates['dist_teto']),
        'ff_piso_dir': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_lat_direita'], c=coordinates['dist_piso']),
        'ff_piso_esq': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_lat_esquerda'], c=coordinates['dist_piso']),
        'ff_lat_dir_baixo': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_piso'], c=coordinates['dist_lat_direita']),
        'ff_lat_dir_cima': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_teto'], c=coordinates['dist_lat_direita']),
        'ff_lat_esq_baixo': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_piso'], c=coordinates['dist_lat_esquerda']),
        'ff_lat_esq_cima': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_teto'], c=coordinates['dist_lat_esquerda'])
    }

    ort_ff_posterior_dict = {
        'ff_teto_esq': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_lat_esquerda'], c=coordinates['dist_teto']),
        'ff_teto_dir': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_lat_direita'], c=coordinates['dist_teto']),
        'ff_piso_esq': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_lat_esquerda'], c=coordinates['dist_piso']),
        'ff_piso_dir': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_lat_direita'], c=coordinates['dist_piso']),
        'ff_lat_esq_baixo': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_piso'], c=coordinates['dist_lat_esquerda']),
        'ff_lat_esq_cima': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_teto'], c=coordinates['dist_lat_esquerda']),
        'ff_lat_dir_baixo': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_piso'], c=coordinates['dist_lat_direita']),
        'ff_lat_dir_cima': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_teto'], c=coordinates['dist_lat_direita'])
    }

    par_ff_dict = {
        'ff_frontal_quad_1': par_ff(b=coordinates['dist_teto'], a=coordinates['dist_lat_direita'], c=coordinates['dist_frontal']),
        'ff_frontal_quad_2': par_ff(b=coordinates['dist_teto'], a=coordinates['dist_lat_esquerda'], c=coordinates['dist_frontal']),
        'ff_frontal_quad_3': par_ff(b=coordinates['dist_piso'], a=coordinates['dist_lat_esquerda'], c=coordinates['dist_frontal']),
        'ff_frontal_quad_4': par_ff(b=coordinates['dist_piso'], a=coordinates['dist_lat_direita'], c=coordinates['dist_frontal']),
        'ff_posterior_quad_1': par_ff(b=coordinates['dist_teto'], a=coordinates['dist_lat_esquerda'], c=coordinates['dist_posterior']),
        'ff_posterior_quad_2': par_ff(b=coordinates['dist_teto'], a=coordinates['dist_lat_direita'], c=coordinates['dist_posterior']),
        'ff_posterior_quad_3': par_ff(b=coordinates['dist_piso'], a=coordinates['dist_lat_direita'], c=coordinates['dist_posterior']),
        'ff_posterior_quad_4': par_ff(b=coordinates['dist_piso'], a=coordinates['dist_lat_esquerda'], c=coordinates['dist_posterior'])
    }

    conferencia = {
        'sum_ff_frontal': round((sum(ort_ff_frontal_dict.values()) + par_ff_dict['ff_frontal_quad_1'] + par_ff_dict['ff_frontal_quad_2'] + par_ff_dict['ff_frontal_quad_3'] + par_ff_dict['ff_frontal_quad_4']), 14),
        'sum_ff_posterior': round((sum(ort_ff_posterior_dict.values()) + par_ff_dict['ff_posterior_quad_1'] + par_ff_dict['ff_posterior_quad_2'] + par_ff_dict['ff_posterior_quad_3'] + par_ff_dict['ff_posterior_quad_4']), 14)
    }

    ajuste_frontal = 0
    ajuste_posterior = 0

    if conferencia['sum_ff_frontal'] != 1:
        ajuste_frontal = conferencia['sum_ff_frontal']
        ajuste_frontal = 1 - ajuste_frontal
        ajuste_frontal = ajuste_frontal / 4

    if conferencia['sum_ff_posterior'] != 1:
        ajuste_posterior = conferencia['sum_ff_posterior']
        ajuste_posterior = 1 - ajuste_posterior
        ajuste_posterior = ajuste_posterior / 4

    result_data = {
        'ff_frontal_total': round((par_ff_dict['ff_frontal_quad_1'] + par_ff_dict['ff_frontal_quad_2'] + par_ff_dict['ff_frontal_quad_3'] + par_ff_dict['ff_frontal_quad_4']), 14),
        'ff_posterior_total': round((par_ff_dict['ff_posterior_quad_1'] + par_ff_dict['ff_posterior_quad_2'] + par_ff_dict['ff_posterior_quad_3'] + par_ff_dict['ff_posterior_quad_4']), 14),
        'ff_frontal_lat_dir_total': round(((ort_ff_frontal_dict['ff_lat_dir_baixo'] + ort_ff_frontal_dict['ff_lat_dir_cima']) + ajuste_frontal), 14),
        'ff_frontal_lat_esq_total': round(((ort_ff_frontal_dict['ff_lat_esq_baixo'] + ort_ff_frontal_dict['ff_lat_esq_cima']) + ajuste_frontal), 14),
        'ff_posterior_lat_dir_total': round(((ort_ff_posterior_dict['ff_lat_dir_baixo'] + ort_ff_posterior_dict['ff_lat_dir_cima']) + ajuste_posterior), 14),
        'ff_posterior_lat_esq_total': round(((ort_ff_posterior_dict['ff_lat_esq_baixo'] + ort_ff_posterior_dict['ff_lat_esq_cima']) + ajuste_posterior), 14),
        'ff_frontal_teto_total': round(((ort_ff_frontal_dict['ff_teto_dir'] + ort_ff_frontal_dict['ff_teto_esq']) + ajuste_frontal), 14),
        'ff_frontal_piso_total': round(((ort_ff_frontal_dict['ff_piso_dir'] + ort_ff_frontal_dict['ff_piso_esq']) + ajuste_frontal), 14),
        'ff_posterior_teto_total': round(((ort_ff_posterior_dict['ff_teto_dir'] + ort_ff_posterior_dict['ff_teto_esq']) + ajuste_posterior), 14),
        'ff_posterior_piso_total': round(((ort_ff_posterior_dict['ff_piso_dir'] + ort_ff_posterior_dict['ff_piso_esq']) + ajuste_posterior), 14)
    }

    radiant_temperatures = {
        'frontal': round((((temps['temp_frontal']**4)*result_data['ff_frontal_total']) + ((temps['temp_lat_direita']**4)*result_data['ff_frontal_lat_dir_total']) + ((temps['temp_lat_esquerda']**4)*result_data['ff_frontal_lat_esq_total']) + ((temps['temp_teto']**4)*result_data['ff_frontal_teto_total']) + ((temps['temp_piso']**4)*result_data['ff_frontal_piso_total']))**0.25, 14),
        'posterior': round((((temps['temp_posterior']**4)*result_data['ff_posterior_total']) + ((temps['temp_lat_direita']**4)*result_data['ff_posterior_lat_dir_total']) + ((temps['temp_lat_esquerda']**4)*result_data['ff_posterior_lat_esq_total']) + ((temps['temp_teto']**4)*result_data['ff_posterior_teto_total']) + ((temps['temp_piso']**4)*result_data['ff_posterior_piso_total']))**0.25, 14)
    }

    radiant_temperatures['frontal_celsius'] = round((radiant_temperatures['frontal'] - 273.15), 14)
    radiant_temperatures['posterior_celsius'] = round((radiant_temperatures['posterior'] - 273.15), 14)
    radiant_temperatures['assimetry'] = round(abs(radiant_temperatures['frontal'] - radiant_temperatures['posterior']), 14)

    resultados_teto = f"""
---

## TETO E PISO

### TEMPERATURAS RADIANTES
- Teto: {round(radiant_temperatures['frontal_celsius'], 2)}°C
- Piso: {round(radiant_temperatures['posterior_celsius'], 2)}°C
- Assimetria: {round(radiant_temperatures['assimetry'], 2)}°C

### FATORES DE FORMA TETO
- Teto: {result_data['ff_frontal_total']}
- Lateral direita: {result_data['ff_frontal_lat_dir_total']}
- Lateral esquerda: {result_data['ff_frontal_lat_esq_total']}
- Parede posterior: {result_data['ff_frontal_teto_total']}
- Parede frontal: {result_data['ff_frontal_piso_total']}

### FATORES DE FORMA PISO
- Piso: {result_data['ff_posterior_total']}
- Lateral direita: {result_data['ff_posterior_lat_dir_total']}
- Lateral esquerda: {result_data['ff_posterior_lat_esq_total']}
- Parede posterior: {result_data['ff_posterior_teto_total']}
- Parede frontal: {result_data['ff_posterior_piso_total']}
"""

    resultados =  resultados_frontal + resultados_direita + resultados_teto + inputs
    return resultados