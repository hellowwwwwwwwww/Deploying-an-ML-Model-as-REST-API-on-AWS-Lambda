I have successfully deployed a Machine Learning model as a fully functional REST API using AWS Lambda and API Gateway.

This project uses a lightweight Python-based ML model and exposes a /predict endpoint that accepts JSON input and returns a prediction.

🔹 Tech Used: Python, AWS Lambda, API Gateway  
🔹 Deployment: Serverless model inference  
🔹 Input/Output: JSON → Lambda → JSON  


✔ Example Request (POST)
URL:
https://356slpjhx9.execute-api.ap-southeast-2.amazonaws.com/prod/predict

Body:
{
  "features": [5.1, 3.5, 1.4, 0.2]
}

✔ Example Response
{
  "prediction": 0
}



Brief Instructions:

1. Write inference logic in `lambda_function.py`.
2. Zip only the function file (`lambda_code.zip`) and upload to AWS Lambda.
3. Set handler to `lambda_function.lambda_handler`.
4. Create REST API in API Gateway.
5. Add resource `/predict` and attach POST method.
6. Integrate Lambda with API Gateway.
7. Deploy to stage `prod` and test via cURL/Postman.

The API is live, tested successfully, and ready for evaluation.
