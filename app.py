import os
from flask import Flask,request,jsonify
from google_cloud_storage import upload_blob, list_blobs
from werkzeug.utils import secure_filename

app = Flask(__name__)



@app.route("/api/v1/upload/", methods=["POST"])
def upload():
    """
    This route deals with uploading images to a google cloud storage bucket
    - Content-Type --> multipart/form-data
    For more information checkout https://cloud.google.com/storage/docs/
    """
    image = request.files["image"]

    # BUCKET_NAME - the bucket created in the google cloud service
    # This can be created manually or working with code 
    # Checkout - https://cloud.google.com/storage/docs/creating-buckets

    bucket_name = os.getenv("BUCKET_NAME")

    # Ideally a destination_blob_name should be a name assigned to every image uploaded. 
    # This can be simply getting the filename or seeting a name value on the client side
    # Destination_blob_name is the name saved in the cloud for the uploaded image
    destination_blob_name ="Sample Image2" 
    filename = secure_filename(image.filename)
    
    result = upload_blob(
        bucket_name,
        filename,
        destination_blob_name
        )
    
    return jsonify({
        "Message":result[0],
        "Url":result[1]
    }),200

@app.route("/api/v1/list/", methods=["GET"])
def list_uploads():
    """
    This route deals with listing blobs and files images uploaded to
    the google cloud service
    """
    bucket_name = os.getenv("BUCKET_NAME")
    
    result = list_blobs(bucket_name)
    
    return jsonify({
        "Results" : result,
        "Message" :" Uploaded blobs"
    }),200

if __name__ == "__main__":
    app.run(debug=True)