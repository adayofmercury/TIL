# 파일 업로드 및 다운로드


###### 210928 한이음 프로젝트 중 S3 사용부분

* S3 설정은 모르겠어서 일단 public 으로 전부 체크 풀고 진행함

``` python
import boto3
from botocore.client import Config

ACCESS_KEY_ID = '####' #s3 관련 권한을 가진 IAM계정 정보
ACCESS_SECRET_KEY = '####'
BUCKET_NAME = '####'


def handle_upload_csv(f): # f = 파일명
    data = open(f, 'rb')
    # '로컬의 해당파일경로'+ 파일명 + 확장자
    s3 = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        config=Config(signature_version='s3v4')
    )
    s3.Bucket(BUCKET_NAME).put_object(Key=f, Body=data, ContentType='text/csv')

    
def handle_download_csv(f) :
    s3 = boto3.client(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        config=Config(signature_version='s3v4')
    )
    s3.download_file(BUCKET_NAME, f, "down_file.csv")

```

버킷 정책

``` json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "StatementSid1",
            "Effect": "Allow",
            "Principal": {
                "AWS": "{user_arn}"
            },
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject"
            ],
            "Resource": "arn:aws:s3:::{bucket_name}/*"
        },
        {
            "Sid": "StatementSid2",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::{bucket_name}/*"
        }
    ]
}
```
