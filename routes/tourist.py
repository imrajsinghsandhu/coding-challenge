from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Constants for travel times between stations (time in minutes)
travel_times_per_line = {
    "Tokyo Metro Ginza Line": 2,
    "Tokyo Metro Marunouchi Line": 3,
    "Tokyo Metro Hibiya Line": 2.5,
    "Tokyo Metro Tozai Line": 4,
    "Tokyo Metro Chiyoda Line": 1.5,
    "Tokyo Metro Yurakucho Line": 2,
    "Tokyo Metro Hanzomon Line": 2,
    "Tokyo Metro Namboku Line": 1,
    "Tokyo Metro Fukutoshin Line": 3,
    "Toei Asakusa Line": 3.5,
    "Toei Mita Line": 4,
    "Toei Shinjuku Line": 1.5,
    "Toei Oedo Line": 1
}

# Subway stations map for each line
subway_stations = {
    "Tokyo Metro Ginza Line": [
        "Asakusa", "Tawaramachi", "Inaricho", "Ueno", "Ueno-hirokoji", "Suehirocho",
        "Kanda", "Mitsukoshimae", "Nihombashi", "Kyobashi", "Ginza", "Shimbashi",
        "Toranomon", "Tameike-sanno", "Akasaka-mitsuke", "Nagatacho", "Aoyama-itchome",
        "Gaiemmae", "Omotesando", "Shibuya"
    ],
    "Tokyo Metro Marunouchi Line": [
        "Ogikubo", "Minami-asagaya", "Shin-koenji", "Higashi-koenji", "Shin-nakano",
        "Nakano-sakaue", "Nishi-shinjuku", "Shinjuku", "Shinjuku-sanchome", "Shin-ochanomizu",
        "Ochanomizu", "Awajicho", "Otemachi", "Tokyo", "Ginza", "Kasumigaseki", "Kokkai-gijidomae",
        "Akasaka-mitsuke", "Yotsuya", "Yotsuya-sanchome", "Shinjuku-gyoemmae", "Nishi-shinjuku-gochome",
        "Nakano-fujimicho", "Nakano-shimbashi", "Nakano-sakaue", "Shinjuku-sanchome", "Kokkai-gijidomae",
        "Kasumigaseki", "Ginza", "Tokyo", "Otemachi", "Awajicho", "Shin-ochanomizu", "Ochanomizu"
    ],
    # Add the rest of the lines
}

# Helper function to calculate the total travel time between two stations
def calculate_travel_time(path, travel_times_per_line):
    total_travel_time = 0
    for i in range(len(path) - 1):
        for line, stations in subway_stations.items():
            if path[i] in stations and path[i+1] in stations:
                total_travel_time += travel_times_per_line[line]
                break
    return total_travel_time

# Helper function to calculate the total time for a given path
def calculate_total_time(path, station_times, travel_times_per_line):
    travel_time = calculate_travel_time(path, travel_times_per_line)
    visit_time = sum([station_times[station][1] for station in path])
    return travel_time + visit_time

# Helper function to calculate the total satisfaction for a given path
def calculate_total_satisfaction(path, station_times):
    return sum([station_times[station][0] for station in path])

# Backtracking function to find the optimal path
def find_optimal_path(current_station, stations, station_times, travel_times_per_line, time_limit, current_path, best_path, best_satisfaction):
    if calculate_total_time(current_path, station_times, travel_times_per_line) > time_limit:
        return best_path, best_satisfaction

    current_satisfaction = calculate_total_satisfaction(current_path, station_times)
    if current_satisfaction > best_satisfaction:
        best_path = list(current_path)
        best_satisfaction = current_satisfaction

    for next_station in stations:
        if next_station not in current_path:
            current_path.append(next_station)
            best_path, best_satisfaction = find_optimal_path(
                next_station, stations, station_times, travel_times_per_line, time_limit, current_path, best_path, best_satisfaction
            )
            current_path.pop()

    return best_path, best_satisfaction

# POST endpoint to calculate the optimal tourist route
@app.route('/tourist', methods=['POST'])
def tourist():
    logging.info(data)
    data = request.json
    station_times = data['station_times']  # dict of stations with (satisfaction, min_time)
    start_station = data['start_station']  # starting and ending station
    time_limit = data['time_limit']  # time limit in minutes

    # List of all stations excluding the start station (which must be visited first and last)
    stations = list(station_times.keys())
    stations.remove(start_station)

    # Find the best path starting and ending at the start_station
    best_path, best_satisfaction = find_optimal_path(
        start_station, stations, station_times, travel_times_per_line, time_limit, [start_station], [], 0
    )

    # Add the start station at the end to complete the loop
    best_path.append(start_station)

    return jsonify({"path": best_path, "satisfaction": best_satisfaction})

if __name__ == '__main__':
    app.run(debug=True)
