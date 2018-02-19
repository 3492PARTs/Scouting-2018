CREATE TABLE `user` (
	`user_id` bigint NOT NULL AUTO_INCREMENT,
	`username` varchar(50) NOT NULL,
	`password` varchar(255) NOT NULL,
	`email` varchar(255) NOT NULL,
	`confirmed_at` DATETIME NOT NULL,
	`active` bool NOT NULL,
	`first_name` varchar(100) NOT NULL,
	`last_name` varchar(100) NOT NULL,
	`team` varchar(4) NOT NULL,
	PRIMARY KEY (`user_id`)
);

CREATE TABLE `user_roles` (
	`user_role_id` bigint NOT NULL AUTO_INCREMENT,
	`user_id` bigint NOT NULL,
	`role_id` bigint NOT NULL,
	PRIMARY KEY (`user_role_id`)
);

CREATE TABLE `role` (
	`role_id` bigint NOT NULL AUTO_INCREMENT,
	`role_nm` varchar(10) NOT NULL,
	PRIMARY KEY (`role_id`)
);

CREATE TABLE `event` (
	`event_id` bigint NOT NULL AUTO_INCREMENT,
	`event_nm` varchar(255) NOT NULL,
	`date_st` DATE NOT NULL,
	`date_end` DATE NOT NULL,
	PRIMARY KEY (`event_id`)
);

CREATE TABLE `team` (
	`team_no` varchar(4) NOT NULL,
	`event_id` bigint NOT NULL,
	`team_nm` varchar(255) NOT NULL,
	PRIMARY KEY (`team_no`)
);

CREATE TABLE `match` (
	`match_id` bigint NOT NULL AUTO_INCREMENT,
	`team_no` varchar(4) NOT NULL,
	`auto_id` bigint NOT NULL,
	`tele_id` bigint NOT NULL,
	`match_no` int NOT NULL,
	PRIMARY KEY (`match_id`)
);

CREATE TABLE `auto` (
	`auto_id` bigint NOT NULL AUTO_INCREMENT,
	`no_blocks` int NOT NULL,
	`move` varchar(1) NOT NULL,
	`switch` varchar(1) NOT NULL,
	`scale` varchar(1) NOT NULL,
	`comments` varchar(2000),
	PRIMARY KEY (`auto_id`)
);

CREATE TABLE `tele` (
	`tele_id` bigint NOT NULL AUTO_INCREMENT,
	`no_blocks_scale` int NOT NULL,
	`no_blocks_switch` int NOT NULL,
	`rate` int NOT NULL,
	`comments` varchar(2000) NOT NULL,
	PRIMARY KEY (`tele_id`)
);

ALTER TABLE `user_roles` ADD CONSTRAINT `user_roles_fk0` FOREIGN KEY (`user_id`) REFERENCES `user`(`user_id`);

ALTER TABLE `user_roles` ADD CONSTRAINT `user_roles_fk1` FOREIGN KEY (`role_id`) REFERENCES `role`(`role_id`);

ALTER TABLE `team` ADD CONSTRAINT `team_fk0` FOREIGN KEY (`event_id`) REFERENCES `event`(`event_id`);

ALTER TABLE `match` ADD CONSTRAINT `match_fk0` FOREIGN KEY (`team_no`) REFERENCES `team`(`team_no`);

ALTER TABLE `match` ADD CONSTRAINT `match_fk1` FOREIGN KEY (`auto_id`) REFERENCES `auto`(`auto_id`);

ALTER TABLE `match` ADD CONSTRAINT `match_fk2` FOREIGN KEY (`tele_id`) REFERENCES `tele`(`tele_id`);
