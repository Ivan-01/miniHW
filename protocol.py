from opentrons import robot, instruments, containers
from opentrons.util.vector import Vector
from time import sleep
import matplotlib.pyplot as plt
import numpy as np
from sys import exit

robot.connect(robot.get_serial_ports_list()[0])
robot.home()
robot.head_speed (20000)

# Define map

pipette_slots = ['A3',]
water_slots = ['B3', 'C3', 'D3']
dish_slots = ['B2', 'C2', 'D2']
samples_slots = ['B1', 'C1', 'D1']
trash_slots = ['A1',]

# Define containers

rack = containers.load('tiprack-200ul', pipette_slots[0])
water = []
for slot in water_slots:
	water.append(containers.load('point', slot))
dish = []
for slot in dish_slots:
	dish.append(containers.load('point', slot))
samples = []
for slot in samples_slots:
	samples.append(containers.load('96-PCR-flat', slot))
trash = containers.load('point', trash_slots[0])

# Define Instruments
pipette = instruments.Pipette(
		axis='b',
		name = 'p200_Single',
		channels = 1,
		min_volume=0,
		max_volume=200,
		aspirate_speed = 300,
		dispense_speed = 1000,
		tip_racks = rack[0],
		trash_container = trash[0]
)
# Define Custom Protocol
i = 0 
rad = 41.5
num = 96 
t = np.random.uniform(0.0, 2.0*np.pi, num)
r = rad * np.sqrt(np.random.uniform(0.0, 1.0, num))
x = r * np.cos(t)
y = r*np.sin(t)

while i < 3:
	pipette.pick_up_tip(rack.wells(i))
	j = 0
	for x1, y1 in zip(x, y):

		pipette.move_to(( water[i], Vector( 0, 0, 30 ) ), 'arc' ).aspirate( 20 )
		pipette.aspirate( 50 , water[i] )
		pipette.move_to(( water[i], Vector( 0, 0, 30 ) ), 'arc' ).aspirate( 20 )
		pipette.aspirate( 50 , water[i] )

#		pipette.move_to( (dish[i], Vector(0,0,0))).aspirate(50)
#		pipette.move_to( (dish[i], Vector(42,0,0)))
#		pipette.move_to( (dish[i], Vector(-42,0,0)))
#		pipette.move_to( (dish[i], Vector(0,42,0)))
#		pipette.move_to( (dish[i], Vector(0,-42,0)))
		pipette.move_to( ( dish[i], Vector(x1, y1, 0))).aspirate(60)

		pipette.move_to( ( dish[i], Vector( x1 + 2 , y1       , 0 ) ), 'direct' )
		pipette.move_to( ( dish[i], Vector( x1 - 2 , y1       , 0 ) ), 'direct' )
		pipette.move_to( ( dish[i], Vector( x1       , y1       , 0 ) ), 'direct' )
		pipette.move_to( ( dish[i], Vector( x1       , y1 + 2 , 0 ) ), 'direct' )
		pipette.move_to( ( dish[i], Vector( x1       , y1 - 2 , 0 ) ), 'direct' )

		pipette.dispense( 500, samples[i].well(j)).blow_out()
		j += 1

	pipette.drop_tip(trash)
	i = i + 1

#pipette.transfer(100, samples_slots('A1'), samples_slots('B1'))
