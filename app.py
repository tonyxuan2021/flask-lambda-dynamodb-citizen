from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import boto3
import json
import logging

app = Flask(__name__)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
dynamodb = boto3.resource(
    "dynamodb",
    region_name="us-west-1",
    endpoint_url="https://dynamodb.us-west-1.amazonaws.com",
)
table = dynamodb.Table("citizens")
logger.info("Connected to DynamoDB..")


@app.route("/getcitizens")
@cross_origin()
def get_citizens():
    response = table.scan()["Items"]
    logger.info("All citizens returned")
    return jsonify(response)
