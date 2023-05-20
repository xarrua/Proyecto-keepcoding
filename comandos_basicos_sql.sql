/*seleccionar todos los registros de una tabla*/
/*SELECT * FROM movements;*/
/*seleccionar algunos campos de una tabla*/
/*SELECT concept,quantity FROM movements;*/
/*Insertar nuevos registros de la entidad o tabla movements*/
/*INSERT INTO movements(date,concept,quantity) VALUES("2023-05-02", "comida",500);*/
/*select con where*/
/*SELECT date,concept,quantity FROM movements WHERE quantity > 0;*/
/*update para actualizar registros de una tabla*/
/*UPDATE movements SET concept = "desayuno", quantity = -50 WHERE id=2; */
/*delete para borrar registros de una tabla*/
/*DELETE FROM movements WHERE id=4;*/

SELECT * FROM movements WHERE quantity <0 ORDER BY quantity ASC;