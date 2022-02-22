# Serverless microservice using API Gateway, Lambda, and DynamoDB  

Start up:  

- Deploy application, specifying table name  

Tests:  

```
curl --location --request GET '<endpoint>'
curl --location --request POST '<endpoint>' \
	--header 'Content-Type: application/json' \s
	--data-raw '{
		"Item": {
			"id": {
				"S": "test"
			}
		}
	}'
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

- Go to CloudFormation and delete application stack  
- Go to CloudWatch, log groups, log group and delete  
