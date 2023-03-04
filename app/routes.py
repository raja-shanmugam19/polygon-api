from app import app, collection
from flask import request, jsonify
from bson import json_util
import json

@app.route("/savepolygons", methods=["POST"])
def save_polyogns():
    payload = request.json["body"]
    payload_dict = json.loads(payload)
    polygon_name = payload_dict["polygonName"]
    additional_info = payload_dict["additionalInfo"]
    points = payload_dict["points"]

    existing_polygon = collection.find_one({"polygonName": polygon_name})
    if existing_polygon:
        update_result = collection.update_one({"polygonName": polygon_name}, 
                                              {"$set": {"additionalInfo": additional_info, 
                                                        "points": points}})
        return jsonify({"message": f"Polygon '{polygon_name}' updated successfully"})
    else:
        document = {
            "polygonName": polygon_name, 
            "additionalInfo": additional_info, 
            "points": points
        }
        result = collection.insert_one(document)
        return jsonify({"message": f"Polygon '{polygon_name}' created successfully"})

@app.route("/polygons", methods=["GET"])
def get_polygons():
    print('calling')
    data = list(collection.find())
    json_data = json.loads(json_util.dumps(data))
    return jsonify(json_data)
