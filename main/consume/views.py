from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.
def users(request):
    #pull data from third party rest api
#    response = requests.get('https://jsonplaceholder.typicode.com/users')
    url = 'https://www.recreation.gov/api/permits/234622/divisions/376/availability?start_date=2022-06-21T06:00:00.000Z&end_date=2022-12-31T00:00:00.000Z&commercial_acct=false&is_lottery=false'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get(url, headers=headers)

    #convert reponse data into json
    users = response.json()
    #print(users)
    return render(request, "users.html", {"users":users})
    pass