<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:tei="http://www.tei-c.org/ns/1.0" xmlns="http://www.tei-c.org/ns/1.0" exclude-result-prefixes="#all" expand-text="yes" version="3.0">
  <xsl:output method="xml" indent="yes"/>
  <xsl:mode on-no-match="shallow-copy"/>
  <xsl:param name="languages" as="xs:string+" select="('de', 'en', 'fr')"/>
  <xsl:template match="tei:exemplum">
    <!-- Filters all TEI examples and removes the hack introduced by resolve-xi.xsl -->
    <xsl:if test=".[@type][@xml:lang = $languages][@type = 'ssrq-doc-example']">
      <exemplum>
        <xsl:copy-of select="node()|@* except @type"/>
      </exemplum>
    </xsl:if>
  </xsl:template>
  <xsl:template match="tei:desc[not(@xml:lang = $languages)]"/>
  <xsl:template match="tei:gloss[not(@xml:lang = $languages)]"/>
  <xsl:template match="tei:remarks">
    <!-- Filters all TEI remarks and removes the hack introduced by resolve-specs.xsl -->
    <xsl:if test=".[@type][@xml:lang = $languages][@type = 'ssrq-remarks']">
      <remarks>
        <xsl:copy-of select="node()|@* except @type"/>
      </remarks>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>
