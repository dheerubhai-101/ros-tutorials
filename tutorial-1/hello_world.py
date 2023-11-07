import logging

def log():
    # Configure the logging system to log to the terminal
    logging.basicConfig(level=logging.INFO)

    # Create a logger
    logger = logging.getLogger("stdout stream")

    # Log messages
    logger.info("Hello World, I am listening to you")

# Main program entry point
if __name__ == "__main__":
    log()
