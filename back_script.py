import subprocess
import datetime
import os

# --- Configuration ---
DB_USER = 'root'          # MySQL username
DB_PASS = ''              # MySQL password (leave blank if none)
DB_NAME = 'wasaf'         # Database to backup
BACKUP_DIR = 'C:\\database\\backup'  # Directory to store backups (ensure it exists)
MYSQLDUMP_PATH = 'C:\\xampp\\mysql\\bin\\mysqldump'  # Path to mysqldump.exe

# --- Script Logic ---

def create_backup():
    """Creates a SQL backup of the database."""

    # Ensure backup directory exists
    if not os.path.exists(BACKUP_DIR):
        try:
            os.makedirs(BACKUP_DIR)
        except OSError as e:
            print(f"Error creating backup directory: {e}")
            return False

    # Generate a timestamped filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(BACKUP_DIR, f"{DB_NAME}_backup_{timestamp}.sql")

    # Construct the mysqldump command
    command = [
        MYSQLDUMP_PATH,
        '-u', DB_USER,
        f'--databases', DB_NAME,
        f'--result-file={backup_file}'
    ]

    # Add password if it exists
    if DB_PASS:
        command.extend(['-p' + DB_PASS]) # Corrected password handling

    # Execute the command
    try:
        subprocess.run(command, check=True, capture_output=True, text=True)  # Use subprocess.run

        print(f"Backup created successfully: {backup_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error creating backup: {e}")
        print(f"Stdout: {e.stdout}")  # Print standard output for more debugging info
        print(f"Stderr: {e.stderr}")  # Print standard error for more debugging info
        return False
    except FileNotFoundError:
        print(f"Error: mysqldump not found at {MYSQLDUMP_PATH}.  Check the path.")
        return False


if __name__ == "__main__":
    if create_backup():
        print("Backup process completed.")
    else:
        print("Backup process failed.")