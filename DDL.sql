-- Database: vertebra

-- DROP DATABASE IF EXISTS vertebra;

CREATE DATABASE vertebra
    WITH
    OWNER = user_db
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Venezuela.1252'
    LC_CTYPE = 'Spanish_Venezuela.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

GRANT TEMPORARY, CONNECT ON DATABASE vertebra TO PUBLIC;

GRANT ALL ON DATABASE vertebra TO user_db;

-- Table: public.api_post

-- DROP TABLE IF EXISTS public.api_post;

CREATE TABLE IF NOT EXISTS public.api_post
(
    id bigint NOT NULL DEFAULT nextval('api_post_id_seq'::regclass),
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    is_removed boolean NOT NULL,
    url_image text COLLATE pg_catalog."default" NOT NULL,
    date_published timestamp with time zone NOT NULL,
    date_updated timestamp with time zone NOT NULL,
    CONSTRAINT api_post_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.api_post
    OWNER to user_db;

	-- Table: public.historial

-- DROP TABLE IF EXISTS public.historial;

CREATE TABLE IF NOT EXISTS public.historial
(
    id integer NOT NULL DEFAULT nextval('historial_id_seq'::regclass),
    id_img integer NOT NULL,
    status boolean NOT NULL,
    step integer NOT NULL,
    start_time timestamp without time zone NOT NULL,
    end_time timestamp without time zone,
    CONSTRAINT historial_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.historial
    OWNER to postgres;

-- Table: public.log_error

-- DROP TABLE IF EXISTS public.log_error;

CREATE TABLE IF NOT EXISTS public.log_error
(
    id integer NOT NULL DEFAULT nextval('log_error_id_seq'::regclass),
    "time" timestamp without time zone NOT NULL,
    step integer NOT NULL,
    description character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT log_error_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.log_error
    OWNER to postgres;