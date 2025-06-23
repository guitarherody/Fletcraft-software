# -*- coding: utf-8 -*-
import requests
import json

# Service prices
service_prices = {
    "Custom Software Development": "450.00",
    "Web Applications": "350.00", 
    "Mobile Development": "400.00",
    "AI & Machine Learning": "500.00",
    "Cloud Solutions": "300.00",
    "Cybersecurity": "250.00"
}

# Get all services
response = requests.get('https://fletcraft-software.onrender.com/api/services/')
services = response.json()['results']

print("Updating service prices...")

for service in services:
    service_title = service['title']
    if service_title in service_prices:
        new_price = service_prices[service_title]
        
        # Update the service
        update_data = {
            'title': service['title'],
            'description': service['description'],
            'icon': service['icon'],
            'price': new_price
        }
        
        url = "https://fletcraft-software.onrender.com/api/services/" + str(service['id']) + "/"
        update_response = requests.put(
            url,
            json=update_data,
            headers={'Content-Type': 'application/json'}
        )
        
        if update_response.status_code == 200:
            print("Updated " + service_title + ": R" + new_price)
        else:
            print("Failed to update " + service_title + ": " + str(update_response.status_code))

print("All services updated! Prices should now show on the front page.") 