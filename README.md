# sam-app

## Usage

```
pip install boto3 -t lambda_function/
sam package --output-template-file packaged.yaml --s3-bucket csv-logger-test
sam deploy --template-file packaged.yaml --stack-name csv-logger --capabilities CAPABILITY_IAM
sam delete --stack-name csv-logger
```