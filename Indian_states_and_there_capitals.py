import json

indian_states = {
    "Telangana": "Hyderabad",
    "Karnataka": "Banglore",
    "Maharastra": "Mumbai",
    "West Bengal": "Kolkata",
    "Tamil Nadu": "Chennai",
    "Rajasthan": "Jaipur",
    "Uttarakhand": "Dehradun",
}

file=open('C:\\Users\\chint\\practise\\Assignment2.py\\Assignment3.py\\Assignment_6\\test.json','w')
data=json.dump(indian_states,file)
