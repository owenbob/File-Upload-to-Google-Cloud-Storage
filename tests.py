import os
from unittest import TestCase
from app import app
from io import BytesIO

#Ideally a test bucket should be set up and cleared when ever the tests are done running


class FileUploadTestcase(TestCase):
 
    client = app.test_client()
    image =(BytesIO(b'test'), 'download.jpeg')
    data = {
        "image":image
    }

    def test_upload(self):
        
        response = self.client.post(
            "/api/v1/upload/",
             content_type='multipart/form-data',
             data=self.data
        )
        resp = response.data.decode("utf-8")
        msg = "File download.jpeg uploaded to Sample Image2."
        self.assertIn(msg, resp)
        self.assertEqual(response.status_code,200)

    def test_list_upload(self):
        response = self.client.get("/api/v1/list/")
        resp = response.data.decode("utf-8")

        self.assertIn("Results", resp)
        self.assertEqual(response.status_code,200)
