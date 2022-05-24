'''
Merve Atay 24.05.2022

API Homework
https://api.nasa.gov adresindeki datalardan;
1- NeoWs (Near Earth Object Web Service) is a RESTful web service for near earth Asteroid information. 
With NeoWs a user can: search for Asteroids based on their closest approach date to Earth, 
lookup a specific Asteroid with its NASA JPL small body id, as well as browse the overall data-set.
1 temmuz 2016 ile 30 temmuz 2016 tarihleri arasinda,
dunyaya potansiyel tehlike olusturan astroid datasini alarak astorid.csv dosyasina kaydediniz.'''

import requests
import csv

url= 'https://api.nasa.gov/neo/rest/v1/feed'
datas=[]

start_dates= ['2016-07-01','2016-07-09','2016-07-17', '2016-07-25']
end_dates= ['2016-07-08','2016-07-16','2016-07-24','2016-07-30']

for x in range(4):
    
    response = requests.get(url, params= {
        'api_key' : '2ijwiUacOxzK2mYabhvNHw8lRSV0nJAv64lGqaGH',
        'start_date' : start_dates[x],
        'end_date' : end_dates[x]
        })
    
    data= response.json()['near_earth_objects']
    
    for i in range(len(data.keys())):

        data_list= list(data.values())[i]
    
        for j in data_list:
            if j['is_potentially_hazardous_asteroid'] == True :
                datas.append(j)
    #print(datas)

with open('astorid.csv' , 'a') as f:
    fields=['links','id','neo_reference_id','name','nasa_jpl_url','absolute_magnitude_h','estimated_diameter','is_potentially_hazardous_asteroid','close_approach_data','is_sentry_object']
    
    writer = csv.DictWriter(f,fieldnames= fields)
    writer.writeheader()
    writer.writerows(datas)
    
f.close()

