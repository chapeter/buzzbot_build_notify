__author__ = 'Chad Peterson'
__email__ = 'chapeter@cisco.com'

from flask import Flask
from flask import request

app = Flask(__name__)

from spark.rooms import Room
from spark.session import Session

token = os.environ['SPARK_BOT_TOKEN']
url = 'https://api.ciscospark.com'
session = Session(url, token)
auth = "Bearer %s" % token

roomid = os.environ['SPARK_ROOMID']

@app.route("/buzzbot/api/build", methods=['POST'])
def buildNotification():
    data = request.get_json()
    repo = data['repository']['repo_name']

    room = Room(attributes={'id':roomid})
    room.send_message("New build of {0}:{1}".format(repo, data['push_data']['tag']))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)