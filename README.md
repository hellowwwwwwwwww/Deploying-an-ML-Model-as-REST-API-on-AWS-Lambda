Deploying a Machine Learning Model as a REST API on AWS Lambda

This project demonstrates how to deploy a Machine Learning model using AWS Lambda and API Gateway, creating a fully serverless, scalable, and cost-efficient REST API for real-time predictions.

# Project Overview

A simple Iris classifier model was trained locally using Python and scikit-learn, serialized as model.pkl, and deployed to AWS Lambda.
An API Gateway endpoint was created to expose the Lambda function as a REST API that accepts feature inputs and returns the predicted class.

This setup avoids EC2 servers and uses pay-per-use serverless architecture.

 # Tech Stack

Python 3.10

scikit-learn (for ML model)

AWS Lambda (model inference)

AWS API Gateway (REST endpoint)

cURL / Postman for testing

JSON for input/output

# Repository Structure


ml_lambda_project/
│
├── lambda_function.py       # AWS Lambda handler (main inference code)
├── train_model.py           # Script to train and save the ML model (model.pkl)
├── model.pkl                # Trained ML model (lightweight)
├── requirements.txt         # Local development dependencies
│
├── README.md                # Project documentation
│
├── (Optional / Auto-generated AWS files)
│
├── deployment.zip           # Auto-generated Lambda deployment package
├── lambda_code.zip          # Auto-generated minimal Lambda package
├── sklearn_layer/           # AWS Lambda Layer (large dependencies like numpy, sklearn)
├── lambda_small/            # Additional AWS layer (generated during deployment)

Only the lightweight files are uploaded.
Heavy layer dependencies (NumPy, SciPy, scikit-learn) are attached using AWS Lambda Layers.

 # Live API Endpoint

Your deployed ML model can be accessed here:

 # POST

https://356slpjhx9.execute-api.ap-southeast-2.amazonaws.com/prod/predict

# Example Request
POST Request Body
{
  "features": [5.1, 3.5, 1.4, 0.2]
}

Example cURL Request
curl -X POST \
  -H "Content-Type: application/json" \
  -d "{\"features\": [5.1, 3.5, 1.4, 0.2]}" \
  https://356slpjhx9.execute-api.ap-southeast-2.amazonaws.com/prod/predict

Example Response
{
  "statusCode": 200,
  "body": "{\"prediction\": 0}"
}

# How It Works

Client sends a POST request with feature values

API Gateway forwards request to AWS Lambda

Lambda loads the model.pkl

Model performs prediction

Response is sent back as JSON

This architecture is serverless, scalable, and low-cost.

# Instructions to Reproduce Locally
1️.Train the model
python train_model.py

2️.Prepare Lambda deployment package

Add lambda_function.py

Add model.pkl

Zip the files

3️.Upload to AWS Lambda

Set runtime to Python 3.10

4️.Attach AWS Lambda Layer

(Contains numpy, pandas, sklearn)

5️.Create API Gateway → POST → /predict

Integrate with Lambda

6️⃣ Deploy API and test
