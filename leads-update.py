import argparse
import csv

def read_csv(csv_path):
    interesting_fields = {"Summary", "Issue key", "Resolution"}
    columns = {}
    tasks = []
    with open(csv_path, newline='') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0:
                for j, col in enumerate(row):
                    if col in interesting_fields:
                        columns[j] = col
            else:
                task = {}
                for j, col in enumerate(row):
                    if j in columns:
                        if columns[j] in interesting_fields:
                            task[columns[j]] = col
                tasks.append(task)
    return tasks

def filter_tickets(tickets):
    skip_resolutions = {"Duplicate", "Won\'t Fix", "Works as Designed", "Gone away", "Declined", "Won\'t Do"}
    return [ticket for ticket in tickets if ticket['Resolution'] not in skip_resolutions]

def pp_tickets(tickets):
    for ticket in tickets:
        print("{0} (https://jira.mongodb.org/browse/{1})".format(ticket["Summary"], ticket["Issue key"]))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path")
    tickets = read_csv(parser.parse_args().csv_path)
    filtered = filter_tickets(tickets)
    pp_tickets(filtered)
