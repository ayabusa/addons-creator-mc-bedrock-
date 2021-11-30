import os
import json

BPpath = input("enter the Path of the BP : ")+ "\\item"

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