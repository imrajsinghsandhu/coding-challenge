import json
from flask import Flask, request, jsonify
import re

from routes import app

def parse_input(input_data):
    lab_data = []
    for table in input_data:
        labs = []
        rows = table.split('\n')[1:]  # Skip the header
        for row in rows:
            if not row.strip():
                continue
            columns = row.split('|')[1:-1]  # Split and remove excess
            lab = int(columns[0].strip())
            cell_counts = list(map(int, re.findall(r'\d+', columns[1])))
            increment = columns[2].strip()
            condition = list(map(int, columns[3].split()))
            labs.append({
                "lab": lab,
                "cell_counts": cell_counts,
                "increment": increment,
                "condition": condition
            })
        lab_data.append(labs)
    return lab_data

def simulate_lab_work(lab_data):
    results = []
    for labs in lab_data:
        days_results = {}
        lab_analysis = [0] * len(labs)  # Track number of dishes analyzed by each lab

        for day in range(1, 10001):
            next_day_labs = [[] for _ in labs]

            for lab in labs:
                current_lab = lab['lab']
                for count in lab['cell_counts']:
                    # Update the count
                    if 'count *' in lab['increment']:
                        factor = int(lab['increment'].split('*')[1].strip())
                        new_count = count * (factor if factor != 'count' else count)
                    else:
                        addition = int(lab['increment'].split('+')[1].strip())
                        new_count = count + (addition if addition != 'count' else count)

                    # Check condition
                    divisor, true_lab, false_lab = lab['condition']
                    if new_count % divisor == 0:
                        next_day_labs[true_lab].append(new_count)
                    else:
                        next_day_labs[false_lab].append(new_count)

                    lab_analysis[current_lab] += 1  # Increment the dish analysis count

            # Update labs with new cell counts for the next day
            for i, lab in enumerate(labs):
                lab['cell_counts'] = next_day_labs[i]

            # Log the results every 1000 days
            if day % 1000 == 0:
                days_results[day] = lab_analysis.copy()

        results.append(days_results)

    return results

@app.route('/lab_work', methods=['POST'])
def lab_work():
    input_data = request.json
    lab_data = parse_input(input_data)
    results = simulate_lab_work(lab_data)
    return jsonify(results)
