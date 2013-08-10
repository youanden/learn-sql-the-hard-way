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
