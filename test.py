import os
import subprocess
import logging
import shutil

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('/tmp/test.log')
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(levelname)s %(asctime)s [%(name)s] %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

command = "free"
options = "-th"
args=[]
args.append(command)
args.append(options)
output = subprocess.run(args,capture_output=True)

print('#################################')
print('Return Code: ', output.returncode)
print(output)

#working_dir = os.getcwd()
#print(working_dir)

#print(os.listdir('/'))

#os.chdir('/tmp')
#try:
#    os.mkdir('./test')
#except:
#    logger.warning('mkdir is failed')

#print(os.listdir('/tmp'))

#os.rmdir('/tmp/test')
#print(os.listdir('/tmp'))
