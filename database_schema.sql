create table if not exists recipes
(
	recipe_id integer not null
		constraint recipes_pk
			primary key autoincrement,
	name text not null,
	prep text not null,
	recipe text not null
);

create unique index if not exists  recipes_recipe_id_uindex
	on recipes (recipe_id);

create table if not exists ingredients
(
	ingredient_id integer not null
		constraint ingredients_pk
			primary key autoincrement,
	recipe_id integer not null
		constraint ingredients_recipes_recipe_id_fk
			references recipes
				on update restrict on delete restrict,
	amount text not null,
	item text not null
);

create unique index if not exists ingredients_ingredient_id_uindex
	on ingredients (ingredient_id);

create table if not exists history
(
	history_id integer not null
		constraint history_pk
			primary key autoincrement,
	recipe_id integer not null
		constraint history_recipes_recipe_id_fk
			references recipes
				on update restrict on delete restrict,
	date text not null,
	start_time text,
	end_time text
);

create unique index if not exists history_history_id_uindex
	on history (history_id);

create unique index if not exists history_date_uindex
	on history (date);

create table if not exists schedule
(
	schedule_id integer not null
		constraint schedule_pk
			primary key autoincrement,
	recipe_id integer not null
		constraint schedule_recipes_recipe_id_fk
			references recipes
				on update restrict on delete restrict,
	date text not null
);

create unique index if not exists schedule_schedule_id_uindex
	on schedule (schedule_id);

create unique index if not exists schedule_date_uindex
	on schedule (date);


