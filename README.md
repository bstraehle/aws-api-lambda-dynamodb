<a href="https://aws.amazon.com/cli/">Install AWS CLI</a>  (alternatively, use CloudShell)  

<a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html">Install AWS SAM CLI</a> (alternatively, use CloudShell)  

Initialize application (1, 1, enter, 1)  
```
sam init --runtime python3.9
```

Create files lambda_function.py, policy.json, and template.yaml  

Create S3 bucket  
```
aws s3 mb s3://<bucket>
```

Allow read from bucket  
```
aws s3api put-bucket-policy --bucket <bucket> --policy file://policy.json
```

Package application  
```
sam package --template-file template.yaml --output-template-file packaged.yaml --s3-bucket <bucket>
```

Publish application  
```
sam publish --template packaged.yaml --region <region>
```

Login to the AWS Console and deploy application  

Tear down:  

- Go to CloudFormation and delete application stack  
- Go to CloudWatch, log groups, select log group and delete  
- Go to S3 and delete bucket  
