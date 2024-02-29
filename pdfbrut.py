import subprocess
import os

# Path to the word list file
file_path = 'rockyou.txt'

# Open the file and read each line
with open(file_path, 'r', encoding='latin-1') as file:
    for line in file:
        # Strip newline characters from each line
        password = line.strip()
        
        # Command to run
        command_to_run = ['pdftk', 'encrypted.pdf', 'input_pw', password, 'output', 'output.pdf']
        
        # Execute the command
        result = subprocess.run(command_to_run, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        
        # Check for success indicator - this is simplistic and might need to be adjusted based on pdftk's actual behavior
        if "Error" not in result.stderr and os.path.exists("output.pdf") and os.path.getsize("output.pdf") > 0:
            print(f"Success with password: {password}")
            break  # Exit the loop if successful
        else:
            # Optionally, remove the output.pdf if it's invalid to clean up before the next attempt
            try:
                os.remove("output.pdf")
            except OSError:
                pass  # If file doesn't exist or can't be removed, ignore and continue