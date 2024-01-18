from django.shortcuts import render
from .models import *
import requests
import json
import re
import datetime
import pandas as pd
import html
# Create your views here.
def homeView(request):
    mainPage = MainPage.objects.all().first()
    return render(request, 'home.html', {'mainPage': mainPage})

def geographyView(request):
    page = GeographyPage.objects.all().first()
    table_first = pd.read_csv(page.table_first).to_json(orient='records')
    data_first = json.loads(table_first)

    table_second = pd.read_csv(page.table_second).to_json(orient='records')
    data_second = json.loads(table_second)

    table_third = pd.read_csv(page.table_third).to_json(orient='records')
    data_third = json.loads(table_third)

    table_fourth = pd.read_csv(page.table_fourth).to_json(orient='records')
    data_fourth = json.loads(table_fourth)

    context = {
        'page': page,
        'data_first': data_first,
        'data_second': data_second,
        'data_third': data_third,
        'data_fourth': data_fourth
    }

    return render(request, 'geography.html', context=context)

def demandView(request):
    page = DemandPage.objects.all().first()
    table_all = pd.read_csv(page.table_all).to_json(orient='records')
    data_all = json.loads(table_all)

    table_vac = pd.read_csv(page.table_vac).to_json(orient='records')
    data_vac = json.loads(table_vac)

    context = {
        'page': page,
        'data_all': data_all,
        'data_vac': data_vac
    }

    return render(request, 'demand.html', context=context)

def skillsView(request):
    page = SkillsPage.objects.all().first()
    table_O_1_json = pd.read_csv(page.table_0_1).to_json(orient='records')
    table_0_1 = json.loads(table_O_1_json)

    table_1_1_json = pd.read_csv(page.table_1_1).to_json(orient='records')
    table_1_1 = json.loads(table_1_1_json)

    context = {
        'page': page,
        'table_0_1': table_0_1,
        'table_1_1': table_1_1
    }

    return render(request, 'skills.html', context=context)


def last_vacanciesView(request):
    models_list = [',', 'j', 'j']
    return render(request, 'lact_vacancies.html', {'vacs': models_list})

def clean_string(s):
    s = str(s)
    s = re.sub(r'<.*?>', '', s)
    s = s.replace("\r\n", ", ")
    s = s.replace("\n", ", ")
    s = " ".join(s.split())
    s = html.unescape(s)
    return s

def get_last_vacancies():
    currency = {
        "AZN": "Манаты",
        "BYR": "Белорусские рубли",
        "EUR": "Евро",
        "GEL": "Грузинский лари",
        "KGS": "Киргизский сом",
        "KZT": "Тенге",
        "RUR": "Рубли",
        "UAH": "Гривны",
        "USD": "Доллары",
        "UZS": "Узбекский сум"
    }

    day_ago = (datetime.datetime.now() - datetime.timedelta(days=1)).isoformat()
    url ='https://api.hh.ru/vacancies'
    params = {
        'text': 'NAME:(ux OR ui)',
        'date_from': f'{day_ago}'
    }
    response = requests.get(url, params=params)
    hh_dict = json.loads(response.content)
    vacancies_list = hh_dict['items']
    res_list = []
    for vacancy in vacancies_list:
        vacancy_info = {}
        vacancy_info['name'] = vacancy['name']
        id = vacancy['id']
        vac_response = requests.get(f'https://api.hh.ru/vacancies/{id}')
        vac_response.close()
        vac_dict = json.loads(vac_response.content)

        vacancy_info['description'] = clean_string(vac_dict['description'])

        key_skills = vac_dict['key_skills']
        if key_skills:
            key_skills_list = ', '.join([x['name'] for x in key_skills])
        else:
            key_skills_list = 'Не указано'
        vacancy_info['key_skills'] = key_skills_list
        vacancy_info['company'] = vacancy['employer']['name']

        salary = vacancy['salary']
        if salary:
            if salary['from'] and salary['to']:
                formatted_salary = f'{salary["from"]}-{salary["to"]} ({currency[salary["currency"]]})'
            elif salary['from']:
                formatted_salary = f'{salary["from"]} ({currency[salary["currency"]]})'
            else:
                formatted_salary = f'{salary["to"]} ({currency[salary["currency"]]})'
        else:
            formatted_salary = 'Не указано'
        vacancy_info['salary'] = formatted_salary
        vacancy_info['area'] = vacancy['area']['name']

        published_at = vacancy['published_at'][:-8]
        year, month, day = published_at[:10].split('-')
        hours, minutes = published_at[11:].split(':')
        published_at_formatted = f'{day}.{month}.{year} {hours}:{minutes}'
        vacancy_info['published_at'] = published_at_formatted
        res_list.append(vacancy_info)
    sorted_list = sorted(res_list, key=lambda k: k['published_at'], reverse=True)
    if len(sorted_list) > 10:
        sorted_list = sorted_list[:10]
    return json.dumps(sorted_list)

def latest_vacancies_view(request):
    l = get_last_vacancies()
    l = json.loads(l)
    context = {'data': l}
    return render(request, 'lact_vacancies.html', context)