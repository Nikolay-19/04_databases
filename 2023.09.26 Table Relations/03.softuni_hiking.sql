SELECT
    routes.start_point,
    routes.end_point,
    routes.leader_id,
    concat(campers.first_name, ' ', campers.last_name) AS leader_name
FROM
    routes, campers
WHERE
    routes.leader_id = campers.id
