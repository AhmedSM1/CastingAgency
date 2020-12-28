CREATE DATABASE castingAgency_test
CREATE DATABASE castingAgency



\connect "castingAgency";

DROP TABLE IF EXISTS "Cast";
DROP SEQUENCE IF EXISTS "Cast_id_seq";
CREATE SEQUENCE "Cast_id_seq" INCREMENT  MINVALUE  MAXVALUE  START 1 CACHE ;

CREATE TABLE "public"."Cast" (
    "id" integer DEFAULT nextval('"Cast_id_seq"') NOT NULL,
    "movie_id" integer NOT NULL,
    "actor_id" integer NOT NULL,
    CONSTRAINT "Cast_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "Cast_actor_id_fkey" FOREIGN KEY (actor_id) REFERENCES actors(id) NOT DEFERRABLE,
    CONSTRAINT "Cast_movie_id_fkey" FOREIGN KEY (movie_id) REFERENCES movies(id) NOT DEFERRABLE
) WITH (oids = false);


DROP TABLE IF EXISTS "actors";
DROP SEQUENCE IF EXISTS actors_id_seq;
CREATE SEQUENCE actors_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."actors" (
    "id" integer DEFAULT nextval('actors_id_seq') NOT NULL,
    "name" character varying(120) NOT NULL,
    "age" integer NOT NULL,
    "email" character varying(120) NOT NULL,
    "gender" character varying(120),
    "phone" character varying(120) NOT NULL,
    "image_link" character varying(500),
    CONSTRAINT "actors_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

INSERT INTO "actors" ("id", "name", "age", "email", "gender", "phone", "image_link") VALUES
(1,	'Ahmed',	25,	'Ahmed@Gmail.com',	'male',	'+966505558844',	'https://docs.sqlalchemy.org/en/13/errors.html#error-e3q8');

DROP TABLE IF EXISTS "alembic_version";
CREATE TABLE "public"."alembic_version" (
    "version_num" character varying(32) NOT NULL,
    CONSTRAINT "alembic_version_pkc" PRIMARY KEY ("version_num")
) WITH (oids = false);


DROP TABLE IF EXISTS "movies";
DROP SEQUENCE IF EXISTS movies_id_seq;
CREATE SEQUENCE movies_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."movies" (
    "id" integer DEFAULT nextval('movies_id_seq') NOT NULL,
    "title" character varying(120) NOT NULL,
    "release_date" timestamp NOT NULL,
    "description" character varying(500),
    "genre" character varying(120) NOT NULL,
    "trailer_link" character varying(500),
    "poster_link" character varying(500),
    CONSTRAINT "movies_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


-- 2020-12-28 23:52:19.661253+00
