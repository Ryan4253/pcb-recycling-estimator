import numpy

class PID:
    def __init__(self, kP, kI, kD, minPower = 0, maxError = None):
        self.kP = kP
        self.kI = kI
        self.kD = kD
        self.minPower = minPower
        self.maxError = maxError
        self.error = None
        self.prevError = None
        self.integral = 0
        self.derivative = None

    def step(self, error, dt):
        self.error = error
        self.derivative = (self.error - self.prevError) / dt
        self.integral += self.error * dt
        self.prevError = self.error

        output = self.kP * self.error + self.kI * self.integral + self.kD * self.derivative

        if(abs(self.output) < self.minPower):
            output = numpy.sign(self.output) * self.minPower

        return output

    def reset(self):
        self.error = None
        self.prevError = None
        self.integral = 0
        self.derivative = None

    def getError(self):
        return self.error

    def isSettled(self):
        return self.error < self.maxError