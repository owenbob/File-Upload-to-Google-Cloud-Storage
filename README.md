# File-Upload-to-Google-Cloud-Storage

## Specifications
- A simple flask API that uploads an image to google cloud storage  and lists all uploaded images.
    -   `Upload` end point 
    ```
    YOUR_SERVER_URL/api/v1/upload/
    ```
    -  `List` end point 
    ```
    YOUR_SERVER_URL/api/v1/list/
    ```
## Installation
First clone this repository
```
$ git clone https://github.com/owenbob/File-Upload-to-Google-Cloud-Storage.git
```
Create virtual environment and install it
```
$ virtualenv env
$ source/env/bin/activate
```
Then install all the necessary dependencies
```
pip install -r requirements.txt
```
## Run the application
At the terminal or console type
```
python app.py
```
To run tests run this command at the console/terminal
```
pytest tests.py
```
## Test locally
```
To test using  CURL or POSTMAN (a google chrome extention)
```
#### Python Version Used
```
Python 3.6
```
