BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "room" (
	"id"	INTEGER,
	"room_number"	TEXT UNIQUE,
	"capacity"	INTEGER,
	"price"	INTEGER,
	"status"	TEXT DEFAULT 'available' CHECK("status" IN ('available', 'occupied', 'maintenance')),
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "room" VALUES (1,'101',2,500000,'available');
INSERT INTO "room" VALUES (2,'102',1,350000,'available');
INSERT INTO "room" VALUES (3,'103',1,350000,'occupied');
INSERT INTO "room" VALUES (4,'104',2,500000,'available');
INSERT INTO "room" VALUES (5,'201',4,900000,'available');
INSERT INTO "room" VALUES (6,'202',2,500000,'available');
INSERT INTO "room" VALUES (7,'203',2,500000,'occupied');
INSERT INTO "room" VALUES (8,'204',1,350000,'available');
COMMIT;
