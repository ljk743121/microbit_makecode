cbit_IR.onPressEvent(RemoteButton.CH_MINUS, function () {
    basic.showArrow(ArrowNames.South)
    SuperBit.MotorRun(SuperBit.enMotors.M1, 255)
})
cbit_IR.onPressEvent(RemoteButton.CH, function () {
    basic.showIcon(IconNames.Square)
    SuperBit.MotorRun(SuperBit.enMotors.M1, 0)
})
cbit_IR.onPressEvent(RemoteButton.CH_Add, function () {
    basic.showArrow(ArrowNames.North)
    SuperBit.MotorRun(SuperBit.enMotors.M1, -255)
})
cbit_IR.init(Pins.P8)
