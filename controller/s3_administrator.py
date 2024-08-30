import os
from boto3.session import Session
from keys import ACCESS_KEY, SECRET_KEY

def conection_s3():
    session_aws = Session(ACCESS_KEY, SECRET_KEY)
    session_s3 = session_aws.resource("s3")
    print("Successfull connection to a s3")
    #print(session_s3)
    #for bucket in session_s3.buckets.all():
    #    print(bucket.name)
    return session_s3

def save_file(id, photo):
    # for windows
    # directory = "C:/temp/"
    # os.makedirs(directory, exist_ok=True)  # Crea el directorio si no existe
    
    extension = photo.filename.split(".")[1]
    # photo_path = os.path.join(directory, f"{id}.{extension}")
    photo_path = "/tmp/" + id + "." + extension # for linux
    photo.save(photo_path)
    print("Photo saved")
    return photo_path

def update_file(session_s3, photo, photo_path, id):
    bucket_name = "bucket-cristian-ovalles-cymetria"
    extension = photo.filename.split(".")[1]
    file_s3_path = "images/" + id + "." + extension
    session_s3.meta.client.upload_file(photo_path, bucket_name, file_s3_path)
    print("Update file")