CREATE OR REPLACE VIEW aiml.v_pre_loaded_topics
AS WITH v_pre_loaded_topics AS (
         SELECT stg_pre_loaded_topics.topic_id,
            stg_pre_loaded_topics.theme,
            stg_pre_loaded_topics.category,
            stg_pre_loaded_topics.topic_name,
            stg_pre_loaded_topics.description
           FROM staging.stg_pre_loaded_topics
        )
 SELECT v_pre_loaded_topics.topic_id,
    v_pre_loaded_topics.theme,
    v_pre_loaded_topics.category,
    v_pre_loaded_topics.topic_name,
    v_pre_loaded_topics.description
   FROM v_pre_loaded_topics;