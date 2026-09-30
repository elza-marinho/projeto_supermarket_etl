SELECT
    "Branch",
    SUM(CAST("Sales" AS NUMERIC)) AS faturamento
FROM  supermarket_raw
GROUP BY "Branch"
ORDER BY faturamento DESC;



SELECT "Branch", COUNT(*) AS quantidade_vendas
FROM supermarket_raw
GROUP BY "Branch"
ORDER BY quantidade_vendas DESC;

SELECT "Product line", SUM("Sales":: NUMERIC)  AS  faturamento_produto
FROM supermarket_raw
GROUP BY ("Product line")
ORDER BY faturamento_produto DESC;

SELECT "Product line",
    AVG(CAST("Rating" AS NUMERIC)) AS media_avaliacao
FROM supermarket_raw
GROUP BY "Product line"
ORDER BY media_avaliacao DESC;


SELECT AVG(CAST("Sales" AS NUMERIC)) AS media_vendas
FROM supermarket_raw;

SELECT MAX(CAST("Sales" AS NUMERIC)) AS maior_venda FROM supermarket_raw;
