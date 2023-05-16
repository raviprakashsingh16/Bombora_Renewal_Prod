CREATE TABLE IF NOT EXISTS dwh.f_acc_topics (
	accountid varchar(18) NULL,
	accountname varchar(255) NULL,
	userid varchar(18) NULL,
	theme varchar(1024) NULL,
	category varchar(255) NULL,
	topic varchar(10000) NULL,
	"cluster" varchar(255) NULL
);