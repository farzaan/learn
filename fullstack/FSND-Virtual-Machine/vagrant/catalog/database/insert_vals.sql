delete from item where name like 'Basketball%';

insert into item (name, description, category_id) values('Basketball', 'Ball for playing ball', 3);
insert into item (name, description, category_id) values('Basketball Hoop', 'Hoop for playing ball', 3);
insert into item (name, description, category_id) values('Basketball Show', 'Shoew for playing ball', 3);

insert into category (name) values('Baseball');
insert into item (name, description, category_id) values('Baseball', 'Ball for playing Baseball', 4);
insert into item (name, description, category_id) values('Baseball bat', 'BAt for playing base ball', 4);
insert into item (name, description, category_id) values('Baseball Glove', 'Gloeve for playing Baseball', 4);

insert into category (name) values('Skating');
insert into item (name, description, category_id) values('Skate', 'Ball for playing Baseball', 5);
insert into item (name, description, category_id) values('Skating bat', 'BAt for playing base skating', 5);
insert into item (name, description, category_id) values('Skating Glove', 'Gloeve for playing Skating', 5);


select * from item;