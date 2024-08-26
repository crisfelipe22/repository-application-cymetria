from boto3.session import Session
from keys import ACCESS_KEY, SECRET_KEY

def conecction_s3():
    session_aws = Session(ACCESS_KEY, SECRET_KEY)
    session_s3 = session_aws.resource("s3")
    print("Successfull connection to a s3")
    #print(session_s3)
    #for bucket in session_s3.buckets.all():
    #    print(bucket.name)
    return session_s3

def save_file(id, photo):
    extension = photo.filename.split(".")[1]
    photo_path = "/tmp/" + id + + "." + extension
    photo.save(photo_path)
    print("Save photo correctly")

def update_file(session_s3, photo, photo_path, id):
    bucket_name = "cymetria-aws-cristian"
    extension = photo.filename.split(".")[1]
    file_s3_path = "images/" + id + "." + extension
    session_s3.meta.client.update_file(photo_path, bucket_name, file_s3_path)
    print("Update file")