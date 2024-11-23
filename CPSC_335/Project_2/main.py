import googlemaps

#API Key
gmaps = googlemaps.Client(key='AIzaSyAXFY9pVrVpcHNN3NZbBFdeW9hx38ON0wY')


#Calculate Routes Between
# Starting and destination locations
start_location = "New York, NY"
end_location = "Boston, MA"

# Request directions
directions_result = gmaps.directions(start_location,
                                     end_location,
                                     mode="walking")  # modes include 'walking', 'bicycling', 'transit'

# Display the directions steps
for step in directions_result[0]['legs'][0]['steps']:
    print(step['html_instructions'])
