import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        # 1. Identify if we are running in parallel (xdist worker ID)
        # This will be 'gw0', 'gw1', etc., or None if running normally
        # worker_id = os.environ.get("PYTEST_XDIST_WORKER", "master")        
        # 2. Define the log filename
        # If in parallel, create 'automation_gw0.log', etc. 
        # This prevents "file-locking" errors.
        # log_name = f"automation_{worker_id}.log" if worker_id else "automation.log"
        
        worker_id = os.environ.get("PYTEST_XDIST_WORKER")

        if worker_id:
            # Parallel Mode (gw0, gw1, etc.)
            log_name = f"automation_{worker_id}.log"
        else:
            # Sequential Mode (Standard)
            log_name = "automation.log"

        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs", log_name)
        
        # 3. Configure formatting
        # Use [%(processName)s] instead of threadName for xdist workers
        # We add [%(page_name)s] as a placeholder
        log_format = f'%(asctime)s: %(levelname)s: [{worker_id}] [%(page_name)s] %(message)s'
        date_format = '%m/%d/%Y %I:%M:%S %p'
        
        # 4. Setup basicConfig
        logging.basicConfig(
            filename=path,
            format=log_format,
            datefmt=date_format,
            force=True
        )
        
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        # 5. Console Handler (Ensures you see output in the terminal)
        if not logger.handlers:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(logging.Formatter(log_format, date_format))
            logger.addHandler(console_handler)

        return logger
