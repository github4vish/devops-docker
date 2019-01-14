from flask import Flask
from redis import Redis, RedisError
import os
import socket

#Connect to Redis
redis= Redis( host = "redis", db=0, socket_connect_timeout=2, socket_timeout=2)


ap=Flask(_name_)
@app.route("/")
def hello():
 try:
   visits="<i>cannot connect to Redis, counter disabled</i>

 html="<h3>Hello {name}!</h3>"\
      "<b>Hostname:</b>{hostname}<br/>"\
      "<b>Visits:</b>{visits}"
 return html.format(name=os.getenv"Name","world"), hostname=socket.gethostname(), visits=visits)

if__name__=="__main__":
  app.run(host='0.0.0.0',port=80)
