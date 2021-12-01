#!/bin/bash

# Change this to just docker if you dont want to run sudo everytime
DOCKER='sudo docker'


if [ -d "./MAX-Toxic-Comment-Classifier" ]
then
	echo "MAX-Toxic-Comment-Classifier folder already exists"
else
	echo "cloning MAX-Toxic-Comment-Classifier"

	git clone https://github.com/IBM/MAX-Toxic-Comment-Classifier.git
fi


cd MAX-Toxic-Comment-Classifier


echo "Running docker build with sudo because ubuntu is stupid"

$DOCKER build -t max-toxic-comment-classifier .


echo "Running classifier on port 5000"

$DOCKER run -it -p 5002:5000 max-toxic-comment-classifier

