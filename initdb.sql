DROP TABLE users;
DROP TABLE passwords;

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    login text NOT NULL,
    money_amount INTEGER NOT NULL,
    card_number text NOT NULL,
    status BOOLEAN NOT NULL
);


CREATE TABLE passwords (
    id INTEGER PRIMARY KEY,
    password text NOT NULL
);

INSERT INTO users VALUES (0, 'admin', 382074, '5297737737668887', 1);
INSERT INTO users VALUES (1, 'kek', 528497, '5245166660275903', 1);
INSERT INTO users VALUES (2, 'kekkek', 744298, '5420860372300796', 1);
INSERT INTO users VALUES (3, 'login', 847430, '5352051298937083', 0);
INSERT INTO users VALUES (4, 'root', 402253, '5188636593042629', 0);

INSERT INTO passwords VALUES (0, 'nimda');
INSERT INTO passwords VALUES (1, 'kek');
INSERT INTO passwords VALUES (2, 'kekkek');
INSERT INTO passwords VALUES (3, 'nigol');
INSERT INTO passwords VALUES (4, 'toor');

