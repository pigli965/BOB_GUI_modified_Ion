
import smbus  
import sys 

bus=smbus.SMBus(1)


#define multiplexor 0x70 --> address 
multiplexor_address = 0x70

i2c_ch_0=0b00000001
i2c_ch_1=0b00000010
i2c_ch_2=0b00000011
i2c_ch_3=0b00000100
i2c_ch_4=0b00000101


bus.write_byte(multiplexor_address,i2c_ch_0) #--> select output from multiplexor 

# 
# #MCP23017 define config1
# extender_address1 = 0x20
# 
# reg_portA1 = 0x00 # default register for PortA to config GPIO
# value_portA1 = 0x00
# 
# reg_portB1 = 0x01 # default register for PortB to config GPIO
# value_portB1 = 0x00
# 
# #init commands 
# write_byte_data(extender_address1,reg_portA1,value_portA1)
# bus.write_byte_data(extender_address1,reg_portB1,value_portB1)
# 
# 
# #MCP23017 define config2
# extender_address2 = 0x21
# 
# reg_portA2 = 0x00 # default register for PortA to config GPIO
# value_portA2 = 0x00
# 
# reg_portB2 = 0x01 # default register for PortB to config GPIO
# value_portB2 = 0x00
# 
# #init commands 
# bus.write_byte_data(extender_address2,reg_portA2,value_portA2)
# bus.write_byte_data(extender_address2,reg_portB2,value_portB2)
# 
# 
# #MCP23017 define config3
# extender_address3 = 0x22
# 
# reg_portA3 = 0x00 # default register for PortA to config GPIO
# value_portA3 = 0x00
# 
# reg_portB3 = 0x01 # default register for PortB to config GPIO
# value_portB3 = 0x00
# 
# #init commands 
# bus.write_byte_data(extender_address3,reg_portA3,value_portA3)
# bus.write_byte_data(extender_address3,reg_portB3,value_portB3)
# 
# #MCP23017 define config4
# extender_address4 = 0x23
# 
# reg_portA4 = 0x00 # default register for PortA to config GPIO
# value_portA4 = 0x00
# 
# reg_portB4 = 0x01 # default register for PortB to config GPIO
# value_portB4 = 0x00
# 
# #init commands 
# bus.write_byte_data(extender_address4,reg_portA4,value_portA4)
# bus.write_byte_data(extender_address4,reg_portB4,value_portB4)
# 
# 
# #MCP23017 define config5
# extender_address5 = 0x24
# 
# reg_portA5 = 0x00 # default register for PortA to config GPIO
# value_portA5 = 0x00
# 
# reg_portB5 = 0x01 # default register for PortB to config GPIO
# value_portB5 = 0x00
# 
# #init commands 
# bus_write_byte_data(extender_address5,reg_portA5,value_portA5)
# bus_write_byte_data(extender_address5,reg_portB5,value_portB5)
# 
# 
# #MCP23017 define config6
# extender_address6 = 0x25
# 
# reg_portA6 = 0x00 # default register for PortA to config GPIO
# value_portA6 = 0x00
# 
# reg_portB6 = 0x01 # default register for PortB to config GPIO
# value_portB6 = 0x00
# 
# #init commands 
# bus_write_byte_data(extender_address6,reg_portA6,value_portA6)
# bus_write_byte_data(extender_address6,reg_portB6,value_portB6)
# 

#MCP23017 define config7
extender_address7 = 0x26

reg_portA7 = 0x00 # default register for PortA to config GPIO
value_portA7 = 0x00

reg_portB7 = 0x01 # default register for PortB to config GPIO
value_portB7 = 0x00

#init commands 
bus.write_byte_data(extender_address7,reg_portA7,value_portA7)
bus.write_byte_data(extender_address7,reg_portB7,value_portB7)

# 
# #MCP23017 define config8
# extender_address8 = 0x27
# 
# reg_portA8 = 0x00 # default register for PortA to config GPIO
# value_portA8 = 0x00
# 
# reg_portB8 = 0x01 # default register for PortB to config GPIO
# value_portB8 = 0x00
# 
# #init commands 
# bus_write_byte_data(extender_address8,reg_portA8,value_portA8)
# bus_write_byte_data(extender_address8,reg_portB8,value_portB8)
# 


def board1_Write(x,y):
    bus.write_byte_data(extender_address7,0x12, x)
    bus.write_byte_data(extender_address7,0x13, y)

