CREATE VIEW chaquePoint AS
    select gid, roadno, start_km, end_km, lengthkm, width, (st_dumpPoints(geom)).geom
        from dago5

--REQUETE
SELECT COUNT(idBatiment)

select roadno from dago5 
    where roadno in 
    (select roadno from dago5
        where st_distance_sphere(, ())) 

CREATE TABLE REFFERENCEOBJET(
    idRefference SERIAL PRIMARY KEY,
    nom VARCHAR(200)
);

INSERT INTO REFFERENCEOBJET(nom) VALUES('Hopital'),('Humain'),('Ecole');


CREATE TABLE OBJETSURFACE(
    idObjet SERIAL PRIMARY KEY,
    idRefference int,
    nombre bigint,
    coordonne geometry(POINT, 4326)
);


-- 47.9995262	-18.8921933
INSERT INTO OBJETSURFACE(idRefference, nombre, coordonne) VALUES(3, 3, 'POINT(47.9995262 -18.8921933)');

-- 47.989484	-18.8878385
INSERT INTO OBJETSURFACE(idRefference, nombre, coordonne) VALUES(3, 3, 'POINT(47.989484	-18.8878385)');

-- 48.1631291	-18.9107643
INSERT INTO OBJETSURFACE(idRefference, nombre, coordonne) VALUES(3, 3, 'POINT(48.1631291 -18.9107643)');

-- 47.0606723	-19.9156356

INSERT INTO OBJETSURFACE(idRefference, nombre, coordonne) VALUES(3, 3, 'POINT(47.0606723	-19.9156356)');


-- 47.0605435	-19.9255611
INSERT INTO OBJETSURFACE(idRefference, nombre, coordonne) VALUES(3, 3, 'POINT(47.0605435 -19.9255611)');

-- 47.0789636	-20.0647593
INSERT INTO OBJETSURFACE(idRefference, nombre, coordonne) VALUES(3, 3, 'POINT(47.0789636 -20.0647593)');

-- 47.081796	-20.0755622
INSERT INTO OBJETSURFACE(idRefference, nombre, coordonne) VALUES(3, 3, 'POINT(47.081796	-20.0755622)');

-- 47.0966332	-19.7966552
INSERT INTO OBJETSURFACE(idRefference, nombre, coordonne) VALUES(3, 3, 'POINT(47.0966332 -19.7966552)');
--47.1104734	-19.7966148
INSERT INTO OBJETSURFACE(idRefference, nombre, coordonne) VALUES(3, 3, 'POINT(47.1104734 -19.7966148)');

INSERT INTO OBJETSURFACE(idRefference, nombre, coordonne) VALUES(3, 3, 'POINT(47.0605435 -19.9255611)');

--47.0605435	-19.9255611

INSERT INTO OBJETSURFACE(idRefference, nombre, coordonne) VALUES(3, 3, 'POINT(47.0605435 -19.9255611)');

--47.0789636	-20.0647593

INSERT INTO OBJETSURFACE(idRefference, nombre, coordonne) VALUES(3, 3, 'POINT(47.0789636 -20.0647593)');


--47.081796	-20.0755622

INSERT INTO OBJETSURFACE(idRefference, nombre, coordonne) VALUES(3, 3, 'POINT(47.081796	-20.0755622)');

--47.0966332	-19.7966552

INSERT INTO OBJETSURFACE(idRefference, nombre, coordonne) VALUES(3, 3, 'POINT(47.0966332 -19.7966552)');

--47.1104734	-19.7966148

INSERT INTO OBJETSURFACE(idRefference, nombre, coordonne) VALUES(3, 3, 'POINT(47.0966332 -19.7966552)');

--ETOO

--47.9995262	-18.8921933

--47.989484	-18.8878385

--48.1631291	-18.9107643

--47.0606723	-19.9156356

INSERT INTO OBJETSURFACE(idRefference, nombre, coordonne) VALUES(3, 3, 'POINT(47.9995262 -18.8921933)');

INSERT INTO OBJETSURFACE(idRefference, nombre, coordonne) VALUES(3, 3, 'POINT(47.989484	-18.8878385)');

INSERT INTO OBJETSURFACE(idRefference, nombre, coordonne) VALUES(3, 3, 'POINT(48.1631291 -18.9107643)');

INSERT INTO OBJETSURFACE(idRefference, nombre, coordonne) VALUES(3, 3, 'POINT(47.0606723 -19.9156356)');



CREATE VIEW refferencexobjet AS
    SELECT r.idRefference, r.nom, o.idObjet, o.nombre, o.coordonne FROM REFFERENCEOBJET r
        JOIN OBJETSURFACE o ON r.idRefference = o.idRefference;

-- ITO TAPENA AM MAINTY
shp2pgsql -s 4326 -I madagascar_roads_version4.shp dago5 | psql -d <nom de la base de donnee>

-------------------------------------

CREATE DATABASE bddspaciale;
\c bddspaciale


ALTER TABLE dago5 add column profondeur float;
-- decomposer multilignestring
select st_length(st_dumpPoints(geom)) from dago5 WHERE roadno = 'RNP 2' and start_km = 0;
--longueur multiligne string
select (ST_LengthSpheroid(dago5.geom, 'SPHEROID["WGS 84",6378137,298.257223563]'))/1000 from dago5 WHERE roadno = 'RNP 2' and start_km = 0;

DROP TABLE MATERIAUX;
CREATE TABLE MATERIAUX(
    idMateriaux SERIAL PRIMARY KEY,
    nom VARCHAR(200),
    refference int,
    prix float,
    duree int
);

INSERT INTO MATERIAUX(nom, refference, prix, duree) values('GOUDRON', 1, 3000, 2, 0.05);

CREATE TABLE ECHELLEJour(
    idechelleJour SERIAL PRIMARY KEY,
    niveau int,
    jour int,
    duree int
);

INSERT INTO ECHELLEJour(niveau, jour) 
    VALUES(100, 2);

CREATE TABLE ECHELLE(
    idechelle SERIAL PRIMARY KEY,
    niveau int,
    prix float
);

INSERT INTO ECHELLE(niveau, prix) 
    VALUES(100, 5000);

CREATE TABLE LALANASIMBA(
    idfahasimbana SERIAL PRIMARY KEY,
    roadno VARCHAR(200),
    debut int,
    fin int,
    niveau int    
);

alter table LALANASIMBA add column profondeur int;
INSERT INTO LALANASIMBA(roadno, debut, fin, niveau)
    VALUES('RNP 2', 20, 25, 30, 100);

INSERT INTO LALANASIMBA(roadno, debut, fin, niveau)
    VALUES('RNP 2', 2, 5, 30, 100);

-- 88,6	89,4
INSERT INTO LALANASIMBA(roadno, debut, fin, niveau)
    VALUES('RNP 2', 88, 89, 100);
-- 81,2	82,7
INSERT INTO LALANASIMBA(roadno, debut, fin, niveau)
    VALUES('RNP 2', 81, 82, 100);
-- 105	106
INSERT INTO LALANASIMBA(roadno, debut, fin, niveau)
    VALUES('RNP 2', 105, 106, 100);
	
-- 154	155
INSERT INTO LALANASIMBA(roadno, debut, fin, niveau)
    VALUES('RNP 7', 154, 155, 100);
-- 191	192
INSERT INTO LALANASIMBA(roadno, debut, fin, niveau)
    VALUES('RNP 7', 191, 192, 100);
-- 172	173
INSERT INTO LALANASIMBA(roadno, debut, fin, niveau)
    VALUES('RNP 7', 172, 173, 100);



ALTER TABLE dago5 add column profondeur float;


CREATE TABLE FAHASIMBANA(
    id SERIAL PRIMARY KEY,
    idLalana int,
    PKD int,
    PKA int,
    degre int
);
