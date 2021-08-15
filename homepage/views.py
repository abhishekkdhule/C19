from django.shortcuts import render
import pandas as pd

first=pd.read_json("https://api.rootnet.in/covid19-in/unofficial/covid19india.org/statewise")

def homepage_view(request):
    first=pd.read_json("https://api.rootnet.in/covid19-in/unofficial/covid19india.org/statewise")
    print(first.head())
    total=first.iloc[3,1]
    state=first.iloc[2,1]
    context={
        'total':total,
        'delhi':state[1],
        'state_data':state,
    }
    return render(request,'homepage/homepage.html',context)
