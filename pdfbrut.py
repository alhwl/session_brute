import subprocess

# Path to the word list file
file_path = 'rockyou.txt'

# Command template
base_command = 'pdftk encrypted.pdf input_pw {} output output.pdf'

# Open the file and read each line
with open(file_path, 'r', encoding='latin-1') as file:
    for line in file:
        # Strip newline characters from each line
        password = line.strip()
        
        # Substitute {} with the current password
        command_to_run = base_command.format(password)
        
        try:
            # Execute the command
            subprocess.run(command_to_run, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            print(f"Success with password: {password}")
            break  # If successful, stop the loop
        except subprocess.CalledProcessError:
            # If the command failed (wrong password), continue with the next one
            continue
