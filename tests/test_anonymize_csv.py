import pandas as pd
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from anonymize_csv import anonymize_data

# Test if the CSV file is generated correctly
def test_csv_generation():
    input_file = 'output/generated_data.csv'
    output_file = 'output/anonymized_data.csv'

    # Ensure that the generated CSV file has the required columns
    anonymize_data(input_file, output_file)

    df = pd.read_csv(output_file)
    assert 'first_name' in df.columns
    assert 'last_name' in df.columns
    assert 'address' in df.columns
    assert 'date_of_birth' in df.columns

# Test if anonymization changes first_name, last_name, and address
def test_anonymization():
    input_file = 'output/generated_data.csv'
    output_file = 'output/anonymized_data.csv'

    # Generate anonymized data
    anonymize_data(input_file, output_file)

    df = pd.read_csv(output_file)

    # Check that the first name, last name, and address are anonymized
    assert df['first_name'][0] != 'John'  # Assuming 'John' is in the original data
    assert df['last_name'][0] != 'Doe'   # Assuming 'Doe' is in the original data
    assert df['address'][0] != '123 Main St'  # Assuming '123 Main St' is in the original data

# Test if other columns remain unchanged
def test_other_columns():
    input_file = 'output/generated_data.csv'
    output_file = 'output/anonymized_data.csv'

    anonymize_data(input_file, output_file)

    df_input = pd.read_csv(input_file)
    df_output = pd.read_csv(output_file)

    # Check that date_of_birth is not changed
    assert df_input['date_of_birth'][0] == df_output['date_of_birth'][0]
