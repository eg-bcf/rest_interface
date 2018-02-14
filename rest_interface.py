from flask import Flask
import serial

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/pump/<int:task_id>")
def pump(task_id):
    print(task_id)
    return "Hello World!"

@app.route("/dispense/<int:dispense>")
def pump_dispense(dispense):
    print(dispense)
    dispensePercent(dispense)
    return "Hello World!"

@app.route("/aspirate/<int:aspirate>")
def pump_aspirate(aspirate):
    print(aspirate)
    aspiratePercent(aspirate)
    return "Hello World!"

@app.route("/home")
def pump_home():
    print("home")
    homePiston()
    return "Hello World"

@app.route("/setup")
def pump_setup():
    print("setup")
    setupPump()
    return "Hello World"

@app.route("/create/<port>")
def create_pump(port):
    print(port)
    createPumpPort(port)
    return "Hello World"


def createPumpPort(port):
    self.pump = serial.Serial(
        port,
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
    )

def setupPump():
    setupString = '/1' + 'j16m100R\r\n'
    self.pump.write(setupString.encode())

def homePiston():
    accel = str(round(int(100000 * 65536 / 400000000)))
    homeString = '/1' + 'V' + "16000" + 'L' + accel + 'ZR\r\n'
    self.pump.write(homeString.encode())

def dispensePercent(amount):
    steps = str(40 * 1600 * amount/100)
    accel = str(round(int(self.piston_a.get()) * 65536 / 400000000))
    dispenseString = '/' + str(self.piston_address.get()) + 'V' + self.piston_v.get() + 'L'  + accel + 'P' + steps + 'R\r\n'
    self.pump.write(dispenseString.encode())

def aspiratePercent(amount):
    steps = str(40 * 1600 * amount/100))
    accel = str(round(100000 * 65536 / 400000000))
    aspirateString = '/1' + 'V' + "16000" + 'L'  + accel + 'D' + steps + 'R\r\n'
    self.pump.write(aspirateString.encode())

def stopPiston():
    stopString = '/1' + 'TR\r\n'
    self.pump.write(stopString.encode())




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
