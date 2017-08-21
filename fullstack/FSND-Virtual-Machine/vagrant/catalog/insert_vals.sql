delete from category;
delete from item; --where name like 'Basketball%';


insert into category (name) values('Basketball');
insert into item (name, description, category_id, username) values('Basketball', 'Ball for playing ball', 1, 'Farzaan Nasar');
insert into item (name, description, category_id, username) values('Basketball Hoop', 'Hoop for playing ball', 1, 'Farzaan Nasar');
insert into item (name, description, category_id, username) values('Basketball Show', 'Shoew for playing ball', 1, 'Farzaan Nasar');

insert into category (name) values('Baseball');
insert into item (name, description, category_id, username) values('Baseball', 'Ball for playing Baseball', 2, 'Farzaan Nasar');
insert into item (name, description, category_id, username) values('Baseball bat', 'BAt for playing base ball', 2, 'Farzaan Nasar');
insert into item (name, description, category_id, username) values('Baseball Glove', 'Gloeve for playing Baseball', 2, 'Farzaan Nasar');

insert into category (name) values('Skating');
insert into item (name, description, category_id, username) values('Skate', 'Ball for playing Baseball', 3, 'Farzaan Nasar');
insert into item (name, description, category_id, username) values('Skating bat', 'BAt for playing base skating', 3, 'Farzaan Nasar');
insert into item (name, description, category_id, username) values('Skating Glove', 'Gloeve for playing Skating', 3, 'Farzaan Nasar');

insert into category (name) values('Frisbee');

insert into category (name) values('Snowboarding');

insert into category (name) values('Rock Claimbing');

insert into category (name) values('Foosball');

select * from item;
select * from category;