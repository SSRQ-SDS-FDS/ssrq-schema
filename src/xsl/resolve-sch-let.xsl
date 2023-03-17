<?xml version="1.0" encoding="utf-8"?>
<!-- Adapted from https://github.com/TEIC/Stylesheets/blob/dev/odds/extract-sch.xsl -->
<xsl:stylesheet xmlns:teix="http://www.tei-c.org/ns/Examples"
                xmlns:xi="http://www.w3.org/2001/XInclude" xmlns:rng="http://relaxng.org/ns/structure/1.0"
                xmlns:tei="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron"
                xmlns="http://purl.oclc.org/dsdl/schematron" xmlns:xs="http://www.w3.org/2001/XMLSchema"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="3.0"
                exclude-result-prefixes="tei rng teix xi xs #default">
    
    
    <xsl:output method="xml" indent="yes"/>
    <xsl:mode on-no-match="shallow-copy"/>
    
    <xsl:template match="sch:let[starts-with(@value, '{{') and ends-with(@value, '}}')]">
        <sch:let>
            <xsl:variable name="xpathValue" as="xs:string"
                select="@value => replace('^\{\{(.*)\}\}$', '$1')"/>
            <xsl:variable name="resolvedValue">
                <xsl:evaluate xpath="$xpathValue" context-item="root(.)" as="xs:string"/>
            </xsl:variable>
            <xsl:attribute name="name" select="@name"/>
            <xsl:attribute name="value" select="$resolvedValue"> </xsl:attribute>
        </sch:let>
    </xsl:template>
    
    
    
</xsl:stylesheet>
