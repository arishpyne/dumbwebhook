Dumbwebhook
===========
This is a super-simple webhook app that can be used to ease webhooks debugging

* Catches all paths
* Catches all HTTP methods (even non-existent ones) 
* Uses ngrok to automagically give you a fine globally accessible URL to point your Webhook producers at
* Decodes and pretty-prints the payload if it's in JSON format

Usage
-----
Download it from DockerHub:

    docker pull arishpyne/dumbwebhook
   
Or build it yourself:
   
    docker build -t dumbwebhook:latest .
    
Then run it:

    docker run -it arishpyne/dumbwebhook
    
