import boto3
from keys import ACCESS_KEY, SECRET_KEY

bucket_name = "bucket-actividades"

def connectionS3():
    session_aws = boto3.Session(
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY
    )
    session_s3 = session_aws.resource('s3')
    return session_s3

def get_image_url(activity_name):
    session_s3 = connectionS3()
    bucket_location = session_s3.meta.client.get_bucket_location(Bucket=bucket_name)
    region = bucket_location['LocationConstraint']
    image_url = f"https://{bucket_name}.s3.{region}.amazonaws.com/imagenes/{activity_name}.jpg"
    return image_url

def get_file(session_s3):    
    bucket_project = session_s3.Bucket(bucket_name)
    bucket_objects = bucket_project.objects.all()
    for obj in bucket_objects:
        print(obj.key)
    print(bucket_objects)

def save_file(activity, image):
    extension = image.filename.split(".")[-1]
    image_name = f"{activity}.{extension}"
    image_path = f"/tmp/{image_name}"
    image.save(image_path)
    print("Imagen guardada")
    return image_path, image_name

def upload_file_s3(session_s3, image_path, image_name):
    path_image_local = f"imagenes/{image_name}"
    session_s3.meta.client.upload_file(image_path, bucket_name, path_image_local)
    print("Imagen subida")

    