# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit


#https://mortoray.com/2014/03/04/http-streaming-of-command-output-in-python-flask/

import flask
from shelljob import proc

import eventlet
eventlet.monkey_patch()

app = flask.Flask(__name__)

@app.route( '/stream' )
def stream():
    g = proc.Group()
    p = g.run( [ "python", "-u", "taildiy.py","ascii.txt" ] )##

    def read_process():
        while g.is_pending():
            lines = g.readlines()
            for proc, line in lines:
                yield ("data:" + str(line) + "\n\n")

    return flask.Response( read_process(), mimetype= 'text/event-stream' )


@app.route('/page')
def get_page():
    return flask.send_file('templates/page.html')

if __name__ == "__main__":
    app.run(debug=True)
