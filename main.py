def on_pin_pressed_p0():
    global reset_counter, ABbutton_on2
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                . . . # .
                . . . . #
    """)
    strip.show()
    reset_counter += 1
    basic.show_number(reset_counter)
    basic.pause(100)
    if reset_counter % 3 == 0:
        strip.show_rainbow(1, 360)
        reset_counter = 0
        ABbutton_on2 = False
    else:
        ABbutton_on2 = False
    ABbutton_on2 = False
def on_button_pressed_a():
    basic.show_leds("""
        # . . . .
                . # . . .
                . . # . .
                . # . # .
                # . . . #
    """)
    strip.set_brightness(100)
    strip.shift(-1)
    strip.show()

def on_pin_pressed_p2():
    basic.show_leds("""
        # . . . .
                . # . . .
                . . # . .
                . # . # .
                # . . . #
    """)
    strip.set_brightness(100)
    strip.shift(-1)
    strip.show()
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_ab():
    global ABbutton_on3
    ABbutton_on3 = True
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                . . . # .
                . . . . #
    """)
    while ABbutton_on3 == True and reset_counter == 0:
        strip.set_brightness(100)
        strip.shift(1)
        strip.show()
        basic.pause(200)
        input.on_button_pressed(Button.A, on_button_pressed_a)
        input.on_button_pressed(Button.B, on_button_pressed_b)
        input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)
    ABbutton_on3 = False
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                . . . # .
                . . . . #
    """)
    strip.set_brightness(100)
    strip.shift(1)
    strip.show()
ABbutton_on3 = False
ABbutton_on2 = False
reset_counter = 0
strip: neopixel.Strip = None
ABbutton_on = False
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)
input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)
basic.show_leds("""
    # . . . .
        . # . . .
        . . # . .
        . . . # .
        . . . . #
""")
strip = neopixel.create(DigitalPin.P1, 15, NeoPixelMode.RGB_RGB)
strip.show_rainbow(1, 360)

def on_forever():
    pass
basic.forever(on_forever)
