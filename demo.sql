select AVG(quantity * unit_price) as avg_price
from orders
where status = 'shipped'
  
