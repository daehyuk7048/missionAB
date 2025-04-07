#!/bin/bash

# 3비트용 GPIO 핀 (LSB부터 순서대로)
leds=(18 19 20)

# 초기화: 출력 설정
for pin in "${leds[@]}"; do
    gpioset gpiochip0 $pin=0
done


while true; do
    # 0~7까지 카운트
    for i in {0..7}; do
        # 이진수 변환
        bin=$(printf "%03d" "$(echo "obase=2; $i" | bc)")

        # 각 비트를 해당 GPIO에 매핑
        for j in {0..2}; do
            bit=${bin:2-j:1}  # MSB부터 꺼냄 (bash의 substring)
            gpioset gpiochip0 ${leds[$j]}=$bit
        done

        sleep 1
    done
done
