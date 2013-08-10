CREATE TABLE server (
	id INTEGER PRIMARY KEY,
	build_date DATE,
	hostname TEXT,
	cpu TEXT,
	gpu TEXT,
	ram INTEGER,
	hdd INTEGER
);

CREATE TABLE service (
	id INTEGER PRIMARY KEY,
	name TEXT,
	port INTEGER
);

CREATE TABLE server_service (
	server_id INTEGER,
	service_id INTEGER
);

INSERT INTO server (build_date, hostname, cpu, gpu, ram, hdd)
VALUES ("2013-08-05", "local.youanden.me", "i7 920", "Nvidia GTX 550 Ti", 5939, 978);

INSERT INTO service (name, port)
VALUES	("mysql", 3306),
	("nginx", 80),
	("rails", 3000),
	("ssh", 20);

INSERT INTO server_service (server_id, service_id)
VALUES 	(0, 0),
	(0, 1),
	(0, 2),
	(0, 3);

