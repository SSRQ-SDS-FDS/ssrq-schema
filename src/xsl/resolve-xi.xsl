<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:xs="http://www.w3.org/2001/XMLSchema"
                xmlns:tei="http://www.tei-c.org/ns/1.0"
                xmlns:xi="http://www.w3.org/2001/XInclude"
                xmlns="http://www.tei-c.org/ns/1.0"
                exclude-result-prefixes="#all"
                expand-text="yes"
                version="3.0">
    
    
    <xsl:output method="xml" indent="yes"/>
    <xsl:mode on-no-match="shallow-copy"/>
    
    <xsl:param name="path_base" as="xs:string"/>
    
    <xsl:template match="xi:include">
        <xsl:variable name="target" select="($path_base, @href) => string-join('/')" as="xs:string"/>
        <xsl:choose>
            <xsl:when test=".[@xpointer]">
                <xsl:variable name="id" as="xs:string" select="@xpointer"/>
                <xsl:variable name="content" as="node()" select="doc($target)//*[@xml:id = $id]"/>
                <xsl:apply-templates select="$content"/>
            </xsl:when>
            <xsl:otherwise>
                <xsl:variable name="content" as="node()">
                    <xsl:copy-of select="doc($target)"/>
                </xsl:variable>
                <xsl:apply-templates select="$content"/>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>
    
    <!-- A hack, because the compiled odd get's cleaned afterwards – see clean-compiled.xsl -->
    <xsl:template match="tei:exemplum[not(@type)]">
        <exemplum type="ssrq-doc-example">
            <xsl:copy-of select="@*"/>
            <xsl:apply-templates/>
        </exemplum>
    </xsl:template>
    
    <xsl:template match="processing-instruction()" />
    
</xsl:stylesheet>
