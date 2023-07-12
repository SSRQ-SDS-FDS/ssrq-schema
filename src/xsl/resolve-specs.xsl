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
    
    <xsl:template match="tei:specGrpRef">
        <xsl:variable name="target" select="@target" as="xs:string"/>
        <xsl:choose>
            <xsl:when test="$target => contains('#')">
                <xsl:variable name="file_and_part" as="xs:string+" select="$target => tokenize('#')"/>
                <xsl:variable name="content" as="node()" select="doc($file_and_part[1])//*[@xml:id = $file_and_part[2]]"/>
                <xsl:call-template name="process-included-spec">
                    <xsl:with-param name="context" as="node()" select="$content"/>
                </xsl:call-template>
            </xsl:when>
            <xsl:otherwise>
                <xsl:variable name="content" as="node()">
                    <xsl:copy-of select="doc($target)"/>
                </xsl:variable>
                <xsl:call-template name="process-included-spec">
                    <xsl:with-param name="context" as="node()" select="$content"/>
                </xsl:call-template>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>
    
    <xsl:template match="processing-instruction()" />
    
    <xsl:template name="process-included-spec">
        <xsl:param name="context" as="node()"/>
        <xsl:choose>
            <xsl:when test="$context/self::tei:specGrp">
                <xsl:apply-templates select="$context/node()"/>
            </xsl:when>
            <xsl:otherwise>
                <xsl:apply-templates select="$context"/>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>
    
    <xsl:template match="tei:remarks">
        <remarks type="ssrq-remarks">
            <xsl:copy-of select="@*"/>
            <xsl:apply-templates/>
        </remarks>
    </xsl:template>
    
</xsl:stylesheet>
