from faker import Faker
import pandas as pd
from random import randint


fake = Faker()
# print(dir(fake))
def generate_fake_data(num_records=100):
    data = []

    for _ in range(num_records):
        dob = fake.date_of_birth(minimum_age=18, maximum_age=60)
        
        # Extract year, month, day from the date_of_birth
        year = dob.year
        month = dob.month
        day = dob.day
        person = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "address": fake.address().replace("\n", ", "),
            "date_of_birth": dob.strftime('%Y-%m-%d')
        }
        data.append(person)

    return data

def save_to_csv(data, filename='output/generated_data.csv'):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"✅ Data successfully written to {filename}")

if __name__ == "__main__":
    data = generate_fake_data(50)
    save_to_csv(data)
