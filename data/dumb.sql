

CREATE DATABASE castingagency_test; 
\c  castingagency_test;

--
-- PostgreSQL database dump
--

-- Dumped from database version 13.1 (Debian 13.1-1.pgdg100+1)
-- Dumped by pg_dump version 13.1 (Debian 13.1-1.pgdg100+1)


SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Cast; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public."Cast" (
    id integer NOT NULL,
    movie_id integer NOT NULL,
    actor_id integer NOT NULL
);


ALTER TABLE public."Cast" OWNER TO root;

--
-- Name: Cast_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public."Cast_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Cast_id_seq" OWNER TO root;

--
-- Name: Cast_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public."Cast_id_seq" OWNED BY public."Cast".id;


--
-- Name: actors; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.actors (
    id integer NOT NULL,
    name character varying(120) NOT NULL,
    age integer NOT NULL,
    email character varying(120) NOT NULL,
    gender character varying(120),
    phone character varying(120) NOT NULL,
    image_link character varying(500)
);


ALTER TABLE public.actors OWNER TO root;

--
-- Name: actors_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.actors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actors_id_seq OWNER TO root;

--
-- Name: actors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.actors_id_seq OWNED BY public.actors.id;


--
-- Name: movies; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.movies (
    id integer NOT NULL,
    title character varying(120) NOT NULL,
    release_date timestamp without time zone NOT NULL,
    description character varying(500),
    genre character varying(120) NOT NULL,
    trailer_link character varying(500),
    poster_link character varying(500)
);


ALTER TABLE public.movies OWNER TO root;

--
-- Name: movies_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.movies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.movies_id_seq OWNER TO root;

--
-- Name: movies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.movies_id_seq OWNED BY public.movies.id;


--
-- Name: Cast id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public."Cast" ALTER COLUMN id SET DEFAULT nextval('public."Cast_id_seq"'::regclass);


--
-- Name: actors id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.actors ALTER COLUMN id SET DEFAULT nextval('public.actors_id_seq'::regclass);


--
-- Name: movies id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.movies ALTER COLUMN id SET DEFAULT nextval('public.movies_id_seq'::regclass);


--
-- Data for Name: Cast; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public."Cast" (id, movie_id, actor_id) FROM stdin;
\.


--
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public.actors (id, name, age, email, gender, phone, image_link) FROM stdin;
1	ahmed 	25	Anya@Gmail.com	male	+9665555555555	https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/
2	Gloria britchit	45	gloria_colombia@Gmail.com	female	+9665555555555	https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/
3	Mitchil britchit	40	Mitchill@Gmail.com	male	+9665555555555	https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/
4	Anya Taylor-Joy	24	Anya@Gmail.com	female	+9665555555555	https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/
5	Alext	24	Anya@Gmail.com	female	+9665555555555	https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/
6	Alex	24	Anya@Gmail.com	female	+9665555555555	https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/
7	lilly	24	Anya@Gmail.com	female	+9665555555555	https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/
8	hailey	24	Anya@Gmail.com	female	+9665555555555	https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/
9	dede	24	Anya@Gmail.com	female	+9665555555555	https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/
10	jay	65	Anya@Gmail.com	male	+9665555555555	https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/
11	manny	23	manny@Gmail.com	male	+9665555555555	https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/
12	look	23	look@Gmail.com	male	+9665555555555	https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/
13	kim	40	kim@Gmail.com	male	+9665555555555	https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/
\.


--
-- Data for Name: movies; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public.movies (id, title, release_date, description, genre, trailer_link, poster_link) FROM stdin;
1	scarface	1980-12-29 00:00:00	very nice story 	family	\N	https://images.app.goo.gl/mG2ARPW22BHbrLo76
2	scarface	1980-12-29 00:00:00	very nice story 	family	\N	https://images.app.goo.gl/mG2ARPW22BHbrLo76
3	titanic	1999-12-29 00:00:00	Story about a ship drawn in the oscen	family	\N	https://images.app.goo.gl/mG2ARPW22BHbrLo76
4	Elcamino	2019-12-29 00:00:00	what heepnd to jesse after breaking bad series	crime	\N	https://images.app.goo.gl/mG2ARPW22BHbrLo76
5	Ford vs Ferrari	2019-12-19 00:00:00	what heepnd to jesse after breaking bad series	crime	\N	https://images.app.goo.gl/mG2ARPW22BHbrLo76
\.


--
-- Name: Cast_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('public."Cast_id_seq"', 1, false);


--
-- Name: actors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('public.actors_id_seq', 13, true);


--
-- Name: movies_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('public.movies_id_seq', 5, true);


--
-- Name: Cast Cast_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public."Cast"
    ADD CONSTRAINT "Cast_pkey" PRIMARY KEY (id);


--
-- Name: actors actors_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.actors
    ADD CONSTRAINT actors_pkey PRIMARY KEY (id);


--
-- Name: movies movies_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.movies
    ADD CONSTRAINT movies_pkey PRIMARY KEY (id);


--
-- Name: Cast Cast_actor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public."Cast"
    ADD CONSTRAINT "Cast_actor_id_fkey" FOREIGN KEY (actor_id) REFERENCES public.actors(id);


--
-- Name: Cast Cast_movie_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public."Cast"
    ADD CONSTRAINT "Cast_movie_id_fkey" FOREIGN KEY (movie_id) REFERENCES public.movies(id);


--
-- PostgreSQL database dump complete
--


