'''
An ecommerce website admin panel needs to generate a report to display product stock status in their warehouse. The report should display a list of all product categories and the total number of products available in each category. It should be limited to products with more than 10 units available. The result should have the following columns: category | title | total_stock. • category- the name of the product category (e.g., Electronics, Clothing) . title-the title of the product • total_stock-total number of items available in stock for that product The result should be sorted in ascending order by category, then in ascending order by title, and finally in descending order by total_stock. Note: • Only products with a total stock of more than 10 items should be included in the report. 2 3 4 my SQL query for it
​'''




# Just write the things...

# SELECT  category,title,SUM(stock) AS total_stock FROM products
# WHERE stock > 10 GROUP BY category, title ORDER BY category ASC, title ASC, total_stock DESC;