1) Set Up Project Folder We created a repository and we clone that repo.
        git clone https://github.com/jksurampudi5/csv-anonymizer.git
        cd civ-anonymizer


2) Create a Virtual Environment and install Required Packages(pandas,faker)


        python3 -m venv jkvenv
        source jkvenv/bin/activate
        pip install pandas faker
        pip freeze > requirements.txt

3)  Create requirements.txt
	    pip freeze > requirements.txt

4)  Create Your Python Scripts
	    touch generating_csv.py anonymize_csv.py

5)  Create Folder for CSV Output:
	    mkdir output

6)  Initialize Git and Set Up Repository:
        git init

7)  Creating a feature branch:
        git checkout -b feature/jk-csv-anonymization
        git add .
        git commit -m "Add CSV generation and anonymization scripts"
        git push -u origin feature/jk-csv-anonymization


8) Raise PR In Git Repo:Raise Pull Request and check for any conflicts before merging to main
        git pull origin feature/jk-csv-anonymization


9. Anonymization of Data->Here we need to write code modifications in anonymize_csv.py file we made some transformations on original  csv file and  made  saved in the same output folder as  anonymize.csv file Post this we do the same steps like 

        git add .
        git commit -m "Add "generated anonymized csv file”
        git push -u origin feature/jk-csv-anonymization


10. Adding Tests cases:
        pip install pytest
        pip freeze > requirements.txt
        (this will provide the package version  in requirements.txt file)

        mkdir tests
        cd tests
        touch test_anonymize_csv.py
        (write transformation code in this file)

        
11. Post this we need to deploy using Docker  below are the steps and commands we need to follow.

1) Build the Docker image:
        docker build -t csv-anonymizer .

2) Run the Docker container
	    docker run csv-anonymizer


 3) Saving the tar file:
	    docker save -o csv-anonymizer.tar csv-anonymizer


4)  Load the image:
	    docker load -i csv-anonymizer.tar


5)  To load tar file:
	    docker load -i csv-anonymizer.tar
