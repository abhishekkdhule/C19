from django.shortcuts import render
import pandas as pd

df=pd.read_json("https://covid19.mathdro.id/api/countries/India")
# print(df.head(1))
# print(df[['confirmed','recovered','deaths','lastUpdate']])
# print(df.dtypes)
#https://www.freecodecamp.org/news/how-to-make-your-first-javascript-chart/
# confirmed=df['confirmed'].head(1)
# recovery=df['recovered'].head(1)
# death=df['deaths'].head(1)
# print()
# print("total no. of cases = ",confirmed.value)
# print("total no. of recovery = ",recovery.value)
# print("total no. of deaths = ",death.value)
# Create your views here.
def homepage_view(request):
    df=pd.read_json("https://covid19.mathdro.id/api/countries/India")
    confirmed=df['confirmed'].head(1)
    recovery=df['recovered'].head(1)
    death=df['deaths'].head(1)
    context={
        'confirmed':confirmed.value,
        'recovery':recovery.value,
        'deaths':death.value,
    }
    return render(request,'homepage/homepage.html',context)