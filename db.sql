--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1
-- Dumped by pg_dump version 14.1

-- Started on 2022-09-19 10:14:15 +07

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
-- TOC entry 211 (class 1259 OID 16420)
-- Name: accounts; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.accounts (
    account_number character(10) NOT NULL,
    user_id integer NOT NULL,
    bank character(30) NOT NULL,
    balance numeric DEFAULT 0 NOT NULL,
    status character(20) DEFAULT 'active'::bpchar NOT NULL
);


--
-- TOC entry 212 (class 1259 OID 16432)
-- Name: transactions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.transactions (
    transaction_id uuid NOT NULL,
    datetime timestamp(6) with time zone DEFAULT now() NOT NULL,
    account_number character(10) NOT NULL,
    transaction_account character(10) DEFAULT NULL::bpchar,
    channel character(30) NOT NULL,
    transaction_name character(30) NOT NULL,
    indicator "char" NOT NULL,
    amount double precision NOT NULL,
    description text,
    parent_id uuid
);


--
-- TOC entry 209 (class 1259 OID 16390)
-- Name: users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.users (
    id integer NOT NULL,
    name character(255) NOT NULL,
    birthdate date,
    gender character(10) DEFAULT NULL::bpchar,
    nationality character(50) DEFAULT NULL::bpchar,
    identity_id character(100),
    is_verify boolean DEFAULT false,
    activated_phone character(20) DEFAULT NULL::bpchar,
    activated_email character(100) DEFAULT NULL::bpchar
);


--
-- TOC entry 210 (class 1259 OID 16419)
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.users ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 3598 (class 0 OID 16420)
-- Dependencies: 211
-- Data for Name: accounts; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.accounts (account_number, user_id, bank, balance, status) FROM stdin;
4356605536	2	TTB                           	2000.0	active              
5569981327	1	KBANK                         	1400.0	active              
6584779139	3	KBANK                         	1000.0	active              
1266300742	1	KTB                           	1600.0	active              
6953870038	4	TTB                           	1700.0	active              
7348571047	2	SCB                           	400.0	active              
7511541340	2	KTB                           	1500.0	active              
\.


--
-- TOC entry 3599 (class 0 OID 16432)
-- Dependencies: 212
-- Data for Name: transactions; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.transactions (transaction_id, datetime, account_number, transaction_account, channel, transaction_name, indicator, amount, description, parent_id) FROM stdin;
c823ebcc-fa69-4b25-a2f9-491f4c132fde	2022-09-19 09:20:59.957954+07	1266300742	\N	iOS                           	deposit                       	C	1000	Open an account.	\N
d7d129b8-a263-48ad-93dd-03f5c330b7bc	2022-09-19 09:21:17.579618+07	5569981327	\N	iOS                           	deposit                       	C	700	Open an account.	\N
1bca0e87-7835-4089-ac96-9ef2443f4642	2022-09-19 09:21:42.366583+07	4356605536	\N	Android                       	deposit                       	C	1500	Open an account.	\N
9d006fc5-79ca-41b9-bd1a-f30a4d473277	2022-09-19 09:21:51.572764+07	7348571047	\N	Android                       	deposit                       	C	600	Open an account.	\N
8333693c-d2d7-435c-ac93-325441d0e513	2022-09-19 09:22:03.608898+07	7511541340	\N	Web                           	deposit                       	C	500	Open an account.	\N
0d485ce9-f4d2-4600-916e-75d22a566a68	2022-09-19 09:22:32.348591+07	6584779139	\N	iOS                           	deposit                       	C	1300	Open an account.	\N
09dea74c-954f-406c-ae1e-250e18f02e6d	2022-09-19 09:23:10.501875+07	6953870038	\N	Android                       	deposit                       	C	3000	Open an account.	\N
9db783b8-3f46-4041-84e1-69d5dd4b8a9b	2022-09-19 09:34:06.523432+07	4356605536	\N	Web                           	deposit                       	C	500	\N	\N
b142f243-7c56-4a59-99f2-33e74255f291	2022-09-19 09:34:15.6409+07	6584779139	\N	iOS                           	deposit                       	C	300	\N	\N
c7ce74d3-5d57-44a6-b713-6838c9fef090	2022-09-19 09:34:37.620933+07	5569981327	\N	Android                       	deposit                       	C	700	\N	\N
83d6e345-52c7-4cc7-82ae-a2b22e94998c	2022-09-19 09:35:04.34999+07	7511541340	\N	iOS                           	deposit                       	C	900	\N	\N
c75107ae-44e1-4fe3-aa9b-63bc0675de6b	2022-09-19 09:39:01.00926+07	6953870038	\N	Web                           	withdraw                      	D	-1000	\N	\N
7a1e4efc-162f-46ab-928a-7b9cf8b6a755	2022-09-19 09:39:48.241742+07	7348571047	\N	Android                       	withdraw                      	D	-100	\N	\N
67437d91-6211-4d32-a212-315136216545	2022-09-19 09:40:00.474342+07	7511541340	\N	iOS                           	withdraw                      	D	-300	\N	\N
671444c1-31df-4dad-b2ac-bdebdd3d1ad3	2022-09-19 09:43:27.724923+07	6584779139	1266300742	Web                           	withdraw                      	D	-600	\N	\N
5f017437-5733-44a9-8e28-2b77c1b1c809	2022-09-19 09:43:27.747902+07	1266300742	6584779139	Web                           	deposit                       	C	600	\N	671444c1-31df-4dad-b2ac-bdebdd3d1ad3
f9b59ee6-9689-41d2-80bb-5aed3ca1e117	2022-09-19 09:43:58.148263+07	6953870038	7348571047	iOS                           	withdraw                      	D	-300	\N	\N
e5545447-00a7-4e1e-8f97-841f4f6f898b	2022-09-19 09:43:58.173598+07	7348571047	6953870038	iOS                           	deposit                       	C	300	\N	f9b59ee6-9689-41d2-80bb-5aed3ca1e117
c6e19545-3f57-4d1f-9499-50d3e3ec30f3	2022-09-19 09:44:18.667557+07	7348571047	7511541340	Android                       	withdraw                      	D	-400	\N	\N
6144a263-3c3b-464f-a560-abccf8212f7b	2022-09-19 09:44:18.694711+07	7511541340	7348571047	Android                       	deposit                       	C	400	\N	c6e19545-3f57-4d1f-9499-50d3e3ec30f3
\.


--
-- TOC entry 3596 (class 0 OID 16390)
-- Dependencies: 209
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.users (id, name, birthdate, gender, nationality, identity_id, is_verify, activated_phone, activated_email) FROM stdin;
1	Arisha Barron                                                                                                                                                                                                                                                  	\N	\N	\N	\N	f	\N	\N
2	Branden Gibson                                                                                                                                                                                                                                                 	\N	\N	\N	\N	f	\N	\N
3	Rhonda Church                                                                                                                                                                                                                                                  	\N	\N	\N	\N	f	\N	\N
4	Georgina Hazel                                                                                                                                                                                                                                                 	\N	\N	\N	\N	f	\N	\N
\.


--
-- TOC entry 3605 (class 0 OID 0)
-- Dependencies: 210
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.users_id_seq', 4, true);


--
-- TOC entry 3451 (class 2606 OID 16445)
-- Name: accounts accounts_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts
    ADD CONSTRAINT accounts_pkey PRIMARY KEY (account_number);


--
-- TOC entry 3449 (class 2606 OID 16394)
-- Name: users bank_account_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT bank_account_pkey PRIMARY KEY (id);


--
-- TOC entry 3453 (class 2606 OID 16438)
-- Name: transactions transactions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.transactions
    ADD CONSTRAINT transactions_pkey PRIMARY KEY (transaction_id);


--
-- TOC entry 3456 (class 2606 OID 16525)
-- Name: transactions transaction_id_ref; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.transactions
    ADD CONSTRAINT transaction_id_ref FOREIGN KEY (parent_id) REFERENCES public.transactions(transaction_id) MATCH FULL NOT VALID;


--
-- TOC entry 3606 (class 0 OID 0)
-- Dependencies: 3456
-- Name: CONSTRAINT transaction_id_ref ON transactions; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON CONSTRAINT transaction_id_ref ON public.transactions IS 'for void transaction';


--
-- TOC entry 3455 (class 2606 OID 16446)
-- Name: transactions transactions_accounts; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.transactions
    ADD CONSTRAINT transactions_accounts FOREIGN KEY (account_number) REFERENCES public.accounts(account_number) MATCH FULL NOT VALID;


--
-- TOC entry 3454 (class 2606 OID 16427)
-- Name: accounts users_accounts; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.accounts
    ADD CONSTRAINT users_accounts FOREIGN KEY (user_id) REFERENCES public.users(id) MATCH FULL;


-- Completed on 2022-09-19 10:14:15 +07

--
-- PostgreSQL database dump complete
--

