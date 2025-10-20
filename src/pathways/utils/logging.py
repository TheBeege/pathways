import logging
import json
import sys


class JsonFormatter(logging.Formatter):
    """Custom JSON formatter for logging"""
    def format(self, record):
        log_data = {
            "timestamp": self.formatTime(record, "%Y-%m-%d %H:%M:%S"),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_data)


def configure_logging(log_level: str = "INFO"):
    """Configure JSON formatted logging for the pathways logger"""
    log_handler = logging.StreamHandler(sys.stdout)
    log_handler.setFormatter(JsonFormatter())

    # Configure the pathways logger
    pathways_logger = logging.getLogger("pathways")
    pathways_logger.addHandler(log_handler)
    pathways_logger.setLevel(log_level.upper())
    pathways_logger.propagate = False  # Don't propagate to root logger

    return pathways_logger


def get_logger() -> logging.Logger:
    """Dependency function to get the pathways logger"""
    return logging.getLogger("pathways")
