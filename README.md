# Flask API

This is A model deployed through a Flask API. The environment is created through a `docker-compose` command, that references the corresponding Dockerfile and requirements.txt file. 

First you will need to sync your repo to pull the new files. To run this API, change your directory to the docker folder and run:

`docker-compose up`

If it has created the localhost server correctly you will not get your prompt back. You will need to open a new terminal (be in the same directory) and run the following curl command to get a response

`curl http://localhost:5000/`



Pass predictor values through a json formatted input through a curl POST request to the API. Values are needed for "cyl", "disp", "hp", "drat", "wt", "qsec", and "vs." This is done as, for example,

`curl -H "Content-Type: application/json" -X POST -d '{"cyl":"6.0","disp":"258.0","hp":"110.0","drat":"2.93","wt":"5.25","qsec":"17.3", "vs":"1.0"}' "http://localhost:5000/predict"`

Both of the curl commands can be found in the file `curl_test.sh`. To stop your server running the API, type `ctrl-C`. As usual, check to see if you have any docker containers running using `docker container ls` and stop them through `docker container kill <container-name>`
