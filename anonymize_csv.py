import pandas as pd
from faker import Faker
# Initialize Faker instance
fake = Faker()

def anonymize_data(input_file='output/generated_data.csv', output_file='output/anonymized_data.csv'):
    # Load the original CSV data
    df = pd.read_csv(input_file)
    
    # Check if required columns exist in the data
    if not all(col in df.columns for col in ['first_name', 'last_name', 'address']):
        print(" Missing required columns in the CSV.")
        return
    
    # Anonymize the required columns
    df['first_name'] = df['first_name'].apply(lambda _: fake.first_name())
    df['last_name'] = df['last_name'].apply(lambda _: fake.last_name())
    df['address'] = df['address'].apply(lambda _: fake.address().replace("\n", ", "))  # Clean formatting
    
    # Save the anonymized data to a new CSV file
    df.to_csv(output_file, index=False)
    print(f" Anonymized data saved to {output_file}")

if __name__ == "__main__":
    anonymize_data()


