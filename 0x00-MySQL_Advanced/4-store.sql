-- Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity


DELIMITER $$
CREATE TRIGGER minustrigger
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END$$
DELIMITER ;
