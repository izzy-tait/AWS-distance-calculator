# AWS-distance-calculator
An End-to-End Web App using AWS.
This application uses 5 AWS services: Amplify, Lambda, API Gateway, DynamoDB, and IAM. 
This distance calculator app was hosted on Amplify. When the user submits their input, an endpoint (hosted on API Gateway) is called. That endpoint then calls a Lambda function; the code for this is stored in the python file. This Lambda function inserts the calculated value in a table hosted on DynamoDB. AN IAM inline policy gives the Lambda function permission to write/read to the database. The endpoint's response, the calculated distance, is displayed on the UI. 
