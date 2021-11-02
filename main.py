input.onButtonPressed(Button.A, function () {
    OLED.writeStringNewLine("Øyeblikksverdi ")
    basic.showNumber(måltVerdiFukt)
    OLED.writeNumNewLine(måltVerdiFukt)
})
input.onButtonPressed(Button.B, function () {
    OLED.writeStringNewLine(list)
})
let gjennomsnittsverdiFukt = 0
let list = ""
let måltVerdiFukt = 0
OLED.init(128, 64)
let Index = 0
let ønsketVerdiFukt = 70
let tabell: string = [
0,
0,
0,
0,
0,
0,
0,
0,
0,
0
]
for (let index = 0; index < 10; index++) {
    tabell[Index] = måltVerdiFukt
    Index += 1
}
basic.forever(function () {
    måltVerdiFukt = måltVerdiFukt
    if (gjennomsnittsverdiFukt < smarthome.ReadSoilHumidity(AnalogPin.P1)) {
        smarthome.Relay(DigitalPin.P8, smarthome.RelayStateList.Off)
    } else {
        smarthome.Relay(DigitalPin.P8, smarthome.RelayStateList.On)
    }
})
basic.forever(function () {
    gjennomsnittsverdiFukt = (tabell[1] + tabell[2] + tabell[3] + (tabell[4] + (tabell[5] + tabell[6] + tabell[7] + tabell[8]) + (tabell[9] + tabell[10]))) / tabell.length
})
basic.forever(function () {
    if (Index < 10) {
        list.insertAt(Index, tabell[Index - 1])
        Index += 1
    }
    Index = 1
    list.unshift(måltVerdiFukt)
})
