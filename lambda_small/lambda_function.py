import json
import joblib
import os


model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(model_path)

def lambda_handler(event, context):
    try:
        
        body = json.loads(event["body"])
        features = body["features"]  

        
        prediction = model.predict([features])[0]

        return {
            "statusCode": 200,
            "body": json.dumps({
                "prediction": int(prediction)
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }
