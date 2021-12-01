#!/bin/bash




curl -d "{ \"text\": [ \"I would like to punch you.\", \"In hindsight, I do apologize for my previous statement.\" ]}" -X POST "http://localhost:5000/model/predict" -H "Content-Type: application/json"

