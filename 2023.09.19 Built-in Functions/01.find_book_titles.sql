SELECT
    title
FROM
    books
WHERE
    title LIKE 'The%';


SELECT
    title
FROM
    books
WHERE
    SUBSTRING(title, 1, 3) = 'The';
