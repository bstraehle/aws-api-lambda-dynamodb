# Serverless microservice using API Gateway, Lambda, and DynamoDB  

Enter TableName and deploy  

URL:  
```
<endpoint>
```

Tests:
```
curl --location --request GET '<endpoint>'
```
```
curl --location --request POST '<endpoint>' \
--header 'Content-Type: application/json' \
--data-raw '{
	"Item": {
		"id": {
			"S": "test"
		}
	}
}'
```
```
curl --location --request DELETE '<endpoint>' \
--header 'Content-Type: application/json' \
--data-raw '{
	"Key": {
		"id": {
			"S": "test"
		}
	}
}'
```

Tear down:  

- Go to CloudFormation and delete stack  
- Go to CloudWatch, log groups, select log group and delete  

Source: https://github.com/bstraehle/aws-api-lambda-dynamodb  
