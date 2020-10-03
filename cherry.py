import subprocess
from subprocess import Popen, PIPE
from subprocess import check_output
from flask import Flask

def get_shell_script_output_using_communicate():
    session = Popen(['./some.sh'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = session.communicate()
    if stderr:
        raise Exception("Error "+str(stderr))
    return stdout.decode('utf-8')


def get_shell_script_output_using_check_output():
    stdout = check_output(['./some.sh']).decode('utf-8')
    return stdout




app = Flask(__name__)

@app.route('/stat',methods=['GET',])
def next():
    return get_shell_script_output_using_check_output()

@app.route('/spotify/prev', methods=['GET'])
def prev():
    return get_shell_script_output_using_check_output()


app.run(debug=True)
