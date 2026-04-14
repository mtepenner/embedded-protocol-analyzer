import csv

def export_to_csv(data, filename="data/logs/export.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Protocol", "Alert Level", "Message"])
        for row in data:
            writer.writerow(row)
