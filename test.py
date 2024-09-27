import heapq

SUBWAY_TRAVEL_TIMES = {
    "Tokyo Metro Ginza Line": 2,
    "Tokyo Metro Marunouchi Line": 3,
    "Tokyo Metro Hibiya Line": 2.5,
    "Tokyo Metro Tozai Line": 4,
    "Tokyo Metro Chiyoda Line": 1.5,
    "Tokyo Metro Yurakucho Line": 2,
    "Tokyo Metro Hanzomon Line": 2,
    "Tokyo Metro Namboku Line" : 1,
    "Tokyo Metro Fukutoshin Line": 3,
    "Toei Asakusa Line": 3.5,
    "Toei Mita Line": 4,
    "Toei Shinjuku Line": 1.5,
    "Toei Oedo Line": 1
}

SUBWAY_LINES = {
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
    "Tokyo Metro Hibiya Line": [
        "Naka-meguro", "Ebisu", "Hiroo", "Roppongi", "Kamiyacho", "Kasumigaseki", "Hibiya",
        "Ginza", "Higashi-ginza", "Tsukiji", "Hatchobori", "Kayabacho", "Nihombashi",
        "Kodemmacho", "Akihabara", "Naka-okachimachi", "Ueno", "Iriya", "Minowa",
        "Minami-senju", "Kita-senju"
    ],
    "Tokyo Metro Tozai Line": [
        "Nakano", "Ochiai", "Takadanobaba", "Waseda", "Kagurazaka", "Iidabashi", "Kudanshita",
        "Takebashi", "Otemachi", "Nihombashi", "Kayabacho", "Monzen-nakacho", "Kiba",
        "Toyosu", "Minami-sunamachi", "Nishi-kasai", "Kasai", "Urayasu", "Minami-gyotoku",
        "Gyotoku", "Myoden", "Baraki-nakayama", "Nishi-funabashi"
    ],
    "Tokyo Metro Chiyoda Line": [
        "Yoyogi-uehara", "Yoyogi-koen", "Meiji-jingumae", "Omotesando", "Nogizaka", "Akasaka",
        "Kokkai-gijidomae", "Kasumigaseki", "Hibiya", "Nijubashimae", "Otemachi",
        "Shin-ochanomizu", "Yushima", "Nezu", "Sendagi", "Nishi-nippori", "Machiya",
        "Kita-senju", "Ayase", "Kita-ayase"
    ],
    "Tokyo Metro Yurakucho Line": [
        "Wakoshi", "Chikatetsu-narimasu", "Chikatetsu-akatsuka", "Heiwadai", "Hikawadai",
        "Kotake-mukaihara", "Senkawa", "Kanamecho", "Ikebukuro", "Higashi-ikebukuro",
        "Gokokuji", "Edogawabashi", "Iidabashi", "Ichigaya", "Kojimachi", "Nagatacho",
        "Sakuradamon", "Yurakucho", "Ginza-itchome", "Shintomicho", "Toyocho",
        "Kiba", "Toyosu", "Tsukishima", "Shintomicho", "Tatsumi", "Shinonome", "Ariake",
        "Toyosu", "Toyosu"
    ],
    "Tokyo Metro Hanzomon Line": [
        "Shibuya", "Omotesando", "Aoyama-itchome", "Nagatacho", "Hanzomon", "Kudanshita",
        "Jimbocho", "Otemachi", "Mitsukoshimae", "Suitengumae", "Kiyosumi-shirakawa",
        "Sumiyoshi", "Kinshicho", "Oshiage"
    ],
    "Tokyo Metro Namboku Line": [
        "Meguro", "Shirokanedai", "Shirokane-takanawa", "Azabu-juban", "Roppongi-itchome",
        "Tameike-sanno", "Nagatacho", "Yotsuya", "Ichigaya", "Iidabashi", "Korakuen",
        "Todaimae", "Hon-komagome", "Komagome", "Nishigahara", "Oji", "Oji-kamiya",
        "Shimo", "Akabane-iwabuchi"
    ],
    "Tokyo Metro Fukutoshin Line": [
        "Wakoshi", "Chikatetsu-narimasu", "Chikatetsu-akatsuka", "Narimasu", "Shimo-akatsuka",
        "Heiwadai", "Hikawadai", "Kotake-mukaihara", "Senkawa", "Kanamecho", "Ikebukuro",
        "Zoshigaya", "Nishi-waseda", "Higashi-shinjuku", "Shinjuku-sanchome", "Kita-sando",
        "Meiji-jingumae", "Shibuya"
    ],
    "Toei Asakusa Line": [
        "Nishi-magome", "Magome", "Nakanobu", "Togoshi", "Gotanda", "Takanawadai",
        "Sengakuji", "Mita", "Shiba-koen", "Daimon", "Shimbashi", "Higashi-ginza",
        "Takaracho", "Nihombashi", "Ningyocho", "Higashi-nihombashi", "Asakusabashi",
        "Kuramae", "Asakusa", "Honjo-azumabashi", "Oshiage"
    ],
    "Toei Mita Line": [
        "Meguro", "Shirokanedai", "Shirokane-takanawa", "Mita", "Shiba-koen", "Onarimon",
        "Uchisaiwaicho", "Hibiya", "Otemachi", "Jimbocho", "Suidobashi", "Kasuga",
        "Hakusan", "Sengoku", "Sugamo", "Nishi-sugamo", "Shin-itabashi", "Itabashi-kuyakushomae",
        "Itabashi-honcho", "Motohasunuma", "Shin-takashimadaira", "Nishidai", "Hasune",
        "Takashimadaira", "Shimura-sakaue", "Shimura-sanchome", "Nishidai"
    ],
    "Toei Shinjuku Line": [
        "Shinjuku", "Shinjuku-sanchome", "Akebonobashi", "Ichigaya", "Kudanshita",
        "Jimbocho", "Ogawamachi", "Iwamotocho", "Bakuro-yokoyama", "Hamacho",
        "Morishita", "Kikukawa", "Sumiyoshi", "Nishi-ojima", "Ojima", "Higashi-ojima",
        "Funabori", "Ichinoe", "Mizue", "Shinozaki", "Motoyawata"
    ],
    "Toei Oedo Line": [
        "Hikarigaoka", "Nerima-kasugacho", "Toshimaen", "Nerima", "Nerima-sakamachi",
        "Shin-egota", "Ochiai-minami-nagasaki", "Nakai", "Higashi-nakano", "Nakano-sakaue",
        "Nishi-shinjuku-gochome", "Tochomae", "Shinjuku-nishiguchi", "Higashi-shinjuku",
        "Wakamatsu-kawada", "Ushigome-yanagicho", "Ushigome-kagurazaka", "Iidabashi",
        "Kasuga", "Hongosanchome", "Ueno-okachimachi", "Shin-okachimachi", "Kuramae",
        "Ryogoku", "Morishita", "Kiyosumi-shirakawa", "Monzen-nakacho", "Tsukishima",
        "Kachidoki", "Shiodome", "Daimon", "Akasaka-mitsuke", "Roppongi", "Aoyama-itchome",
        "Shinjuku", "Tochomae", "Shinjuku", "Shinjuku-sanchome", "Higashi-shinjuku",
        "Wakamatsu-kawada", "Ushigome-yanagicho", "Ushigome-kagurazaka", "Iidabashi",
        "Kasuga", "Hongosanchome", "Ueno-okachimachi", "Shin-okachimachi", "Kuramae",
        "Ryogoku", "Morishita", "Kiyosumi-shirakawa", "Monzen-nakacho", "Tsukishima",
        "Kachidoki", "Shiodome", "Daimon", "Shiodome", "Tsukishima"
    ]
}

def tourist_attractions_dp(locations, starting_point, time_limit_minutes):
    time_limit_seconds = time_limit_minutes * 60  # Convert the time limit to seconds
    stations = list(locations.keys())
    station_count = len(stations)
    
    # DP table: dp[i][t] will store the maximum satisfaction we can get by visiting station i with t seconds
    dp = [[-1 for _ in range(time_limit_seconds + 1)] for _ in range(station_count)]
    dp[stations.index(starting_point)][0] = 0  # Start at the initial station with 0 time
    
    # Track the path
    path_track = [[[] for _ in range(time_limit_seconds + 1)] for _ in range(station_count)]
    
    # Function to get travel time between two stations (returns time in seconds)
    def get_travel_time(station1, station2):
        for line, stations_in_line in SUBWAY_LINES.items():
            if station1 in stations_in_line and station2 in stations_in_line:
                return SUBWAY_TRAVEL_TIMES[line] * 60  # Convert travel time to seconds
        return float('inf')  # No direct connection
    
    # DP loop: visit each station and attempt to move to other stations
    for t in range(time_limit_seconds):
        for i in range(station_count):
            if dp[i][t] == -1:  # Skip if no valid path to this station at time t
                continue
            current_station = stations[i]
            
            # Try visiting every other station
            for j in range(station_count):
                if i == j:
                    continue
                next_station = stations[j]
                travel_time = get_travel_time(current_station, next_station)
                if travel_time == float('inf'):  # No valid connection
                    continue
                
                # Time and satisfaction for the next station (min_time_spent is converted to seconds)
                next_station_satisfaction, min_time_spent_minutes = locations[next_station]
                min_time_spent_seconds = min_time_spent_minutes * 60  # Convert to seconds
                
                new_time = int(t + travel_time + min_time_spent_seconds)  # Convert new_time to int
                
                if new_time > time_limit_seconds:  # Make sure new_time is within the limit
                    continue
                
                # Update DP table if this path gives better satisfaction
                new_satisfaction = dp[i][t] + next_station_satisfaction
                if new_satisfaction > dp[j][new_time]:
                    dp[j][new_time] = new_satisfaction
                    path_track[j][new_time] = path_track[i][t] + [next_station]
    
    # Find the best satisfaction achievable within the time limit
    best_satisfaction = 0
    best_path = []
    for t in range(time_limit_seconds + 1):
        if dp[stations.index(starting_point)][t] > best_satisfaction:
            best_satisfaction = dp[stations.index(starting_point)][t]
            best_path = path_track[stations.index(starting_point)][t]
    
    # Add the starting point at the beginning and end of the path
    best_path = [starting_point] + best_path + [starting_point]
    
    return {"path": best_path, "satisfaction": best_satisfaction}


locations = {
    "Magome": [0, 0], "Nagatacho": [41, 25], "Sugamo": [26, 35], "Nishigahara": [35, 15], 
    "Tsukishima": [36, 15], "Inaricho": [45, 15], "Nezu": [19, 20], "Monzen-nakacho": [22, 15], 
    "Kodemmacho": [40, 15], "Hasune": [41, 15], "Uchisaiwaicho": [36, 20], "Meiji-jingumae": [34, 35], 
    "Mitsukoshimae": [21, 25], "Asakusa": [29, 20], "Kikukawa": [36, 20], "Shin-ochanomizu": [35, 30], 
    "Ginza": [12, 15], "Nishi-ojima": [12, 15], "Akabane-iwabuchi": [13, 30], "Roppongi-itchome": [18, 35], 
    "Shimura-sakaue": [13, 15], "Gokokuji": [45, 35], "Motohasunuma": [16, 30], "Sendagi": [33, 30], 
    "Ichinoe": [32, 30], "Kudanshita": [11, 25], "Awajicho": [29, 20], "Kasai": [23, 30], 
    "Zoshigaya": [29, 35], "Shimura-sanchome": [45, 30], "Ueno-hirokoji": [34, 35], "Ikebukuro": [41, 30], 
    "Sengakuji": [43, 25], "Nijubashimae": [14, 30], "Baraki-nakayama": [44, 35], "Chikatetsu-akatsuka": [45, 30], 
    "Ueno-okachimachi": [17, 20], "Tawaramachi": [14, 35], "Ryogoku": [15, 15], "Kojimachi": [22, 35], 
    "Toranomon": [14, 30], "Higashi-shinjuku": [19, 15], "Akihabara": [44, 25], "Akasaka-mitsuke": [22, 25], 
    "Ueno": [37, 20], "Gotanda": [26, 35], "Todaimae": [41, 20], "Kinshicho": [17, 35], "Ojima": [13, 25], 
    "Wakoshi": [35, 15], "Nishi-sugamo": [10, 20], "Kamiyacho": [33, 15], "Yotsuya": [18, 35], 
    "Kanda": [12, 25], "Shiba-koen": [14, 35], "Shibuya": [28, 30], "Onarimon": [21, 20], 
    "Iidabashi": [28, 15], "Iriya": [27, 25], "Ushigome-kagurazaka": [23, 30], "Suitengumae": [10, 25], 
    "Shin-takashimadaira": [10, 20], "Ginza-itchome": [33, 20], "Kita-ayase": [20, 20], "Otemachi": [43, 25], 
    "Tameike-sanno": [16, 15], "Aoyama-itchome": [19, 25], "Nakano-fujimicho": [10, 30], 
    "Naka-okachimachi": [19, 30], "Hamacho": [26, 15], "Kokkai-gijidomae": [42, 35], "Sumiyoshi": [37, 35], 
    "Ebisu": [39, 25], "Nishi-waseda": [16, 30], "Nishi-magome": [45, 20], "Higashi-ikebukuro": [16, 20], 
    "Hanzomon": [35, 15], "Kita-sando": [42, 35], "Shinonome": [13, 35], "Shinjuku-nishiguchi": [15, 25]
}
starting_point = "Magome"
time_limit = 480

result = tourist_attractions_dp(locations, starting_point, time_limit)
print(result)
