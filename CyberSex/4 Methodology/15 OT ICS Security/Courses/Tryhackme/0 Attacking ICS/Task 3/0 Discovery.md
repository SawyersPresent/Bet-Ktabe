
Connect to the plant using the browser ([http://MACHINE_IP](http://machine_ip/)) and learn how the bottle-filling plant works.

We have three phases:

1. Initialization: the plant is starting from the beginning. The roller moves the first bottle under the nozzle.
2. Filling: once a bottle is under the nozzle, the nozzle opens and the water flows in the bottle.
3. Moving: once the bottle is filled, the roller starts again moving the next empty bottle under the nozzle.


When the phase 3 ends, the plant starts again with phase 2.

From the three phases described above, we can observe:

- Sensors: used to read a state of the plant.
    
- Actuators: used to alter the state of the plant.
    

Example: a sensor can detect if a bottle is under the nozzle, while an actuator can open or close the nozzle.

Mind we can press the ESC button to start the plant from the beginning.

VirtuaPlant can be downloaded from [GitHub](https://github.com/jseidl/virtuaplant/network/members).