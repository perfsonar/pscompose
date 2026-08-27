from pscompose.settings import LOGLEVEL
import logging

logging.basicConfig(
    level=getattr(logging, LOGLEVEL.upper()), format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()
