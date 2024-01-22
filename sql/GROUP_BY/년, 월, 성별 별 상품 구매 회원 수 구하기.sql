-- 코드를 입력하세요
SELECT DATE_FORMAT(O.SALES_DATE, '%Y') AS YEAR,
    DATE_FORMAT(O.SALES_DATE, '%m') AS MONTH,
    U.GENDER,
    COUNT(DISTINCT U.USER_ID) AS USERS
FROM USER_INFO U
JOIN ONLINE_SALE O
ON U.USER_ID = O.USER_ID
GROUP BY YEAR, MONTH, GENDER
HAVING GENDER IS NOT NULL
ORDER BY YEAR, MONTH, GENDER