# Server and backend for SNA project

## Setup

You will need to create proper directory for database first and initialize everything.

```
mkdir DB
```

After running docker, you need to start ```init.js``` in ```mongosh```. ```init.js``` is a simple script that initializes mongo database:

mongosh --host localhost --port 27017 -u root -p rootpassword --file init.js


