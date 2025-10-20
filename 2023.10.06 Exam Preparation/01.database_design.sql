DROP TABLE IF EXISTS owners CASCADE;
CREATE TABLE owners(
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR(50) NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    address VARCHAR(50));

DROP TABLE IF EXISTS animal_types CASCADE;
CREATE TABLE animal_types(
    "id" SERIAL PRIMARY KEY,
    animal_type VARCHAR(30) NOT NULL);

DROP TABLE IF EXISTS cages CASCADE;
CREATE TABLE cages(
    "id" SERIAL PRIMARY KEY,
    animal_type_id INTEGER NOT NULL,
    CONSTRAINT fk_cages_animal_types FOREIGN KEY (animal_type_id) REFERENCES animal_types("id") ON UPDATE CASCADE ON DELETE CASCADE);

DROP TABLE IF EXISTS animals CASCADE;
CREATE TABLE animals(
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR(30) NOT NULL,
    birthdate DATE NOT NULL,
    owner_id INTEGER,
    animal_type_id INTEGER NOT NULL,
    CONSTRAINT fk_animals_owners FOREIGN KEY (owner_id) REFERENCES owners("id") ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_animals_animal_types FOREIGN KEY (animal_type_id) REFERENCES animal_types("id") ON UPDATE CASCADE ON DELETE CASCADE);

DROP TABLE IF EXISTS volunteers_departments CASCADE;
CREATE TABLE volunteers_departments(
    "id" SERIAL PRIMARY KEY,
    department_name VARCHAR(30) NOT NULL);

DROP TABLE IF EXISTS volunteers CASCADE;
CREATE TABLE volunteers(
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR (50) NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    address VARCHAR(50),
    animal_id INTEGER,
    department_id INTEGER NOT NULL,
    CONSTRAINT fk_volunteers_animals FOREIGN KEY (animal_id) REFERENCES animals("id") ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_volunteers_volunteers_departments FOREIGN KEY (department_id) REFERENCES volunteers_departments("id") ON UPDATE CASCADE ON DELETE CASCADE);

DROP TABLE IF EXISTS animals_cages CASCADE;
CREATE TABLE animals_cages(
    cage_id INTEGER NOT NULL,
    animal_id INTEGER NOT NULL,
    CONSTRAINT fk_animals_cages_cages FOREIGN KEY (cage_id) REFERENCES cages("id") ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_animals_cages_animals FOREIGN KEY (animal_id) REFERENCES animals("id") ON UPDATE CASCADE ON DELETE CASCADE);
