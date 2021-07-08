Program files support an API endpoint for the Easy, Medium, and Hard code challenges

After cloning the repo to a docker host, run the following commands from the folder that the files were cloned into.

1. docker build -t myapp .
2. docker run -d -p 8000:80 myapp
3. From your web browser, go to http://localhost/docs
4. Try out the three API endpoints and their functionality
    - use your cisco devnet username and password in the open fields by the same name
