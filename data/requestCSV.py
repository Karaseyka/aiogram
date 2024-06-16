import csv


async def read_users():
    with open('data/users.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        return [i[0] for i in reader if len(i) > 0]


async def write_user(users):
    with open('data/users.csv', 'w', newline='') as csvfile:
        writer = csv.writer(
            csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in users:
            writer.writerow([i])
