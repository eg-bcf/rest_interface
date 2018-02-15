    from pump import Pump
    from flask import Flask

    app = Flask(__name__)

    piston = 0
    def create_pump(num):
        print(num)
        return Pump(num)

    @app.route("/")
    def hello():
        return "Hello World!"

    @app.route("/create/<path:port>")
    def create_port(port):
        global piston
        piston = create_pump(port)
        return "created"

    @app.route("/setup")
    def pump_setup():
        print("setup")
        global piston
        piston.setupPump()
        return "Setup"

    @app.route("/home")
    def pump_home():
        print("home")
        global piston
        piston.homePiston()
        return "Homed"

    @app.route("/dispense/<int:dispense>/<int:tpi>")
    def pump_dispense(dispense, tpi):
        print(dispense, tpi)
        global piston
        piston.dispensePercent(dispense, tpi)
        return "Dispensed"

    @app.route("/aspirate/<int:aspirate>/<int:tpi>")
    def pump_aspirate(aspirate, tpi):
        print(aspirate, tpi)
        global piston
        piston.aspiratePercent(aspirate, tpi)
        return "Aspirated"

    @app.route("/prime/<int:tpi>")
    def pump_prime(tpi):
        print(tpi)
        global piston
        piston.primePiston(tpi)
        print("Priming")

    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=80, debug=True)
