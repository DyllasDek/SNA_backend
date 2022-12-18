db = connect('mongodb://pl:pl@mongo_db:27017/game');

use game;

db.createUser( { user: "pl", pwd: "pl", roles: [{ role: "readWrite", db: "game" }] });

db.init.insert.({0:0})
