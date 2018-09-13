import os
from flask import Flask,request,jsonify
from google_cloud_storage import upload_blob, list_blobs

app = Flask(__name__)

@app.route("/api/vi/upload/", methods=["POST"])
def upload():
    image = request.files["image"]
    
    bucket_name = os.getenv("BUCKET_NAME")
    destination_blob_name ="Sample Image" 
    result = upload_blob(
        bucket_name,
        image,
        destination_blob_name
        )
    
    return jsonify({
        "Message":result

    }),200

@app.route("/api/vi/list/", methods=["GET"])
def list_uploads():
    bucket_name = os.getenv("BUCKET_NAME")
    result = list_blobs(bucket_name)
    
    return jsonify({
        "Results" : result,
        "Message" :" Uploaded blobs"
    }),200


if __name__ == "__main__":
    app.run(debug=True)