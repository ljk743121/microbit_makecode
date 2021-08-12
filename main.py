def on_press_ch_minus():
    basic.show_arrow(ArrowNames.SOUTH)
    SuperBit.motor_run(SuperBit.enMotors.M1, -255)
    music.start_melody(music.built_in_melody(Melodies.POWER_DOWN),
        MelodyOptions.ONCE)
cbit_IR.on_press_event(RemoteButton.CH_MINUS, on_press_ch_minus)

def on_press_ch():
    basic.show_arrow(ArrowNames.SOUTH)
    SuperBit.motor_run(SuperBit.enMotors.M1, 0)
cbit_IR.on_press_event(RemoteButton.CH, on_press_ch)

def on_press_ch_add():
    basic.show_arrow(ArrowNames.NORTH)
    SuperBit.motor_run(SuperBit.enMotors.M1, 255)
    music.start_melody(music.built_in_melody(Melodies.POWER_UP), MelodyOptions.ONCE)
cbit_IR.on_press_event(RemoteButton.CH_ADD, on_press_ch_add)

cbit_IR.init(Pins.P16)