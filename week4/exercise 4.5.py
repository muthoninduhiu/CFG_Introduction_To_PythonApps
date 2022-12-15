"""
Exercise 4.5: Print the values of name , post_code and street_number from the dictionary

Extension: Print the values of longitude and latitude from the inner dictionary
"""
place = {
    'name': 'The Anchor',
    'post_code': 'E14 6HY',
    'street_number': '54',
    'location': {
        'longitude': 127,
        'latitude': 63,
    }
}
print("Name: {}".format(place['name']))
print("Postal Code: {}".format(place['post_code']))
print("Street Number: {}".format(place['street_number']))
print("Longitude: {}".format(place['location']['longitude']))
print("Latitude: {}".format(place['location']['latitude']))
