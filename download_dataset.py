import os
import requests
import zipfile
from subprocess import call

print("")

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00240/UCI HAR Dataset.zip"

if not os.path.exists("UCI HAR Dataset.zip"):
    response = requests.get(url)
    with open("UCI HAR Dataset.zip", "wb") as f:
        f.write(response.content)
    print("Downloading Done...\n")
else:
    print("Dataset already downloaded. Did not download twice.\n")

print("Extracting...")
extract_dir = os.path.abspath("UCI HAR Dataset")
if not os.path.exists(extract_dir):
    with zipfile.ZipFile("UCI HAR Dataset.zip", "r") as zip_ref:
        zip_ref.extractall(extract_dir)
    print("Extracting successfully done to {}.".format(extract_dir))
else:
    print("Dataset already extracted. Did not extract twice\n")
