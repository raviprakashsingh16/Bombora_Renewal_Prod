CREATE TABLE IF NOT EXISTS bombora_dwh.f_adat_bombora
(
    company character varying(256) ,
    domain character varying(256) ,
    size character varying(256) ,
    industry character varying(256) ,
    category character varying(256) ,
    topic character varying(256) ,
    composite_score character varying(256) ,
    metro_area character varying(1000) ,
    domain_origin character varying(256) ,
    bucket_code character varying(256) ,
    datestamp date );
