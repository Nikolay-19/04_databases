SELECT
    LTRIM(peak_name, 'M') as "Left Trim",
	RTRIM(peak_name, 'm') as "Right Trim"
FROM
    peaks
