#!/bin/bash

leds=(18 19 20 21)

# 초기화: 출력 설정
for pin in "${leds[@]}"; do
    gpioset gpiochip0 $pin=0
done

while true; do
    for pin in "${leds[@]}"; do
        gpioset gpiochip0 $pin=1
        sleep 1
        gpioset gpiochip0 $pin=0
    done
done

