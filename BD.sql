--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.6
-- Dumped by pg_dump version 9.6.6

-- Started on 2017-12-04 16:10:31 -02

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 1 (class 3079 OID 12393)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2229 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_with_oids = false;

--
-- TOC entry 188 (class 1259 OID 19584)
-- Name: analise_de_requisitos; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE analise_de_requisitos (
    id integer NOT NULL,
    nome character varying(255) NOT NULL,
    descricao text NOT NULL
);


--
-- TOC entry 187 (class 1259 OID 19582)
-- Name: analise_de_requisitos_analisederequisitos_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE analise_de_requisitos_analisederequisitos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2230 (class 0 OID 0)
-- Dependencies: 187
-- Name: analise_de_requisitos_analisederequisitos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE analise_de_requisitos_analisederequisitos_id_seq OWNED BY analise_de_requisitos.id;


--
-- TOC entry 194 (class 1259 OID 19729)
-- Name: equipe; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE equipe (
    id integer NOT NULL,
    ar_id_id integer NOT NULL,
    dev_id_id integer NOT NULL
);


--
-- TOC entry 193 (class 1259 OID 19727)
-- Name: analise_de_requisitos_equipe_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE analise_de_requisitos_equipe_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2231 (class 0 OID 0)
-- Dependencies: 193
-- Name: analise_de_requisitos_equipe_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE analise_de_requisitos_equipe_id_seq OWNED BY equipe.id;


--
-- TOC entry 196 (class 1259 OID 19772)
-- Name: atividade; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE atividade (
    id integer NOT NULL,
    descricao text NOT NULL,
    data_inicio date,
    data_fim date,
    prazo date,
    dev_id_id integer NOT NULL,
    req_id_id integer NOT NULL
);


--
-- TOC entry 195 (class 1259 OID 19770)
-- Name: atividade_atividade_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE atividade_atividade_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2232 (class 0 OID 0)
-- Dependencies: 195
-- Name: atividade_atividade_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE atividade_atividade_id_seq OWNED BY atividade.id;


--
-- TOC entry 192 (class 1259 OID 19620)
-- Name: desenvolvedor; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE desenvolvedor (
    id integer NOT NULL,
    nome character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    senha character varying(255) NOT NULL
);


--
-- TOC entry 191 (class 1259 OID 19618)
-- Name: desenvolvedor_desenvolvedor_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE desenvolvedor_desenvolvedor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2233 (class 0 OID 0)
-- Dependencies: 191
-- Name: desenvolvedor_desenvolvedor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE desenvolvedor_desenvolvedor_id_seq OWNED BY desenvolvedor.id;


--
-- TOC entry 198 (class 1259 OID 19849)
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


--
-- TOC entry 197 (class 1259 OID 19847)
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2234 (class 0 OID 0)
-- Dependencies: 197
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- TOC entry 186 (class 1259 OID 19573)
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


--
-- TOC entry 185 (class 1259 OID 19571)
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2235 (class 0 OID 0)
-- Dependencies: 185
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;


--
-- TOC entry 199 (class 1259 OID 19857)
-- Name: django_session; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


--
-- TOC entry 190 (class 1259 OID 19595)
-- Name: requisito; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE requisito (
    id integer NOT NULL,
    nome character varying(255) NOT NULL,
    tipo character varying(255) NOT NULL,
    detalhes text,
    ar_id_id integer NOT NULL
);


--
-- TOC entry 189 (class 1259 OID 19593)
-- Name: requisito_requisito_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE requisito_requisito_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2236 (class 0 OID 0)
-- Dependencies: 189
-- Name: requisito_requisito_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE requisito_requisito_id_seq OWNED BY requisito.id;


--
-- TOC entry 2052 (class 2604 OID 19587)
-- Name: analise_de_requisitos id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY analise_de_requisitos ALTER COLUMN id SET DEFAULT nextval('analise_de_requisitos_analisederequisitos_id_seq'::regclass);


--
-- TOC entry 2056 (class 2604 OID 19775)
-- Name: atividade id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY atividade ALTER COLUMN id SET DEFAULT nextval('atividade_atividade_id_seq'::regclass);


--
-- TOC entry 2054 (class 2604 OID 19623)
-- Name: desenvolvedor id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY desenvolvedor ALTER COLUMN id SET DEFAULT nextval('desenvolvedor_desenvolvedor_id_seq'::regclass);


--
-- TOC entry 2057 (class 2604 OID 19852)
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- TOC entry 2051 (class 2604 OID 19576)
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);


--
-- TOC entry 2055 (class 2604 OID 19732)
-- Name: equipe id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY equipe ALTER COLUMN id SET DEFAULT nextval('analise_de_requisitos_equipe_id_seq'::regclass);


--
-- TOC entry 2053 (class 2604 OID 19598)
-- Name: requisito id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY requisito ALTER COLUMN id SET DEFAULT nextval('requisito_requisito_id_seq'::regclass);


--
-- TOC entry 2211 (class 0 OID 19584)
-- Dependencies: 188
-- Data for Name: analise_de_requisitos; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO analise_de_requisitos VALUES (1, 'Laboratório Santa Maria', 'Criação de um software de armazenamento e recuperação de dados de pacientes para o diagnóstico molecular.');


--
-- TOC entry 2237 (class 0 OID 0)
-- Dependencies: 187
-- Name: analise_de_requisitos_analisederequisitos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('analise_de_requisitos_analisederequisitos_id_seq', 1, true);


--
-- TOC entry 2238 (class 0 OID 0)
-- Dependencies: 193
-- Name: analise_de_requisitos_equipe_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('analise_de_requisitos_equipe_id_seq', 4, true);


--
-- TOC entry 2219 (class 0 OID 19772)
-- Dependencies: 196
-- Data for Name: atividade; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO atividade VALUES (1, 'Implementação da tabela de paciente no banco de dados.', '2017-10-23', NULL, '2017-10-26', 2, 1);
INSERT INTO atividade VALUES (2, 'Implementação da função de restrição de agendamento de uma única máquina ao mesmo tempo.', '2017-10-20', NULL, '2017-10-25', 7, 4);
INSERT INTO atividade VALUES (3, 'Implementação do tipo de máquina para tempo de uso.', '2017-10-20', '2017-10-21', '2017-10-22', 3, 4);


--
-- TOC entry 2239 (class 0 OID 0)
-- Dependencies: 195
-- Name: atividade_atividade_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('atividade_atividade_id_seq', 3, true);


--
-- TOC entry 2215 (class 0 OID 19620)
-- Dependencies: 192
-- Data for Name: desenvolvedor; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO desenvolvedor VALUES (1, 'Rafael Alves Dias', 'rafaeldias@mac0350.com', '123');
INSERT INTO desenvolvedor VALUES (2, 'Matheus Fernandes', 'matheusfernandes@mac0350.com', '123');
INSERT INTO desenvolvedor VALUES (3, 'Alice Sousa', 'alicesousa@mac0350.com', '123');
INSERT INTO desenvolvedor VALUES (4, 'Vinicius Rocha', 'viniciusrocha@mac0350.com', '123');
INSERT INTO desenvolvedor VALUES (5, 'Douglas Rodrigues', 'douglasrodrigues@mac0350.com', '123');
INSERT INTO desenvolvedor VALUES (6, 'Gabriela Correia', 'gabrielacorreia@mac0350.com', '123');
INSERT INTO desenvolvedor VALUES (7, 'Gabriela Oliveira', 'gabrielaoliveira@mac0350.com', '123');
INSERT INTO desenvolvedor VALUES (8, 'Brenda Cunha', 'brendacunha@mac0350.com', '123');
INSERT INTO desenvolvedor VALUES (9, 'Fábio Almeida Santos', 'fabiosantos@mac0350.com', '123');
INSERT INTO desenvolvedor VALUES (10, 'Carolina Silva', 'carolinasilva@mac0350.com', '123');


--
-- TOC entry 2240 (class 0 OID 0)
-- Dependencies: 191
-- Name: desenvolvedor_desenvolvedor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('desenvolvedor_desenvolvedor_id_seq', 10, true);


--
-- TOC entry 2221 (class 0 OID 19849)
-- Dependencies: 198
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO django_content_type VALUES (1, 'contenttypes', 'contenttype');
INSERT INTO django_content_type VALUES (2, 'sessions', 'session');
INSERT INTO django_content_type VALUES (3, 'desenvolvedor', 'desenvolvedor');
INSERT INTO django_content_type VALUES (4, 'analise_de_requisitos', 'equipe');
INSERT INTO django_content_type VALUES (5, 'analise_de_requisitos', 'analisederequisitos');
INSERT INTO django_content_type VALUES (6, 'requisito', 'requisito');
INSERT INTO django_content_type VALUES (7, 'atividade', 'atividade');


--
-- TOC entry 2241 (class 0 OID 0)
-- Dependencies: 197
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('django_content_type_id_seq', 7, true);


--
-- TOC entry 2209 (class 0 OID 19573)
-- Dependencies: 186
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO django_migrations VALUES (1, 'analise_de_requisitos', '0001_initial', '2017-12-04 16:08:30.648636-02');
INSERT INTO django_migrations VALUES (2, 'requisito', '0001_initial', '2017-12-04 16:08:30.838946-02');
INSERT INTO django_migrations VALUES (3, 'requisito', '0002_auto_20171202_1137', '2017-12-04 16:08:30.849593-02');
INSERT INTO django_migrations VALUES (4, 'requisito', '0003_auto_20171202_1141', '2017-12-04 16:08:30.871766-02');
INSERT INTO django_migrations VALUES (5, 'requisito', '0004_auto_20171202_1207', '2017-12-04 16:08:30.883839-02');
INSERT INTO django_migrations VALUES (6, 'desenvolvedor', '0001_initial', '2017-12-04 16:08:31.335038-02');
INSERT INTO django_migrations VALUES (7, 'desenvolvedor', '0002_auto_20171128_0028', '2017-12-04 16:08:31.46691-02');
INSERT INTO django_migrations VALUES (8, 'desenvolvedor', '0003_auto_20171129_2336', '2017-12-04 16:08:31.533205-02');
INSERT INTO django_migrations VALUES (9, 'desenvolvedor', '0004_auto_20171201_1822', '2017-12-04 16:08:31.599461-02');
INSERT INTO django_migrations VALUES (10, 'desenvolvedor', '0005_auto_20171202_1914', '2017-12-04 16:08:31.906034-02');
INSERT INTO django_migrations VALUES (11, 'desenvolvedor', '0006_auto_20171202_2026', '2017-12-04 16:08:31.955839-02');
INSERT INTO django_migrations VALUES (12, 'analise_de_requisitos', '0002_equipe', '2017-12-04 16:08:32.120235-02');
INSERT INTO django_migrations VALUES (13, 'analise_de_requisitos', '0003_auto_20171203_1255', '2017-12-04 16:08:32.153448-02');
INSERT INTO django_migrations VALUES (14, 'desenvolvedor', '0007_auto_20171202_2030', '2017-12-04 16:08:32.195845-02');
INSERT INTO django_migrations VALUES (15, 'requisito', '0005_atividade', '2017-12-04 16:08:32.426094-02');
INSERT INTO django_migrations VALUES (16, 'requisito', '0006_auto_20171202_2126', '2017-12-04 16:08:32.476595-02');
INSERT INTO django_migrations VALUES (17, 'atividade', '0001_initial', '2017-12-04 16:08:32.706939-02');
INSERT INTO django_migrations VALUES (18, 'atividade', '0002_auto_20171202_2212', '2017-12-04 16:08:32.739915-02');
INSERT INTO django_migrations VALUES (19, 'atividade', '0003_auto_20171202_2324', '2017-12-04 16:08:33.427027-02');
INSERT INTO django_migrations VALUES (20, 'atividade', '0004_auto_20171203_1115', '2017-12-04 16:08:34.146064-02');
INSERT INTO django_migrations VALUES (21, 'atividade', '0005_auto_20171203_1122', '2017-12-04 16:08:34.176928-02');
INSERT INTO django_migrations VALUES (22, 'atividade', '0006_auto_20171203_1255', '2017-12-04 16:08:34.202624-02');
INSERT INTO django_migrations VALUES (23, 'contenttypes', '0001_initial', '2017-12-04 16:08:34.334674-02');
INSERT INTO django_migrations VALUES (24, 'contenttypes', '0002_remove_content_type_name', '2017-12-04 16:08:34.36773-02');
INSERT INTO django_migrations VALUES (25, 'desenvolvedor', '0008_auto_20171203_1255', '2017-12-04 16:08:34.392378-02');
INSERT INTO django_migrations VALUES (26, 'requisito', '0007_auto_20171203_1255', '2017-12-04 16:08:34.417228-02');
INSERT INTO django_migrations VALUES (27, 'sessions', '0001_initial', '2017-12-04 16:08:34.64841-02');


--
-- TOC entry 2242 (class 0 OID 0)
-- Dependencies: 185
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('django_migrations_id_seq', 27, true);


--
-- TOC entry 2222 (class 0 OID 19857)
-- Dependencies: 199
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 2217 (class 0 OID 19729)
-- Dependencies: 194
-- Data for Name: equipe; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO equipe VALUES (1, 1, 2);
INSERT INTO equipe VALUES (2, 1, 3);
INSERT INTO equipe VALUES (3, 1, 7);
INSERT INTO equipe VALUES (4, 1, 5);


--
-- TOC entry 2213 (class 0 OID 19595)
-- Dependencies: 190
-- Data for Name: requisito; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO requisito VALUES (1, 'Paciente', 'Dado', 'Todas as pessoas que são tratadas no laboratório devem possuir um cadastro, contendo: nome, data de nascimento, situação civil, RG, CPF, endereço, complemento, CEP, email, telefone.', 1);
INSERT INTO requisito VALUES (2, 'Diagnóstico Molecular', 'Dado', 'Representa o diagnóstico de uma doença hereditária. As informações são: causa molecular da doença, alguma deleção de genes ou pedaços de cromossomos, variantes diferentes do que o encontrado na população saudável.', 1);
INSERT INTO requisito VALUES (3, 'Cadastro de informações do paciente', 'Funcional', 'Qualquer funcionário pode fazer o cadastro e alteração das informações dos pacientes.', 1);
INSERT INTO requisito VALUES (4, 'Agendamento de máquina', 'Funcional', 'Qualquer funcionário pode agendar o uso das máquinas. Um mesmo funcionário não pode agendar mais de uma máquina ao mesmo tempo. Cada tipo de máquina pode ter um tempo limite de uso.', 1);


--
-- TOC entry 2243 (class 0 OID 0)
-- Dependencies: 189
-- Name: requisito_requisito_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('requisito_requisito_id_seq', 4, true);


--
-- TOC entry 2061 (class 2606 OID 19592)
-- Name: analise_de_requisitos analise_de_requisitos_analisederequisitos_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY analise_de_requisitos
    ADD CONSTRAINT analise_de_requisitos_analisederequisitos_pkey PRIMARY KEY (id);


--
-- TOC entry 2073 (class 2606 OID 19734)
-- Name: equipe analise_de_requisitos_equipe_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY equipe
    ADD CONSTRAINT analise_de_requisitos_equipe_pkey PRIMARY KEY (id);


--
-- TOC entry 2076 (class 2606 OID 19780)
-- Name: atividade atividade_atividade_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY atividade
    ADD CONSTRAINT atividade_atividade_pkey PRIMARY KEY (id);


--
-- TOC entry 2067 (class 2606 OID 19662)
-- Name: desenvolvedor desenvolvedor_desenvolvedor_email_fc003dcc_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY desenvolvedor
    ADD CONSTRAINT desenvolvedor_desenvolvedor_email_fc003dcc_uniq UNIQUE (email);


--
-- TOC entry 2069 (class 2606 OID 19628)
-- Name: desenvolvedor desenvolvedor_desenvolvedor_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY desenvolvedor
    ADD CONSTRAINT desenvolvedor_desenvolvedor_pkey PRIMARY KEY (id);


--
-- TOC entry 2079 (class 2606 OID 19856)
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- TOC entry 2081 (class 2606 OID 19854)
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- TOC entry 2059 (class 2606 OID 19581)
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- TOC entry 2084 (class 2606 OID 19864)
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- TOC entry 2064 (class 2606 OID 19603)
-- Name: requisito requisito_requisito_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY requisito
    ADD CONSTRAINT requisito_requisito_pkey PRIMARY KEY (id);


--
-- TOC entry 2070 (class 1259 OID 19745)
-- Name: analise_de_requisitos_equipe_ar_id_id_fa26c021; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX analise_de_requisitos_equipe_ar_id_id_fa26c021 ON equipe USING btree (ar_id_id);


--
-- TOC entry 2071 (class 1259 OID 19746)
-- Name: analise_de_requisitos_equipe_dev_id_id_137ec932; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX analise_de_requisitos_equipe_dev_id_id_137ec932 ON equipe USING btree (dev_id_id);


--
-- TOC entry 2074 (class 1259 OID 19791)
-- Name: atividade_atividade_dev_id_id_fa158693; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX atividade_atividade_dev_id_id_fa158693 ON atividade USING btree (dev_id_id);


--
-- TOC entry 2077 (class 1259 OID 19792)
-- Name: atividade_atividade_req_id_id_e227d9a0; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX atividade_atividade_req_id_id_e227d9a0 ON atividade USING btree (req_id_id);


--
-- TOC entry 2065 (class 1259 OID 19663)
-- Name: desenvolvedor_desenvolvedor_email_fc003dcc_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX desenvolvedor_desenvolvedor_email_fc003dcc_like ON desenvolvedor USING btree (email varchar_pattern_ops);


--
-- TOC entry 2082 (class 1259 OID 19866)
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_session_expire_date_a5c62663 ON django_session USING btree (expire_date);


--
-- TOC entry 2085 (class 1259 OID 19865)
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_session_session_key_c0390e0f_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- TOC entry 2062 (class 1259 OID 19609)
-- Name: requisito_requisito_ar_id_id_b22131a0; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX requisito_requisito_ar_id_id_b22131a0 ON requisito USING btree (ar_id_id);


--
-- TOC entry 2087 (class 2606 OID 19735)
-- Name: equipe analise_de_requisito_ar_id_id_fa26c021_fk_analise_d; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY equipe
    ADD CONSTRAINT analise_de_requisito_ar_id_id_fa26c021_fk_analise_d FOREIGN KEY (ar_id_id) REFERENCES analise_de_requisitos(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2088 (class 2606 OID 19740)
-- Name: equipe analise_de_requisito_dev_id_id_137ec932_fk_desenvolv; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY equipe
    ADD CONSTRAINT analise_de_requisito_dev_id_id_137ec932_fk_desenvolv FOREIGN KEY (dev_id_id) REFERENCES desenvolvedor(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2089 (class 2606 OID 19781)
-- Name: atividade atividade_atividade_dev_id_id_fa158693_fk_desenvolv; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY atividade
    ADD CONSTRAINT atividade_atividade_dev_id_id_fa158693_fk_desenvolv FOREIGN KEY (dev_id_id) REFERENCES desenvolvedor(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2090 (class 2606 OID 19786)
-- Name: atividade atividade_atividade_req_id_id_e227d9a0_fk_requisito; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY atividade
    ADD CONSTRAINT atividade_atividade_req_id_id_e227d9a0_fk_requisito FOREIGN KEY (req_id_id) REFERENCES requisito(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2086 (class 2606 OID 19604)
-- Name: requisito requisito_requisito_ar_id_id_b22131a0_fk_analise_d; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY requisito
    ADD CONSTRAINT requisito_requisito_ar_id_id_b22131a0_fk_analise_d FOREIGN KEY (ar_id_id) REFERENCES analise_de_requisitos(id) DEFERRABLE INITIALLY DEFERRED;


-- Completed on 2017-12-04 16:10:31 -02

--
-- PostgreSQL database dump complete
--

