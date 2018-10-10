from datetime import datetime
from datetime import timedelta
import io
import os
import pprint
import logging
import json
print(datetime.now())
print(datetime.now().isoformat())
print(datetime.now().strftime("%Y-%m-%d"))
print(datetime.now().strftime("%Y-%m-%dT%H-%M"))
print(datetime.now().strftime("%Y-%m-%dT%H:%M"))

print('#timedelta')
print(datetime.now() + timedelta(hours=1))
print("#Grinwich time")
print(datetime.utcnow())

#files
file = open("file.txt", 'w')
file.write("Hello world")
file.close()
with open('file.txt', 'r') as file:
	print(file.read())
#io
# creating files na letu
print('io')
bytebuffer = io.BytesIO()
# bytebuffer = io.StringIO()
bytebuffer.write(b'Hello World')
print(bytebuffer.getvalue())
bytebuffer.close()
# making dir
# os.mkdir('test1')
#working in bash
#'test' in os.listdir()
print(os.path.isfile('test'))
# environmental vars
print(os.environ.get("HELLO"))
pprint.pprint(dir(os.environ))
# logging
#creates file and stream logger
# logger = logging.getLogger("my_logger")
# logger.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# stream = logging.StreamHandler()
# file = logging.FileHandler("logging.log")
# stream.setFormatter(formatter)
# file.setFormatter(formatter)
# logger.addHandler(stream)
# logger.addHandler(file)
# logger.info("Hello World")
# logger.warning("Warning! Achtung! You can break something")

# json
data = {"one": 1, "two": 2, "three": 3}
#converts dict to string
print(json.dumps(data))
json_data = '{"hello": "world"}'
# from string to json data
print(json.loads(json_data))
print(json.loads(json_data)['hello'])


