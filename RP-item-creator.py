import os
import json

RPpath = str(input("Enter the Path of the RP : "))

itemName = str(input("enter the item name (myItem) : "))
fileName = str(input("enter the file name (myItem.json) : "))
itemIdentifer = str(input("enter the Identifer of the item (wiki:myItem) : "))
iconIdentifer = str(input("enter the Identifer of the Icon (wiki.myItem) : "))

itemPath = os.path.join(RPpath + "\\items",fileName)
texturePath = os.path.join(RPpath + "\\textures","item_texture.json")

itemJson = {
    			"format_version": "1.10",
    			"minecraft:item": {
      				"description": {
        				"identifier": itemIdentifer,
        				"category": "Items"
      				},
      				"components": {
        			"minecraft:icon": iconIdentifer
      				}
    			}
 			}


item_json_object = json.dumps(itemJson, indent = 4)

with open(itemPath, "w") as outfile:
    outfile.write(item_json_object)

file = open(texturePath, "r+")
#itemTextureJson = file.read()
item_texture_json_object = json.load(file)
newItemTexture = {iconIdentifer: {
          			"textures": "textures/items/"+itemName
       			}}
item_texture_json_object["texture_data"].update(newItemTexture)
item_json_object = json.dumps(item_texture_json_object, indent = 4)
file.write(item_texture_json_object)
#print(item_texture_json_object)
