from flask import Flask, request, jsonify, make_response
import logging
import boto3
import json
from config import config

app = Flask(__name__)
logging.basicConfig(
    filename=config['log_file'], 
    level=config['log_level']
)
@app.route('/ec2/list', methods=['GET'])
def ec2_list():
    accessid = request.args.get("accessid")
    accesskey = request.args.get("accesskey")
    region = request.args.get("region")
    client = boto3.client('ec2',
        aws_access_key_id=accessid,
        aws_secret_access_key=accesskey,
        region_name=region
    )
    response = client.describe_instances(
    )
    InstanceIds = []
    for instance in response["Reservations"]:
            for i in instance["Instances"]:
                InstanceIds.append(i["InstanceId"]) 
    
    return make_response(jsonify(InstanceIds), 200)

@app.route('/ec2/start', methods=['POST'])
def ec2_start():
    json_data = request.get_json()
    json_try = json.dumps(json_data)
    json_json = json.loads(json_try)
    
    accessid = json_json['accessid']
    accesskey = json_json['accesskey']
    region = json_json['region']
    instid = json_json['instid']

    client = boto3.client('ec2',
        aws_access_key_id=accessid,
        aws_secret_access_key=accesskey,
        region_name=region
    )
    InstanceIds1 = []
    for i in instid[0]:
        InstanceIds1.append(instid)

    response = client.start_instances(
        InstanceIds=InstanceIds1,
    )
    print (response)
    return make_response(jsonify(response["StartingInstances"][0]), 200)

@app.route('/ec2/stop', methods=['GET'])
def ec2_stop():
    accessid = request.args.get("accessid")
    accesskey = request.args.get("accesskey")
    region = request.args.get("region")
    instid = request.args.get("instanceid")
    

    client = boto3.client('ec2',
        aws_access_key_id=accessid,
        aws_secret_access_key=accesskey,
        region_name=region
    )
    InstanceIds1 = []
    for i in instid[0]:
        InstanceIds1.append(instid)

    response = client.stop_instances(
        InstanceIds=InstanceIds1,
    )
#    print (response)
    return make_response(jsonify(response["StoppingInstances"][0]), 200)

if __name__ == "__main__":
    app.run(host=config["host"], port=config["port"], debug=True)
