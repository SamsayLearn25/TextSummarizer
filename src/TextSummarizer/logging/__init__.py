import os, sys, logging

log_dir = "logs"

log_file = os.path.join(log_dir, "continuos_logs.log")

log_format = "[%(asctime)s %(levelname)s %(module)s - %(message)s]"

os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=log_format,

    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
    
)


logger = logging.getLogger()
