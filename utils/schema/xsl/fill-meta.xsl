<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:tei="http://www.tei-c.org/ns/1.0" xmlns="http://www.tei-c.org/ns/1.0" exclude-result-prefixes="#all" expand-text="yes" version="3.0">
  <xsl:output method="xml" indent="yes"/>
  <xsl:mode on-no-match="shallow-copy"/>
  <xsl:param name="version" as="xs:string" select="'1.0.0'"/>
  <xsl:template match="tei:teiHeader//tei:date">
    <date when="{current-date()}"/>
  </xsl:template>
  <xsl:template match="tei:idno">
    <idno>
      <xsl:value-of select="$version"/>
    </idno>
  </xsl:template>
</xsl:stylesheet>
