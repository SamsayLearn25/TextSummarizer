<<<<<<< HEAD
import os, logging, sys

log_dir = "logs"

logging_str = "[%(asctime)s %(levelname)s : %(module)s %(message)s]"

log_filepath = os.path.join(log_dir, "continuos_logs.log")
=======
import os, sys, logging

log_dir = "logs"

log_file = os.path.join(log_dir, "continuos_logs.log")

log_format = "[%(asctime)s %(levelname)s %(module)s - %(message)s]"
>>>>>>> a2e825fa325cb88db03b7c06eb6c668403cd5319

os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
<<<<<<< HEAD
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)


logger = logging.getLogger("summarizer")
=======
    format=log_format,

    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
    
)


logger = logging.getLogger()
>>>>>>> a2e825fa325cb88db03b7c06eb6c668403cd5319
