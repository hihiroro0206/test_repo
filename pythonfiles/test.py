print("Hello World!")

import subprocess
from subprocess import PIPE
checkResult = subprocess.run(['tower-cli','--help'],shell=True, stdout=PIPE, stderr=PIPE, text=True)

cr = checkResult.stdout
print('STDOUT: {}'.format(cr))
# STDOUT: 2019年 12月19日 木曜日 11時46分14秒 JST
