import os
import json

<<<<<<< HEAD
false = False
true = True
=======
BPpath = input("enter the Path of the BP : ")+ "\\item"
>>>>>>> 6b169ada0d3ea4b80a191ccea9114573dcc3f7fc

def item():
	BPpath = input("enter the Path of the BP : ")+ "\item"
	fileName = str(input("enter the file name (myItem.json) : "))
	itemIdentifer = str(input("enter the Identifer of the item (wiki:myItem) : "))
	maxStackSize = int(input("enter the max stack size (64, 32, 16) : "))

	filePath = os.path.join(BPpath, fileName)

	itemjson = {
					"format_version": "1.10",
					"minecraft:item": {
						"description": {
							"identifier": itemIdentifer
						},
						"components": {
							"minecraft:max_stack_size": maxStackSize
						}
					}
				}

	# Serializing json 
	json_object = json.dumps(itemjson, indent = 4)
	  
	# Writing to sample.json
	with open(filePath, "w") as outfile:
	    outfile.write(json_object)

def block():

	BPpath = input("enter the Path of the BP : ")+ "\\blocks"
	if(os.path.exists(BPpath) == False):
		os.mkdir(BPpath)


	fileName = str(input("enter the file name (myBlock.json) : "))
	blockIdentifer = str(input("enter the Identifer of the block (wiki:myBlock) : "))
	destroy_time = int(input("enter the destroy_time (1, 5, ...) : "))
	explosion_resistance = int(input("enter the explosion_resistance (5, 10, ...) : "))
	map_color = str(input("enter the map color of the block (#FFFFFF) : "))

	filePath = os.path.join(BPpath, fileName)


	blockJson = {
    				"format_version": "1.17.30",
    				"minecraft:block": {
        				"description": {
            				"identifier": blockIdentifer,
            				"is_experimental": false,
            				"register_to_creative_menu": true
        				},  
        				"components": {
            				"minecraft:destroy_time": destroy_time,
            				"minecraft:explosion_resistance": explosion_resistance,
            				"minecraft:friction": 0.6,
            				"minecraft:flammable": {
                				"flame_odds": 0,
                				"burn_odds": 0
            				},
            				"minecraft:map_color": map_color,
            				"minecraft:block_light_absorption": 0,
            				"minecraft:block_light_emission": 0.250
        				}
    				}
				}


	# Serializing json 
	json_object = json.dumps(blockJson, indent = 4)

	# Writing to sample.json
	with open(filePath, "w") as outfile:
	    outfile.write(json_object)

Mode = int(input("what mode do you want ?\n [1] Item \n [2] Block \n [3] Exit \nMode : "))
if(Mode == 1):
	item()
elif(Mode == 2):
	block()
