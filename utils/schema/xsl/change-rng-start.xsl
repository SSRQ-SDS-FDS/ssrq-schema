<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns="http://relaxng.org/ns/structure/1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema" exclude-result-prefixes="xs" version="3.0" xpath-default-namespace="http://relaxng.org/ns/structure/1.0">
  <xsl:output method="xml" indent="yes"/>
  <xsl:mode on-no-match="shallow-copy"/>
  <xsl:param name="start-el-name" as="xs:string"/>
  <xsl:template match="start">
    <start>
      <ref name="{$start-el-name}"/>
    </start>
  </xsl:template>
</xsl:stylesheet>
