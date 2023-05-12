--
-- PostgreSQL database dump
--

-- Dumped from database version 14.7 (Ubuntu 14.7-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.7 (Ubuntu 14.7-0ubuntu0.22.04.1)

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
-- Name: car; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.car (
    id bigint NOT NULL,
    marque character varying(50) NOT NULL,
    model character varying(50),
    im character varying(7) NOT NULL,
    nom_chauff character varying(50),
    nb_place integer NOT NULL,
    nb_voyage integer
);


ALTER TABLE public.car OWNER TO postgres;

--
-- Name: car_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.car_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.car_id_seq OWNER TO postgres;

--
-- Name: car_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.car_id_seq OWNED BY public.car.id;


--
-- Name: client; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.client (
    id bigint NOT NULL,
    nom character varying(100) NOT NULL,
    prenom character varying(100) NOT NULL,
    cin character varying(50),
    tel character varying(50),
    sexe character varying(10) NOT NULL,
    inscrit timestamp without time zone NOT NULL,
    adresse character varying(100) NOT NULL
);


ALTER TABLE public.client OWNER TO postgres;

--
-- Name: client_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.client_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.client_id_seq OWNER TO postgres;

--
-- Name: client_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.client_id_seq OWNED BY public.client.id;


--
-- Name: voyager; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.voyager (
    id bigint NOT NULL,
    id_client integer NOT NULL,
    id_car integer NOT NULL,
    destination character varying(20) NOT NULL,
    date_heure timestamp without time zone NOT NULL,
    num_place integer NOT NULL,
    nb_bagage integer
);


ALTER TABLE public.voyager OWNER TO postgres;

--
-- Name: voyager_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.voyager_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.voyager_id_seq OWNER TO postgres;

--
-- Name: voyager_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.voyager_id_seq OWNED BY public.voyager.id;


--
-- Name: car id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.car ALTER COLUMN id SET DEFAULT nextval('public.car_id_seq'::regclass);


--
-- Name: client id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.client ALTER COLUMN id SET DEFAULT nextval('public.client_id_seq'::regclass);


--
-- Name: voyager id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voyager ALTER COLUMN id SET DEFAULT nextval('public.voyager_id_seq'::regclass);


--
-- Data for Name: car; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.car (id, marque, model, im, nom_chauff, nb_place, nb_voyage) FROM stdin;
4	Sprinter	312	5001TBS	RALINGA	19	1
5	Volkswagen	2020	5123TBR	RANDRIANARIVELO Patrick	22	1
3	Sprinter	412	2314TAB	RABE	13	1
\.


--
-- Data for Name: client; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.client (id, nom, prenom, cin, tel, sexe, inscrit, adresse) FROM stdin;
1	Ter	Steven	102011027041	0344861844	Homme	2022-10-09 15:10:00	Isada
2	Bla	Kevin	100011027032	0330909817	Homme	2022-10-09 15:15:00	Mahazoarivo
3	ARIVELO	Noémie	\N	\N	Femme	2023-03-18 12:19:08	Ambanidia
4	R	f			Femme	2023-05-09 10:16:06.129337	Isada
6	RAZANAJATOVO	Niriharison Steila		0330567809	Femme	2023-05-09 10:26:53.778812	Ambohipo
7	RAVELO	Johnson			Homme	2023-05-09 10:37:29.854104	Isada
8	RAKOTONANDRA	Jean Paul	100103045067	0342981429	homme	2023-05-09 10:49:39.575045	Ilafy
9	TSANTANIAINA	Fanamby		0348205826	Femme	2023-05-09 15:49:40.57696	Talatamaty
10	TSANTANIAINA					2023-05-09 15:48:27.926963	
11	RABE	Jeannot			Homme	2023-05-09 15:51:38.753645	Igaga
12	RANDRIANASOLO 	Bakoly			Femme	2023-05-10 09:14:31.254156	Ilakaka
13	RAVELOSON 	Mariane	100011045017	0330868028	femme	2023-05-10 16:22:56.091356	Ambohipo
14	RATSIMBAZAFY	Henry	200012045027	0339008923	homme	2023-05-10 16:23:43.848617	Ilafy
15	RAVELOSON 	Maya	100012034045	0380808028	Femme	2023-05-11 04:51:53.414913	Ankorahotra
16	RAZANAJATOVO	Niriharisoa Stevy	101012067023	0388006526	homme	2023-05-11 05:01:40.791005	Lot P 107 Sud Ambohipo
17	Johnson	Mialy			femme	2023-05-11 05:05:02.185375	Mandroseza
18	JOHNSON	Mialy	100012034056	0334002850	femme	2023-05-11 05:09:47.663792	Mandroseza
19	RAZANAJATOVO	Aimé Régis	100023045067	0341898000	homme	2023-05-11 05:21:25.425911	Sud Ambohipo
20	ROOTSMAN	Na Lingi Yo	200023045067	0340000101	homme	2023-05-11 05:33:52.313274	Tuléar
21	Big 	Mj			homme	2023-05-11 05:37:07.920901	elle ville
22	SHYN	James	500012034056	0345067898	homme	2023-05-11 05:41:02.05901	Tamatave
23	RH	Denise	500012034056	0323202026	femme	2023-05-11 05:41:46.511947	Toamasina
24	BLi	Niaina			femme	2023-05-11 05:45:13.599635	cfsdfv
25	vsdd					2023-05-11 05:45:00.851765	
26	RATREMA	William	100023045067	0330161248	homme	2023-05-11 08:36:06.058008	Manakambahiny
27	RAGOVA	Treble	101012034056	0345610632	homme	2023-05-11 08:38:06.426073	Manakambahiny
28	JENAN	Jacques	102034012034		hommw	2023-05-11 08:39:01.828172	Itaosy
29	Henintsoa	andritiana	110011022760	0345908229	HOMME	2023-05-11 17:21:45.280643	ISAHA
30	TOTO	TATA			HOMME	2023-05-11 17:24:15.666259	ISADA
31	TOTO	TITI			F	2023-05-11 17:27:01.808392	ISADA
32	BLA	BLIE			femme	2023-05-12 06:47:35.765359	Isada
\.


--
-- Data for Name: voyager; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.voyager (id, id_client, id_car, destination, date_heure, num_place, nb_bagage) FROM stdin;
1	1	3	Fianarantsoa	2023-05-09 00:00:00	5	1
2	1	3	Moramanga	2023-05-09 12:40:00	3	4
3	8	3	Moramanga	2023-05-09 12:40:00	4	4
4	1	3	Tamatave	2023-05-09 00:00:00	6	2
5	10	3	Tamatave	2023-05-09 00:00:00	1	3
6	11	3	Tamatave	2023-05-09 00:00:00	2	3
7	8	3	Tamatave	2023-05-09 00:00:00	5	1
8	1	3	Tamatave	2023-05-09 00:00:00	7	2
9	8	4	Majunga	2023-05-13 07:30:00	1	2
10	12	4	Majunga	2023-05-13 07:30:00	2	2
11	1	4	Majunga	2023-05-13 07:30:00	3	1
12	1	3	Moramanga	2023-05-09 12:40:00	1	2
13	1	3	Tamatave	2023-05-09 00:00:00	3	2
14	8	4	Majunga	2023-05-10 20:00:00	1	2
15	13	4	Majunga	2023-05-10 20:00:00	2	2
16	14	4	Majunga	2023-05-10 20:00:00	3	2
17	13	4	Majunga	2023-05-10 20:00:00	6	2
18	13	4	Majunga	2023-05-10 20:00:00	4	1
19	14	4	Majunga	2023-05-10 20:00:00	5	2
20	15	4	Majunga	2023-05-10 20:00:00	10	2
21	16	4	Moramanga	2023-05-11 12:00:00	1	2
24	16	4	Majunga	2023-05-10 20:00:00	8	2
25	18	4	Majunga	2023-05-10 20:00:00	9	2
26	19	4	Majunga	2023-05-10 20:00:00	11	2
27	21	4	Majunga	2023-05-10 20:00:00	12	2
28	20	4	Majunga	2023-05-10 20:00:00	13	1
29	22	4	Majunga	2023-05-10 20:00:00	14	1
30	23	4	Majunga	2023-05-10 20:00:00	15	1
31	2	4	Majunga	2023-05-10 20:00:00	18	2
32	2	4	Majunga	2023-05-10 20:00:00	17	2
33	8	4	Majunga	2023-05-10 20:00:00	16	1
34	26	4	Moramanga	2023-05-11 12:00:00	4	2
35	27	4	Moramanga	2023-05-11 12:00:00	2	2
38	30	5	Fianarantsoa	2023-05-11 19:00:00	2	1
39	1	5	Fianarantsoa	2023-05-11 19:00:00	3	1
41	1	5	Tamatave	2023-05-12 19:00:00	1	2
42	32	5	Tamatave	2023-05-12 19:00:00	2	2
\.


--
-- Name: car_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.car_id_seq', 5, true);


--
-- Name: client_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.client_id_seq', 32, true);


--
-- Name: voyager_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.voyager_id_seq', 42, true);


--
-- Name: car car_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.car
    ADD CONSTRAINT car_pkey PRIMARY KEY (id);


--
-- Name: client client_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.client
    ADD CONSTRAINT client_pkey PRIMARY KEY (id);


--
-- Name: voyager voyager_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voyager
    ADD CONSTRAINT voyager_pkey PRIMARY KEY (id);


--
-- Name: voyager fk_car; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voyager
    ADD CONSTRAINT fk_car FOREIGN KEY (id_car) REFERENCES public.car(id) ON DELETE CASCADE;


--
-- Name: voyager voyager_id_client_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voyager
    ADD CONSTRAINT voyager_id_client_fkey FOREIGN KEY (id_client) REFERENCES public.client(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

