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
    
    <xsl:param name="path_base" as="xs:string"/>
    
    
    <xsl:template match="tei:specGrpRef[@target]">
        <specGrpRef>
            <xsl:copy-of select="@* except @target | node()"/>
            <xsl:attribute name="target" select="($path_base, @target) => string-join('/')"/>
        </specGrpRef>
    </xsl:template>
    
</xsl:stylesheet>
