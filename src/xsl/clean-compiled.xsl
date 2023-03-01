<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:tei="http://www.tei-c.org/ns/1.0"
    xmlns="http://www.tei-c.org/ns/1.0"
    exclude-result-prefixes="#all"
    expand-text="yes"
    version="3.0">
    
    
    <xsl:output method="xml" indent="yes"/>
    <xsl:mode on-no-match="shallow-copy"/>
    
    <xsl:param name="languages" as="xs:string+" select="('de', 'en', 'fr')"/>
    
    
    <xsl:template match="tei:exemplum[not(@xml:lang = $languages) or not(@type = 'ssrq-doc-example')]"/>
    
    <xsl:template match="tei:desc[not(@xml:lang = $languages)]"/>
    
    <xsl:template match="tei:gloss[not(@xml:lang = $languages)]"/>
    
    <xsl:template match="tei:remarks"/>
    
    
    
    
</xsl:stylesheet>
