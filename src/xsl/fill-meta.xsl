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
    
    <xsl:param name="title" as="xs:string" select="'Schema of the Swiss Law Sources'"/>
    <xsl:param name="authors" as="xs:string*"/>
    <xsl:param name="version" as="xs:string" select="'1.0.0'"/>
    <xsl:param name="desc" as="xs:string" select="''"/>
    
    <xsl:template match="//tei:title[parent::tei:titleStmt]">
        <title>
            <xsl:value-of select="$title"/>
        </title>
    </xsl:template>
    
    <xsl:template match="tei:author[ancestor::tei:teiHeader]">
        <xsl:for-each select="$authors">
            <author>
                <xsl:value-of select="."/>
            </author>
        </xsl:for-each>
    </xsl:template>
    
    <xsl:template match="tei:teiHeader//tei:date">
        <date when="{current-date()}"/>
    </xsl:template>
    
    <xsl:template match="tei:idno[@type = 'version']">
        <idno type="version">
            <xsl:value-of select="$version"/>
        </idno>
    </xsl:template>
    
    <xsl:template match="tei:sourceDesc/tei:p">
        <p>
            <xsl:value-of select="$desc"/>
        </p>
    </xsl:template>
    
    
    
    
</xsl:stylesheet>
