import json

WEIGHTS = [
    [0.5, -0.2, 0.3, -0.1],
    [-0.3, 0.4, -0.1, 0.2],
    [-0.2, -0.1, 0.2, 0.3]
]

BIAS = [0.1, -0.2, 0.3]

def predict(features):
    scores = []
    for w, b in zip(WEIGHTS, BIAS):
        score = sum(f * wi for f, wi in zip(features, w)) + b
        scores.append(score)
    return scores.index(max(scores))

def lambda_handler(event, context):
    try:
        
        if "body" in event:
            body = json.loads(event["body"])
        else:
            body = event  

        features = body["features"]
        pred = predict(features)

        return {
            "statusCode": 200,
            "body": json.dumps({"prediction": pred})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
