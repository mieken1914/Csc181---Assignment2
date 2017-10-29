--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

--
-- Name: address; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE address AS (
	house_num integer,
	street character varying(10),
	brgy character varying(20),
	city character varying(15)
);


ALTER TYPE public.address OWNER TO postgres;

--
-- Name: fullname; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE fullname AS (
	f_name character varying(20),
	l_name character varying(20),
	m_name character varying(20)
);


ALTER TYPE public.fullname OWNER TO postgres;

--
-- Name: year_enum; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE year_enum AS ENUM (
    '1st Year',
    '2nd Year',
    '3rd Year',
    '4th Year',
    '5th Year',
    'Irregular Year'
);


ALTER TYPE public.year_enum OWNER TO postgres;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: college; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE college (
    idnum integer NOT NULL,
    name character varying(10)
);


ALTER TABLE public.college OWNER TO postgres;

--
-- Name: course; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE course (
    idnum integer NOT NULL,
    name character varying(20),
    college_id integer
);


ALTER TABLE public.course OWNER TO postgres;

--
-- Name: student; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE student (
    idnum integer NOT NULL,
    name fullname,
    gender character(1),
    college_id integer,
    course_id integer,
    year_lvl year_enum,
    address address,
    bdate date
);


ALTER TABLE public.student OWNER TO postgres;

--
-- Data for Name: college; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY college (idnum, name) FROM stdin;
1001	CIT
1002	CNSM
1003	CBAA
1004	CPA
1005	COE
1006	COA
1007	CED
1008	KFCIAAS
1009	CHARM
1010	COF
\.


--
-- Data for Name: course; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY course (idnum, name, college_id) FROM stdin;
2101	BS-ComputerScience	1001
2102	BS-IT	1001
2201	BS-Biology	1002
2202	BS-Zoology	1002
2203	BS-Math	1002
2204	BS-Physics	1002
2501	BS-CE	1005
2502	BS-ECE	1005
2801	BS-IR	1008
\.


--
-- Data for Name: student; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY student (idnum, name, gender, college_id, course_id, year_lvl, address, bdate) FROM stdin;
201248001	(Apipah,Polao,Desso)	F	1002	2201	4th Year	(211,"Diana St","Brgy Lancaf","Iligan City")	1995-02-06
201248469	(Al-Ryan,Calimba,Ali)	M	1001	2102	3rd Year	(45,"Ali St","Bo. Salam","Marawi City")	1995-05-21
201248655	(Arnold,Radaza,"dela Cruz")	M	1005	2501	Irregular Year	(23,"3rd St","Bo. Salam","Marawi City")	1995-05-21
201248557	(As-Harrie,Dianalan,Domado)	M	1001	2101	1st Year	(111,"Alauya Ave","Moncado Col","Marawi City")	1995-01-14
\.


--
-- Name: college_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY college
    ADD CONSTRAINT college_pkey PRIMARY KEY (idnum);


--
-- Name: course_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY course
    ADD CONSTRAINT course_pkey PRIMARY KEY (idnum);


--
-- Name: student_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY student
    ADD CONSTRAINT student_pkey PRIMARY KEY (idnum);


--
-- Name: course_college_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY course
    ADD CONSTRAINT course_college_id_fkey FOREIGN KEY (college_id) REFERENCES college(idnum);


--
-- Name: student_college_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY student
    ADD CONSTRAINT student_college_id_fkey FOREIGN KEY (college_id) REFERENCES college(idnum);


--
-- Name: student_course_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY student
    ADD CONSTRAINT student_course_id_fkey FOREIGN KEY (course_id) REFERENCES course(idnum);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

