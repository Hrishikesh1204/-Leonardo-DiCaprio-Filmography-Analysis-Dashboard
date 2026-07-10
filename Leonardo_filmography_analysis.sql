CREATE DATABASE leonardo_analysis;
USE leonardo_analysis;
CREATE TABLE movies(
title VARCHAR(255),
release_date DATE,
genres TEXT,
    budget BIGINT,
    revenue BIGINT,
    runtime INT,
    vote_average DECIMAL(3,1),
    vote_count INT,
    popularity DECIMAL(10,3),
    crew LONGTEXT,
    cast_members LONGTEXT,
    director VARCHAR(100),
    release_year INT,
    profit BIGINT
);

SELECT COUNT(*) AS Total_Movies
FROM leonardo_movies_final;

SELECT title, revenue
FROM leonardo_movies_final
ORDER BY revenue DESC
LIMIT 10;

SELECT title, vote_average
FROM leonardo_movies_final
ORDER BY vote_average DESC
LIMIT 10;

SELECT director,
COUNT(*) AS Total_Movies
FROM leonardo_movies_final
GROUP BY director
ORDER BY Total_Movies DESC;

SELECT COUNT(*) AS Total_Movies
FROM leonardo_movies_final;

SELECT ROUND(AVG(vote_average),2) AS Average_Rating
FROM leonardo_movies_final;

SELECT title, vote_average
FROM leonardo_movies_final
ORDER BY vote_average DESC
LIMIT 1;

SELECT title, revenue
FROM leonardo_movies_final
ORDER BY revenue DESC
LIMIT 1;

SELECT title, profit
FROM leonardo_movies_final
ORDER BY profit DESC
LIMIT 1;

SELECT title, release_year
FROM leonardo_movies_final
WHERE release_year>2010;

SELECT title, vote_average
FROM leonardo_movies_final
WHERE vote_average>8;

SELECT title,revenue
FROM leonardo_movies_final
WHERE revenue>500000000;

SELECT ROUND(AVG(runtime),2) AS Avg_Runtime
FROM leonardo_movies_final;

SELECT director,
COUNT(*) AS Total_Movies
FROM leonardo_movies_final
GROUP BY director
ORDER BY Total_Movies DESC;

SELECT
title,
revenue,
RANK()OVER(ORDER BY revenue DESC) AS Revenue_Rank
FROM leonardo_movies_final;

SELECT
title,
profit,
DENSE_RANK() OVER(ORDER BY profit DESC) AS Profit_Rank
FROM leonardo_movies_final;

SELECT
director,
ROUND(AVG(revenue))AS Avg_Revenue
FROM leonardo_movies_final
GROUP BY director
ORDER BY Avg_Revenue DESC;

SELECT
director,
ROUND(AVG(vote_average),2) AS Avg_Rating
FROM leonardo_movies_final
GROUP BY director
ORDER BY Avg_Rating DESC;

SELECT
title,
revenue,
CASE
    WHEN revenue >= 1000000000 THEN 'Blockbuster'
    WHEN revenue >= 500000000 THEN 'Hit'
    WHEN revenue >= 100000000 THEN 'Average'
    ELSE 'Low Revenue'
END AS Revenue_Category
FROM leonardo_movies_final;

SELECT
title,
revenue,
SUM(revenue) OVER(ORDER BY release_year) AS Running_Revenue
FROM leonardo_movies_final;

SELECT
title,
release_year,
vote_average,
LAG(vote_average) OVER(ORDER BY release_year) AS Previous_Rating
FROM leonardo_movies_final;

SELECT
title,
release_year,
revenue,
LEAD(revenue) OVER(ORDER BY release_year) AS Next_Revenue
FROM leonardo_movies_final;

SELECT *
FROM (
    SELECT
        title,
        revenue,
        DENSE_RANK() OVER(ORDER BY revenue DESC) AS rnk
    FROM leonardo_movies_final
) t
WHERE rnk <= 3;

SELECT
title,
budget,
revenue,
ROUND(revenue / budget,2) AS ROI
FROM leonardo_movies_final
WHERE budget > 0
ORDER BY ROI DESC;





