import ssl; ssl._create_default_https_context = ssl._create_stdlib_context
from django.shortcuts import render
from django.template.defaulttags import register
import pandas as pd
import json 

from bokeh.plotting import figure, output_file, show
from bokeh.embed import components


@register.filter
def get_range(value):
    return range(value)


def home(request):
    url = 'https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/diabetes.csv'
    diabetes = pd.read_csv(url)
    json_records = diabetes.reset_index().to_json(orient ='records') 
    data = json.loads(json_records)
    context = {
        'data_name': 'Diabetes Data',
        'data' : data,
        'columns': ['index']+list(diabetes.columns),
        'rows': diabetes.shape[0],
        'cols': diabetes.shape[1]
    }
    return render(request, 'app/home.html', context)

def about(request):
    return render(request, 'app/about.html')

def plots(request):
    p = figure(plot_width=400, plot_height=400, title="My Line Plot")
    p.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2)
    script, div = components(p)
    return render(request, 'app/plots.html', {'script': script, 'div': div})