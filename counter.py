import subprocess
from subprocess import Popen, PIPE
from subprocess import check_output
from flask import Flask

def get_shell_script_output_using_communicate():
    session = Popen(['./netstat.sh'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = session.communicate()
    if stderr:
        raise Exception("Error "+str(stderr))
    return stdout.decode('utf-8')


def get_shell_script_output_using_check_output():
    stdout = check_output(['./netstat.sh']).decode('utf-8')
    return stdout




app = Flask(__name__)

@app.route('/api/v1/visitors/total',methods=['GET',])
def next():
    return get_shell_script_output_using_check_output()

@app.route('/werkt',methods=['GET',])
def next2():
    return "Hoera!"


app.run(host='0.0.0.0')

