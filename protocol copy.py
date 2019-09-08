
from opentrons import robot, instruments, containers
from opentrons.util.vector import Vector
from time import sleep

robot.connect(robot.get_serial_ports_list()[0])
robot.home()
#robot.head_speed (4000)

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
		dispense_speed = 2000,
		tip_racks = rack[0],
		trash_container = trash[0]
)
# Define Custom Protocol
cycles = int(input('How many cycles would you like to run ? '))
delay_between_cylces = int(input('How much delay between a cycle (in seconds) ? '))

current_cycle = 0
while current_cycle < cycles:
	i = 0
	while i < 3:
		pipette.pick_up_tip(rack.wells(i))
		j = 0
		while j < 1:
			pipette.move_to((water[i], Vector(0, 0, 30))).aspirate(30)
			pipette.aspirate(50, water[i])
			pipette.aspirate(50, dish[i])
			pipette.dispense(200, samples[i].well(j)).blow_out()
			j = j + 1
		pipette.drop_tip(trash)
		i = i + 1
		print('Cycle #{} complt'.format(current_cycle))
		sleep(delay_between_cylces)

robot.home()

#pipette.transfer(100, samples_slots('A1'), samples_slots('B1'))
