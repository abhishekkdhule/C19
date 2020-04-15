from django.shortcuts import render
import pandas as pd


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
first=pd.read_json("https://api.rootnet.in/covid19-in/unofficial/covid19india.org/statewise")
# print(first.head())
# print(first['data'])
# print(first.iloc[3,1])
# total=first.iloc[3,1]
# state=first.iloc[2,1]
# print(state)

def homepage_view(request):
    first=pd.read_json("https://api.rootnet.in/covid19-in/unofficial/covid19india.org/statewise")
    print(first.head())
    # print(first['data'])
    # print(first.iloc[3,1])
    total=first.iloc[3,1]
    state=first.iloc[2,1]
    # print(state)
    context={
        'total':total,
        'delhi':state[1],
        'state_data':state,
    }
    return render(request,'homepage/homepage.html',context)
