import json
import logging
import random
import time
import psycopg2
from datetime import datetime
from psycopg2.extras import Json
conn = psycopg2.connect(dbname='pg', user='pg',
                        password='pg', host='127.0.0.1')
cur = conn.cursor()



 
logging.basicConfig(
    level="INFO",
    format="%(asctime)s — %(name)s — %(levelname)s — %(message)s",
)
logger = logging.getLogger(__name__)
 
 
if __name__ == "__main__":
    while True:
        msg = dict()
        for level in range(50):
            (
                msg[f"bid_{str(level).zfill(2)}"],
                msg[f"ask_{str(level).zfill(2)}"],
            ) = (
                random.randrange(1, 100),
                random.randrange(100, 200),
            )
        msg["stats"] = {
            "sum_bid": sum(v for k, v in msg.items() if "bid" in k),
            "sum_ask": sum(v for k, v in msg.items() if "ask" in k),
        }
        logger.info(f"{json.dumps(msg)}")
        datenow = str(datetime.now())
        message = str(json.dumps(msg))
        query = "INSERT INTO log (message, date ) VALUES (%s, %s);"
        data = (message, datenow)
        cur.execute(query, data)
        conn.commit()
        time.sleep(0.1)
