import os
import subprocess
from datetime import datetime

# Main folder
main_folder = "allure-results"
os.makedirs(main_folder, exist_ok=True)

# Current date & time
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Create new folder with date & time
new_folder = os.path.join(main_folder, timestamp)

print(f"Running tests for: {new_folder}")

# Run pytest
subprocess.run(
    f"pytest test_id06.py --alluredir={new_folder}",
    shell=True
)

# Serve report
subprocess.run(
    f"allure serve {new_folder}",
    shell=True
)