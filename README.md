Clone repo:  
```
git clone https://github.com/bstraehle/aws-api-lambda-dynamodb.git
cd aws-api-lambda-dynamodb
```

Create S3 bucket:  
```
aws s3 mb s3://<bucket>
```

Update policy.json and add account and bucket info  

Allow read from bucket:  
```
aws s3api put-bucket-policy --bucket <bucket> --policy file://policy.json
```

Package application:  
```
sam package --template-file template.yaml --output-template-file packaged.yaml --s3-bucket <bucket>
```

Publish application:  
```
sam publish --template packaged.yaml --region <region>
```

Login to the AWS Console and deploy application  

URL:  
```
<endpoint>
```

Tear down:  

- Go to CloudFormation and delete application stack  
- Go to CloudWatch, log groups, select log group and delete  
- Go to S3 and delete bucket  
