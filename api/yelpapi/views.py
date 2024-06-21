from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json
import sqlite3

Holiday_API_KEY="e276e028-8307-40dd-9047-f8d8bfbff530"
holiday_end_point=f'https://holidayapi.com/v1/holidays?key={Holiday_API_KEY}&country=US&year=2023'



@csrf_exempt
def home(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        business = data.get('business')
        location = data.get('location')
        date= data.get('date')




        




 
        yelp_endpoint = f'https://api.yelp.com/v3/businesses/search?location={location}&term={business}'
        print(yelp_endpoint)
        headers = {
            'Authorization': 'Bearer kNIRAZWPcyNLjG6XojNCSBZk1J6qZCAeA-4-jzBlpYKdVFUjydm5SVGFqVuTPSfkkYlidORZkcPVa8axsbM2ErZzQ9buHHlzgn4Q2viHQ4dcYPJqOKIaRHJFKRJzZnYx',
            'Content-Type': 'application/json'
        }
        response = requests.get(yelp_endpoint, headers=headers)
        response_dictionary = response.json()
        business_details = []

        # holiday_end_point=f'https://holidayapi.com/v1/holidays?key={Holiday_API_KEY}&country=US'
        # response=requests.get(holiday_end_point)
        # response_dictionary=response.json()
        # holidays=response_dictionary.get("holidays") 
        # print(holidays)
        # selected_holiday=""
        # for h in holidays:
        #     temp_date=h.get("date")
        #     if temp_date == date:
        #         selected_holiday=h.get('name')
        #         break
        #     else:
        #         selected_holiday=""

        for business in response_dictionary.get('businesses', []):
            id = business['id']
            name = business['name']
            distance = business['distance']
            address = business ['location'].get('display_address')
         


            print(address)
            if name == "Costco Wholesale":
                business_detail = [id, name, distance, address]
                business_details.append(business_detail)
                # else:
                #     business_detail = [id, name, distance, address,selected_holiday,"Open"]
                #     business_details.append(business_detail)



        # Sorting the business details by distance in ascending order
        sorted_business_details = sorted(business_details, key=lambda x: x[2])

        # print(sorted_business_details)

        return JsonResponse(sorted_business_details[0][3], safe=False)

    return HttpResponse("respond to your request for the server")



@csrf_exempt
def Holiday (request):
    if request.method == 'POST':
        data=json.loads(request.body)
        date=data.get('date')
        response=requests.get(holiday_end_point)
        return JsonResponse(response.json(),safe=False)
    
    
    return HttpResponse("respond to your request for the server")


@csrf_exempt
def DataBase (request):
    if request.method == 'POST':
        connection = sqlite3.connect("C:\\Users\\m21ne\Downloads\\backEndProjects\\db.sqlite3")
        cursor=connection.cursor()
        list_of_holidays_query= '''SELECT DISTINCT HOLIDAYNAME FROM HOLIDAY;'''
        cursor.execute(list_of_holidays_query)
        holiday_tuple_list=cursor.fetchall()
        holiday_list= list()
        for h in holiday_tuple_list:
            holiday_list.append(h[0])

        placeholders = ','.join('?' for _ in holiday_list)
        holiday_check_query = f'SELECT HOLIDAYNAME FROM HOLIDAY WHERE HOLIDAYNAME IN ()'.format(placeholders)
        cursor.execute(holiday_check_query,holiday_list)
        
        print(f'Holiday List: {holiday_list}')

        # holiday_check_query = "SELECT HOLYDAYNAME FROM HOLIDAY WHERE HOLYDAYNAME IN ({?,?,?}) "
        # data=json.loads(request.body)
        # holidays=data.get('holidays')
        # for holiday in holidays:
        #     if holiday 
        response=requests.get(holiday_end_point)
        return JsonResponse(response.json(),safe=False)
    
    
    return HttpResponse("respond to your request for the server")




