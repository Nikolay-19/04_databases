DROP TABLE IF EXISTS towns CASCADE;
CREATE TABLE towns(
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR(45) NOT NULL);

DROP TABLE IF EXISTS stadiums CASCADE;
CREATE TABLE stadiums(
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR(45) NOT NULL,
    capacity INT NOT NULL,
    town_id INT NOT NULL,
    CONSTRAINT stadiums_capacity_check CHECK (capacity > 0),
    CONSTRAINT fk_stadiums_towns FOREIGN KEY(town_id) REFERENCES towns("id") ON UPDATE CASCADE ON DELETE CASCADE);

DROP TABLE IF EXISTS teams CASCADE;
CREATE TABLE teams(
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR(45) NOT NULL,
    established DATE NOT NULL,
    fan_base INT NOT NULL DEFAULT 0,
    stadium_id INT NOT NULL,
    CONSTRAINT teams_fan_base_check CHECK (fan_base >= 0),
    CONSTRAINT fk_teams_stadiums FOREIGN KEY(stadium_id) REFERENCES stadiums("id") ON UPDATE CASCADE ON DELETE CASCADE);

DROP TABLE IF EXISTS coaches CASCADE;
CREATE TABLE coaches(
    "id" SERIAL PRIMARY KEY,
    first_name VARCHAR(10) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    salary NUMERIC(10, 2) NOT NULL DEFAULT 0,
    coach_level INT NOT NULL DEFAULT 0,
    CONSTRAINT coaches_salary_check CHECK (salary >= 0),
    CONSTRAINT coaches_coach_level_check CHECK (coach_level >= 0));

DROP TABLE IF EXISTS skills_data CASCADE;
CREATE TABLE skills_data(
    "id" SERIAL PRIMARY KEY,
    dribbling INT DEFAULT 0,
    pace INT DEFAULT 0,
    "passing" INT DEFAULT 0,
    shooting INT DEFAULT 0,
    speed INT DEFAULT 0,
    strength INT DEFAULT 0,
    CONSTRAINT skills_data_dribbling_check CHECK (dribbling >= 0),
    CONSTRAINT skills_data_pace_check CHECK (pace >= 0),
    CONSTRAINT skills_data_passing_check CHECK ("passing" >= 0),
    CONSTRAINT skills_data_shooting_check CHECK (shooting >= 0),
    CONSTRAINT skills_data_speed_check CHECK (speed >= 0),
    CONSTRAINT skills_data_strength_check CHECK (strength >= 0));

DROP TABLE IF EXISTS players CASCADE;
CREATE TABLE players(
    "id" SERIAL PRIMARY KEY,
    first_name VARCHAR(10) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    age INT NOT NULL DEFAULT 0,
    "position" CHAR(1) NOT NULL,
    salary NUMERIC(10, 2) NOT NULL DEFAULT 0,
    hire_date TIMESTAMP,
    skills_data_id INT NOT NULL,
    team_id INT,
    CONSTRAINT players_age_check CHECK (age >= 0),
    CONSTRAINT players_salary_check CHECK (salary >= 0),
    CONSTRAINT fk_players_skills_data FOREIGN KEY(skills_data_id) REFERENCES skills_data("id") ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_players_teams FOREIGN KEY(team_id) REFERENCES teams("id") ON UPDATE CASCADE ON DELETE CASCADE);

DROP TABLE IF EXISTS players_coaches CASCADE;
CREATE TABLE players_coaches(
    player_id INT,
	coach_id INT,
    CONSTRAINT fk_players_coaches_players FOREIGN KEY(player_id) REFERENCES players("id") ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_players_coaches_coaches FOREIGN KEY(coach_id) REFERENCES coaches("id") ON UPDATE CASCADE ON DELETE CASCADE);
