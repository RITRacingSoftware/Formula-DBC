cells = 27
segments = 5

#Voltages
f = open("voltages.txt", "w").close()
f = open("voltages.txt", "w")

length = 9
seg = 0
mul = 0
first_start = 5
start = first_start

for i in range(cells * segments):
    letter = chr(65 + seg) 
    seg_num = letter + str((i % cells))
   
    if (start + length > 63):
        start = first_start
        mul += 1

    if (i % cells == cells - 1):
        seg += 1

    f.write(' SG_ BMS_Voltages_{} m{} : {}|{}@1+ (0.01,0) [0|5.12] "V" Vector__XXX\n'.format(seg_num, mul, start, length))
    start += length
f.close()

# Thermistor Voltages
f = open("therm_voltages.txt", "w").close()
f = open("therm_voltages.txt", "w")

therms = 6
length = 9
seg = 0
mul = 0
first_start = 3
start = first_start
for i in range(therms * segments):
    letter = chr(65 + seg)
    seg_num = letter + str((i % therms ))

    if (start + length > 63):
        start = first_start
        mul += 1

    if (i % therms == therms - 1):
        seg += 1

    f.write(' SG_ BMS_ThermistorVoltages_{} m{} : {}|{}@1+ (0.01,0) [0|5.12] "V" Vector__XXX\n'.format(seg_num, mul, start, length))
    start += length
f.close()

#Temps
f = open("temps.txt", "w").close()
f = open("temps.txt", "w")

length = 10
seg = 0
mul = 0
first_start = 3
start = first_start

f.write(' SG_ BMS_Temperatures_mux M : 0|{}@1+ (1,0) [0|{}] "" Vector__XXX\n'.format(first_start, (2**first_start - 1)))

for i in range(therms * segments):
    letter = chr(65 + seg) 
    seg_num = letter + str((i % therms))
   
    if (start + length > 63):
        start = first_start
        mul += 1

    if (i % therms == therms - 1):
        seg += 1

    f.write(' SG_ BMS_Temperatures_{} m{} : {}|{}@1+ (0.1,0) [0|102.3] "C" Vector__XXX\n'.format(seg_num, mul, start, length))
    start += length
f.close()

# Drain Status
f = open("drain_status.txt", "w").close()
f = open("drain_status.txt", "w")

length = 1
seg = 0
mul = 0
first_start = 3
start = first_start

for i in range(cells * segments):
    letter = chr(65 + seg) 
    seg_num = letter + str((i % cells))
   
    if (start + length > 64):
        start = first_start
        mul += 1

    if (i % cells == cells - 1):
        seg += 1

    f.write(' SG_ BMS_DrainStatus_{} m{} : {}|{}@1+ (1,0) [0|1] "" Vector__XXX\n'.format(seg_num, mul, start, length))
    start += length
f.close()

