from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import threading
import serial

class WriterReaderSerial():
    def __init__(self):
        self.serialPort = serial.Serial(port = "/dev/ttyS1", baudrate=1000000)
        self.lastType = 0
        threading.Thread(target=self.serialRead, daemon=True).start()

    def setCmd(self, cmd):
        format_cmd = "lavr:{0}#\n".format(cmd)
        print(format_cmd.encode())
        self.serialPort.write(format_cmd.encode())
    
    def serialRead(self):
        while True:
            serialString = self.serialPort.readline()
            print(serialString)
            try:
                msg_int = int(serialString.decode().split(":")[1].strip().replace("#", ""))
                if msg_int == 0:
                    self.lastType = 0
                else:
                    self.lastType = msg_int / 11
            except:
                pass

app = FastAPI()
writerReader = WriterReaderSerial()
tasks = [
    { "id": 0, "name": "Ожидание" },
    { "id": 1, "name": "Езда по линии" },
    # { "id": 2, "name": "task2" },
    # { "id": 3, "name": "task3" },
    # { "id": 4, "name": "task4" },
],

origins = [
    "*"
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/list")
def read_root():
    return {"tasks": tasks}

@app.get("/api/get")
def read_root():
    global currentId
    return {"id": writerReader.lastType}

@app.get("/api/set/{item_id}")
def read_root(item_id: int,):
    writerReader.setCmd(item_id)
    return {}