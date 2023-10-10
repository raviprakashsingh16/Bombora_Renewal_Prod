$fileDir = Split-Path -Parent $MyInvocation.MyCommand.Path
cd $fileDir
java '-Dtalend.component.manager.m2.repository=%cd%/../lib' '-Xms1024M' '-Xmx2048M' -cp '.;../lib/routines.jar;../lib/log4j-slf4j-impl-2.13.2.jar;../lib/log4j-api-2.13.2.jar;../lib/log4j-core-2.13.2.jar;../lib/components-common-oauth-0.37.0.jar;../lib/ST4-4.3.jar;../lib/org.apache.oltu.oauth2.client-1.0.0.jar;../lib/daikon-exception-0.31.12.jar;../lib/httpclient-4.5.13.jar;../lib/accessors-smart-2.4.7.jar;../lib/javax.inject-1.jar;../lib/avro-1.8.1.jar;../lib/checker-qual-3.5.0.jar;../lib/jackson-core-asl-1.9.15-TALEND.jar;../lib/auto-service-1.0-rc2.jar;../lib/guava-30.0-jre.jar;../lib/json-path-2.1.0.jar;../lib/antlr4-runtime-4.7.jar;../lib/crypto-utils-0.31.12.jar;../lib/auto-common-0.3.jar;../lib/maven-resolver-util-1.3.1.jar;../lib/maven-resolver-spi-1.3.1.jar;../lib/antlr-runtime-3.5.2.jar;../lib/commons-compress-1.21.jar;../lib/failureaccess-1.0.1.jar;../lib/jackson-mapper-asl-1.9.15-TALEND.jar;../lib/pax-url-aether-support-2.6.2.jar;../lib/components-api-0.37.0.jar;../lib/commons-lang3-3.10.jar;../lib/pax-url-aether-2.6.2.jar;../lib/commons-beanutils-1.9.4.jar;../lib/jackson-annotations-2.11.4.jar;../lib/jsr305-1.3.9.jar;../lib/paranamer-2.7.jar;../lib/org.apache.oltu.oauth2.common-1.0.0.jar;../lib/commons-text-1.8.jar;../lib/error_prone_annotations-2.3.4.jar;../lib/jboss-marshalling-2.0.12.Final.jar;../lib/j2objc-annotations-1.3.jar;../lib/force-partner-api-53.0.0.jar;../lib/maven-resolver-impl-1.3.1.jar;../lib/components-salesforce-definition-0.37.0.jar;../lib/org.osgi.service.component.annotations-1.3.0.jar;../lib/maven-resolver-api-1.3.1.jar;../lib/dom4j-2.1.3.jar;../lib/daikon-0.31.12.jar;../lib/force-wsc-53.0.0.jar;../lib/json-smart-2.4.7.jar;../lib/slf4j-api-1.7.29.jar;../lib/commons-codec-1.14.jar;../lib/snappy-java-1.1.1.3.jar;../lib/talend-proxy-1.0.2.jar;../lib/talendcsv-1.0.0.jar;../lib/xz-1.5.jar;../lib/commons-collections-3.2.2.jar;../lib/jackson-core-2.11.4.jar;../lib/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar;../lib/commons-configuration2-2.7.jar;../lib/joda-time-2.8.2.jar;../lib/components-common-0.37.0.jar;../lib/components-salesforce-runtime-0.37.0.jar;../lib/httpcore-4.4.13.jar;../lib/jackson-databind-2.11.4.jar;../lib/commons-logging-1.2.jar;../lib/json-20140107.jar;../lib/json-io-4.9.9-TALEND.jar;../lib/javax.servlet-api-3.1.0.jar;../lib/postgresql-42.2.14.jar;../lib/talend-codegen-utils.jar;f_intent_lead_agg_to_sf_lead_json_1_0.jar;' nq_ai.f_intent_lead_agg_to_sf_lead_json_1_0.f_intent_lead_agg_to_sf_lead_json --context=Default $args
