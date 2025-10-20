CREATE TABLE search_results(
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR(50),
    release_year INT,
    rating FLOAT,
    category_name VARCHAR(50),
    publisher_name VARCHAR(50),
    min_players VARCHAR(50),
    max_players VARCHAR(50));

CREATE OR REPLACE PROCEDURE usp_search_by_category(IN category VARCHAR(50))
LANGUAGE plpgsql
AS $$
BEGIN
    TRUNCATE TABLE search_results;
    INSERT INTO search_results("name", release_year, rating, category_name, publisher_name, min_players, max_players)
    SELECT
        bg.name, bg.release_year, bg.rating, ct.name AS category_name, pb.name AS publisher_name,
        concat(pr.min_players, ' people') AS min_players, concat(pr.max_players, ' people') AS max_players
    FROM
        board_games AS bg
        JOIN categories AS ct
        ON bg.category_id = ct.id
            JOIN publishers AS pb
            ON bg.publisher_id = pb.id
                JOIN players_ranges AS pr
                ON bg.players_range_id = pr.id
    WHERE
        ct.name = category
    ORDER BY
        pb.name ASC, bg.release_year DESC;
END; $$;
