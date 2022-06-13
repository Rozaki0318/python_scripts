import subprocess

SRC_DIR='/tmp/'
SRC_FILES='test.log'
DEST_DIR='/home/ozaki/backup/'

command = "cp"
options = "-r"
args=[]
args.append(command)
args.append(options)
args.append(SRC_DIR+SRC_FILES)
args.append(DEST_DIR)
output = subprocess.run(args,capture_output=True)

print('#################################')
print('Return Code: ', output.returncode)
print(output)
