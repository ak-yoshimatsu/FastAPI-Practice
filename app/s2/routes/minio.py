import boto3
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def confirm_minio():
    s3 = boto3.client(  # pyright: ignore[reportUnknownMemberType]
        "s3",
        endpoint_url="http://minio:9000",
        aws_access_key_id="rootroot",
        aws_secret_access_key="secretsecret",
    )

    response = s3.list_buckets()
    print(response["Buckets"])

    s3.create_bucket(Bucket="from-boto-fastapi-2")

    response = s3.list_buckets()
    print(response["Buckets"])
    return {"buckets": response["Buckets"]}
