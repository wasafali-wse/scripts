import subprocess
import datetime
import os

# --- Configuration ---
HOST = '192.168.100.115'
PORT = '5432'
USER = 'wasaf'
PASSWORD = '#waheed1118#Postgres#'
DB_NAME = 'waheedsons'
BACKUP_DIR = 'C:\\database\\backup'  # Ensure this directory exists
PG_DUMP_PATH = 'C:\\Program Files\\pgAdmin 4\\runtime\\pg_dump.exe'  # Path to pg_dump.exeC:\Program Files\pgAdmin 4\runtime

# --- Script Logic ---

def create_backup():
    """Creates a SQL backup of the PostgreSQL database."""

    # Ensure backup directory exists
    if not os.path.exists(BACKUP_DIR):
        try:
            os.makedirs(BACKUP_DIR)
        except OSError as e:
            print(f"Error creating backup directory: {e}")
            return False

    # Generate a timestamped filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(BACKUP_DIR, f"{DB_NAME}_backup_.sql")

    # Construct the pg_dump command
    command = [
        PG_DUMP_PATH,
        '-h', HOST,
        '-p', PORT,
        '-U', USER,
        '-F', 'p',  # Plain SQL script
        '-f', backup_file,
        DB_NAME
    ]

    # Set environment variable for password
    env = os.environ.copy()
    env['PGPASSWORD'] = PASSWORD

    # Execute the command
    try:
        subprocess.run(command, check=True, env=env, capture_output=True, text=True)
        print(f"Backup created successfully: {backup_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error creating backup: {e}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
        return False
    except FileNotFoundError:
        print(f"Error: pg_dump not found at {PG_DUMP_PATH}. Check the path.")
        return False

if __name__ == "__main__":
    if create_backup():
        print("Backup process completed.")
    else:
        print("Backup process failed.")