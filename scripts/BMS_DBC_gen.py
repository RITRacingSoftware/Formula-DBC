import math

cells = 27
chips = 2
segments = 5
therms = 6

GEN_CELL_VOLTAGES = 1
GEN_CHIP_VOLTAGES = 1
GEN_THERM_VOLTAGES = 1
GEN_TEMPS = 1
GEN_DRAIN_STATUS = 1


if (GEN_CELL_VOLTAGES):
    #Voltages
    f = open("voltages.txt", "w").close()
    f = open("voltages.txt", "w")

    length = 9
    seg = 0
    mul = 0
    first_start = 5
    start = first_start
    one_mul = math.floor((64 - first_start) / length); # Number of signals that can fit in one message
    num_mul = math.ceil((cells * segments) / one_mul) - 1;  # Total number of multiplexed messages needed
    f.write(' SG_ BMS_Voltages_mux M : 0|{}@1+ (1,0) [0|{}] "V" Vector__XXX\n'.format(first_start, num_mul))

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

if (GEN_CHIP_VOLTAGES):
    #Voltages
    f = open("chip_voltages.txt", "w").close()
    f = open("chip_voltages.txt", "w")

    length = 13
    seg = 0
    mul = 0
    first_start = 2
    start = first_start

    one_mul = math.floor((64 - first_start) / length); # Number of signals that can fit in one message
    num_mul = math.ceil((chips * segments) / one_mul) - 1;  # Total number of multiplexed messages needed
    f.write(' SG_ BMS_Chip_Voltages_mux M : 0|{}@1+ (1,0) [0|{}] "V" Vector__XXX\n'.format(first_start, num_mul))

    for i in range(chips * segments):
        letter = chr(65 + seg) 
        seg_num = letter + str((i % chips))
        
        if (start + length > 63):
            start = first_start
            mul += 1

        if (i % chips == chips - 1):
            seg +=1

        f.write(' SG_ BMS_Chip_Voltages_{} m{} : {}|{}@1+ (0.01,0) [0|81.92] "V" Vector__XXX\n'.format(seg_num, mul, start, length))
        start += length
    f.close()

if (GEN_THERM_VOLTAGES):
    # Thermistor Voltages
    f = open("therm_voltages.txt", "w").close()
    f = open("therm_voltages.txt", "w")

    length = 9
    seg = 0
    mul = 0
    first_start = 3
    start = first_start

    one_mul = math.floor((64 - first_start) / length); # Number of signals that can fit in one message
    num_mul = math.ceil((therms * segments) / one_mul) - 1;  # Total number of multiplexed messages needed
    f.write(' SG_ BMS_Thermistor_Voltages_mux M : 0|{}@1+ (1,0) [0|{}] "V" Vector__XXX\n'.format(first_start, num_mul))

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

if (GEN_TEMPS):
    #Temps
    f = open("temps.txt", "w").close()
    f = open("temps.txt", "w")

    length = 10
    seg = 0
    mul = 0
    first_start = 3
    start = first_start


    one_mul = math.floor((64 - first_start) / length); # Number of signals that can fit in one message
    num_mul = math.ceil((therms * segments) / one_mul) - 1;  # Total number of multiplexed messages needed
    f.write(' SG_ BMS_Temperatures_mux M : 0|{}@1+ (1,0) [0|{}] "V" Vector__XXX\n'.format(first_start, num_mul))

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

if (GEN_DRAIN_STATUS):
    # Drain Status
    f = open("drain_status.txt", "w").close()
    f = open("drain_status.txt", "w")

    length = 1
    seg = 0
    mul = 0
    first_start = 3
    start = first_start

    one_mul = math.floor((64 - first_start) / length); # Number of signals that can fit in one message
    num_mul = math.ceil((cells * segments) / one_mul) - 1;  # Total number of multiplexed messages needed
    f.write(' SG_ BMS_Temperatures_mux M : 0|{}@1+ (1,0) [0|{}] "V" Vector__XXX\n'.format(first_start, num_mul))

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
