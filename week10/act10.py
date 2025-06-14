# Decompose the following function and share your results via a GitHub link. 
# See the function below:
 
import datetime
 
def main():

    log_event("event", "id", "message")

 
def log_event(event_type, user_id, message):
    """Logs an event to a file with timestamp, event type, user ID, and message."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] [{event_type}] User: {user_id} - {message}\n"
    read_log_message(log_message)

def read_log_message(log_message):
    with open("rental_log.txt", "a") as log_file:
        log_file.write(log_message)

if __name__ == "__main__":
    main()