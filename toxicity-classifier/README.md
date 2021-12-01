# Toxicity Classifier


Get docker started by running `./start-container.sh`

Test it by typing `python3 toxicity-analyzer.py toxicity-analyzer-test.json`


## Request

```json
{
    "repo": "hus888yu/ma",
    "text": [
        "Delete 0002.json"
    ]
}
```


## Response

```json
[
    {
        "repo": "hus888yu/ma",
        "response": {
            "status": "ok",
            "results": [
                {
                    "original_text": "Delete 0002.json",
                    "predictions": {
                        "toxic": 0.00029842500225640833,
                        "severe_toxic": 0.0001148586452472955,
                        "obscene": 0.00015467633784282953,
                        "threat": 8.211508247768506e-05,
                        "insult": 0.00016002313350327313,
                        "identity_hate": 0.0001240108977071941
                    }
                }
            ]
        }
    }
]
```