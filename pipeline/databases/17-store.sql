-- This task is telling me to let MySQL handle the deletion of data
-- Not sure how
-- Does it just like... automatically happen?

-- DELIMITER //

CREATE TRIGGER after_order_insert
AFTER INSERT ON orders
FOR EACH ROW
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE items.name = NEW.item_name;

-- DELIMITER ;
