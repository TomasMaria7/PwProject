import requests
from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse




# URLs da API do IPMA para obter os dados meteorológicos e avisos
URL_API_IPMA = 'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily'
URL_TIPOS_CLIMA_IPMA = 'https://api.ipma.pt/open-data/weather-type-classe.json'

# Função para obter os dados meteorológicos da API
def obter_dados_meteorologicos(cidade_id):
    resposta = requests.get(f"{URL_API_IPMA}/{cidade_id}.json")
    return resposta.json() if resposta.status_code == 200 else None

# Função para obter as descrições dos tipos de clima
def obter_tipos_clima():
    resposta = requests.get(URL_TIPOS_CLIMA_IPMA)
    return resposta.json() if resposta.status_code == 200 else None

def pagina_api(request):
    return render(request, 'meteo/api.html')

def pagina_inicial(request):
    mapa_cidades_id = {
        '1010500': 'Aveiro',
        '1020500': 'Beja',
        '1030300': 'Braga',
        '1030800': 'Guimarães',
        '1040200': 'Bragança',
        '1050200': 'Castelo Branco',
        '1060300': 'Coimbra',
        '1070500': 'Évora',
        '1080500': 'Faro',
        '1080800': 'Loulé',
        '1081100': 'Portimão',
        '1081505': 'Sagres',
        '1090700': 'Guarda',
        '1090821': 'Penhas Douradas',
        '1100900': 'Leiria',
        '1110600': 'Lisboa',
        '1121400': 'Portalegre',
        '1131200': 'Porto',
        '1141600': 'Santarém',
        '1151200': 'Setúbal',
        '1151300': 'Sines',
        '1160900': 'Viana do Castelo',
        '1171400': 'Vila Real',
        '1182300': 'Viseu',
        '2310300': 'Funchal',
        '2320100': 'Porto Santo',
        '3410100': 'Vila do Porto',
        '3420300': 'Ponta Delgada',
        '3430100': 'Angra do Heroísmo',
        '3440100': 'Santa Cruz da Graciosa',
        '3450200': 'Velas',
        '3460200': 'Madalena',
        '3470100': 'Horta',
        '3480200': 'Santa Cruz das Flores',
        '3490100': 'Vila do Corvo',
    }

    contexto = {
        'mapa_cidades_id': mapa_cidades_id,
    }
    return render(request, 'meteo/pagina_inicial.html', contexto)

def tempo_5_dias(request, cidade_id):
    mapa_cidades_id = {
        '1010500': 'Aveiro',
        '1020500': 'Beja',
        '1030300': 'Braga',
        '1030800': 'Guimarães',
        '1040200': 'Bragança',
        '1050200': 'Castelo Branco',
        '1060300': 'Coimbra',
        '1070500': 'Évora',
        '1080500': 'Faro',
        '1080800': 'Loulé',
        '1081100': 'Portimão',
        '1081505': 'Sagres',
        '1090700': 'Guarda',
        '1090821': 'Penhas Douradas',
        '1100900': 'Leiria',
        '1110600': 'Lisboa',
        '1121400': 'Portalegre',
        '1131200': 'Porto',
        '1141600': 'Santarém',
        '1151200': 'Setúbal',
        '1151300': 'Sines',
        '1160900': 'Viana do Castelo',
        '1171400': 'Vila Real',
        '1182300': 'Viseu',
        '2310300': 'Funchal',
        '2320100': 'Porto Santo',
        '3410100': 'Vila do Porto',
        '3420300': 'Ponta Delgada',
        '3430100': 'Angra do Heroísmo',
        '3440100': 'Santa Cruz da Graciosa',
        '3450200': 'Velas',
        '3460200': 'Madalena',
        '3470100': 'Horta',
        '3480200': 'Santa Cruz das Flores',
        '3490100': 'Vila do Corvo',
    }

    dados_meteorologicos = obter_dados_meteorologicos(cidade_id)
    tipos_clima = obter_tipos_clima()
    nome_cidade = mapa_cidades_id.get(cidade_id, 'Desconhecido')

    if dados_meteorologicos and tipos_clima:
        previsoes = dados_meteorologicos['data'][:5]
        lista_previsoes = []
        for previsao in previsoes:
            tipo_clima = next((item for item in tipos_clima['data'] if item['idWeatherType'] == previsao['idWeatherType']), None)
            if previsao['idWeatherType'] < 10:
                icone_clima = f"/static/meteo/w_ic_d_0{previsao['idWeatherType']}anim.svg"
            else:
                icone_clima = f"/static/meteo/w_ic_d_{previsao['idWeatherType']}anim.svg"
            lista_previsoes.append({
                'data': datetime.strptime(previsao['forecastDate'], '%Y-%m-%d').strftime('%d-%m-%Y'),
                'temp_min': previsao['tMin'],
                'temp_max': previsao['tMax'],
                'descricao_clima': tipo_clima['descWeatherTypePT'] if tipo_clima else 'Descrição não disponível',
                'icone_clima': icone_clima
            })

        contexto = {
            'nome_cidade': nome_cidade,
            'lista_previsoes': lista_previsoes,
        }
        return render(request, 'meteo/tempo_5_dias.html', contexto)
    else:
        return render(request, 'meteo/erro.html')



def lista_de_cidades(request):
    cidades = {
        '1010500': 'Aveiro',
        '1020500': 'Beja',
        '1030300': 'Braga',
        '1030800': 'Guimarães',
        '1040200': 'Bragança',
        '1050200': 'Castelo Branco',
        '1060300': 'Coimbra',
        '1070500': 'Évora',
        '1080500': 'Faro',
        '1080800': 'Loulé',
        '1081100': 'Portimão',
        '1081505': 'Sagres',
        '1090700': 'Guarda',
        '1090821': 'Penhas Douradas',
        '1100900': 'Leiria',
        '1110600': 'Lisboa',
        '1121400': 'Portalegre',
        '1131200': 'Porto',
        '1141600': 'Santarém',
        '1151200': 'Setúbal',
        '1151300': 'Sines',
        '1160900': 'Viana do Castelo',
        '1171400': 'Vila Real',
        '1182300': 'Viseu',
        '2310300': 'Funchal',
        '2320100': 'Porto Santo',
        '3410100': 'Vila do Porto',
        '3420300': 'Ponta Delgada',
        '3430100': 'Angra do Heroísmo',
        '3440100': 'Santa Cruz da Graciosa',
        '3450200': 'Velas',
        '3460200': 'Madalena',
        '3470100': 'Horta',
        '3480200': 'Santa Cruz das Flores',
        '3490100': 'Vila do Corvo',
    }
    return JsonResponse({'cidades': cidades})

def previsao_hoje(request, cidade_id):
    resposta = requests.get(f'{URL_API_IPMA}/{cidade_id}.json')
    if resposta.status_code == 200:
        dados = resposta.json()
        previsao_hoje = dados['data'][0]
        resposta_formatada = {
            'data': previsao_hoje['forecastDate'],
            'temp_min': previsao_hoje['tMin'],
            'temp_max': previsao_hoje['tMax'],
            'descricao_clima': previsao_hoje['predWindDir'],
            'precipitacao': previsao_hoje['precipitaProb'],
            'icone_clima': f"http://api.ipma.pt/open-data/weather-type-classe.json?dia={previsao_hoje['idWeatherType']}"
        }
        return JsonResponse(resposta_formatada)
    else:
        return JsonResponse({'error': 'Erro ao obter a previsão do tempo do IPMA'}, status=500)

def previsao_proximos_5_dias(request, cidade_id):
    resposta = requests.get(f'{URL_API_IPMA}/{cidade_id}.json')
    if resposta.status_code == 200:
        dados = resposta.json()
        previsoes = dados['data'][:5]
        resposta_formatada = {
            'previsoes': []
        }
        for previsao in previsoes:
            previsao_formatada = {
                'data': previsao['forecastDate'],
                'temp_min': previsao['tMin'],
                'temp_max': previsao['tMax'],
                'descricao_clima': previsao['predWindDir'],
                'precipitacao': previsao['precipitaProb'],
                'icone_clima': f"http://api.ipma.pt/open-data/weather-type-classe.json?dia={previsao['idWeatherType']}"
            }
            resposta_formatada['previsoes'].append(previsao_formatada)
        return JsonResponse(resposta_formatada)
    else:
        return JsonResponse({'error': 'Erro ao obter a previsão do tempo do IPMA'}, status=500)
