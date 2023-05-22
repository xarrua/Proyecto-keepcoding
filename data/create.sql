CREATE TABLE "usuariospeck" (
	"usu_id"	INTEGER,
	"usu_name"	TEXT NOT NULL,
	"usu_lastname"	NUMERIC NOT NULL,
	"usu_email"	TEXT NOT NULL UNIQUE,
	"usu_phone"	TEXT NOT NULL UNIQUE,
	"usu_country"	TEXT,
	"usu_city"	TEXT,
	"usu_birthd"	TEXT NOT NULL,
	"usu_sex"	TEXT NOT NULL,
	"usu_date"	TEXT NOT NULL,
	"usu_user"	TEXT NOT NULL UNIQUE,
	"usu_pass"	TEXT NOT NULL,
	"usu_concept"	INTEGER,
	"usu_quantity"	INTEGER NOT NULL,
	PRIMARY KEY("usu_id" AUTOINCREMENT)
)