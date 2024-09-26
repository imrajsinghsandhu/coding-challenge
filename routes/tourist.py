from flask import Flask, request, jsonify

app = Flask(__name__)

def find_best_path(locations, starting_point, time_limit, travel_times):
    # Helper function to calculate satisfaction and time spent
    def dfs(current_station, remaining_time, current_satisfaction, visited_stations):
        if remaining_time < 0:
            return 0, []
        
        # If the station path loops back to the starting point, return satisfaction gained
        if current_station == starting_point and visited_stations:
            return current_satisfaction, visited_stations
        
        best_satisfaction = current_satisfaction
        best_path = visited_stations[:]
        
        for station, (satisfaction, visit_time) in locations.items():
            if station not in visited_stations:
                # Calculate travel time to the next station
                travel_time = travel_times.get((current_station, station), float('inf'))
                # Check if visiting this station is possible within the remaining time
                total_time_spent = travel_time + visit_time
                if remaining_time - total_time_spent >= 0:
                    new_satisfaction, new_path = dfs(
                        station, remaining_time - total_time_spent, 
                        current_satisfaction + satisfaction, 
                        visited_stations + [station]
                    )
                    if new_satisfaction > best_satisfaction:
                        best_satisfaction = new_satisfaction
                        best_path = new_path
        
        return best_satisfaction, best_path

    # Initialize DFS from the starting point
    satisfaction, path = dfs(starting_point, time_limit, 0, [starting_point])
    
    # Return to the starting point
    return {'path': path + [starting_point], 'satisfaction': satisfaction}

@app.route('/tourist', methods=['POST'])
def tourist():
    data = request.json
    locations = data['locations']
    starting_point = data['startingPoint']
    time_limit = data['timeLimit']
    travel_times = data.get('travelTimes', {})
    
    result = find_best_path(locations, starting_point, time_limit, travel_times)
    
    return jsonify(result)