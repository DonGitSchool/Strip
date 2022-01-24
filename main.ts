function on_pin_pressed_p0 () {
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . . . # .
        . . . . #
        `)
    strip.show()
    reset_counter += 1
    basic.showNumber(reset_counter)
    basic.pause(100)
    if (reset_counter % 3 == 0) {
        strip.showRainbow(1, 360)
        reset_counter = 0
        ABbutton_on2 = false
    } else {
        ABbutton_on2 = false
    }
    ABbutton_on2 = false
}
function on_button_pressed_a () {
    basic.showLeds(`
        # . . . .
        . # . . .
        . . # . .
        . # . # .
        # . . . #
        `)
    strip.setBrightness(100)
    strip.shift(-1)
    strip.show()
}
input.onPinPressed(TouchPin.P2, function () {
    basic.showLeds(`
        # . . . .
        . # . . .
        . . # . .
        . # . # .
        # . . . #
        `)
    strip.setBrightness(100)
    strip.shift(-1)
    strip.show()
})
input.onButtonPressed(Button.AB, function () {
    ABbutton_on3 = true
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . . . # .
        . . . . #
        `)
    while (ABbutton_on3 == true && reset_counter == 0) {
        strip.setBrightness(100)
        strip.shift(1)
        strip.show()
        basic.pause(200)
        input.onButtonPressed(Button.A, on_button_pressed_a)
input.onButtonPressed(Button.B, on_button_pressed_b)
input.onPinPressed(TouchPin.P0, on_pin_pressed_p0)
    }
    ABbutton_on3 = false
})
function on_button_pressed_b () {
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . . . # .
        . . . . #
        `)
    strip.setBrightness(100)
    strip.shift(1)
    strip.show()
}
let ABbutton_on3 = false
let ABbutton_on2 = false
let reset_counter = 0
let strip: neopixel.Strip = null
let ABbutton_on = false
input.onPinPressed(TouchPin.P0, on_pin_pressed_p0)
input.onButtonPressed(Button.A, on_button_pressed_a)
input.onButtonPressed(Button.B, on_button_pressed_b)
basic.showLeds(`
    # . . . .
    . # . . .
    . . # . .
    . . . # .
    . . . . #
    `)
strip = neopixel.create(DigitalPin.P1, 15, NeoPixelMode.RGB_RGB)
strip.showRainbow(1, 360)
basic.forever(function () {
	
})
