<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:xs="http://www.w3.org/2001/XMLSchema" exclude-result-prefixes="xs"
                xmlns:tei="http://www.tei-c.org/ns/1.0" xmlns:odd2md="http://ssrq-sds-fds.ch/ns/odd2md"
                expand-text="true" version="3.0">
    
    <xsl:output method="xml"/>
    
    <xsl:mode on-no-match="deep-skip"/>
    
    <xsl:param name="lang" as="xs:string"/>
    <xsl:param name="empty-line" as="xs:string" select="'&#xA;&#xA;'"/>
    <!--
         : Positive values as defined in att.combinable
         :
         : @see: https://tei-c.org/release/doc/tei-p5-doc/en/html/ref-att.combinable.html
    -->
    <xsl:param name="pos-modes" as="xs:string+" select="('add', 'change', 'replace')"/>
    
    <xsl:template match="/">
        <schemaSpec>
            <xsl:apply-templates select="//tei:elementSpec"/>
        </schemaSpec>
    </xsl:template>
    
    <xsl:template match="tei:elementSpec">
        <elementSpec ident="{./@ident}">
            <xsl:variable name="title" select="odd2md:make-heading(1, ./@ident)" as="xs:string"/>
            <xsl:variable name="el-description" as="xs:string+">
                <xsl:variable name="description" as="xs:string*">
                    <xsl:apply-templates select="tei:desc[@xml:lang = $lang]"/>
                </xsl:variable>
                <xsl:value-of select="if ($description => empty()) then $lang || '-description missing for ' || @ident else $description"/>
            </xsl:variable>
            <xsl:variable name="attr-descriptions" as="xs:string?">
                <!--
                     : Create a variable with the attribute descriptions
                     : only if there are attributes with mode add, change or replace
                -->
                <xsl:if test="tei:attList[tei:attDef[@mode = $pos-modes]]">
                    <xsl:variable name="att-title" as="xs:string" select="''"/>
                    <xsl:variable name="att-descriptions" as="xs:string+">
                        <xsl:apply-templates select="tei:attList"/>
                    </xsl:variable>
                    <xsl:value-of select="odd2md:join-components-with-empty-lines(($att-title, $att-descriptions))"/>
                </xsl:if>
            </xsl:variable>
            <xsl:value-of
                select="odd2md:join-components-with-empty-lines(($title, $el-description, $attr-descriptions))"/>
        </elementSpec>
    </xsl:template>
    
    <xsl:template match="tei:desc">
        <xsl:apply-templates select="node() | text()"/>
    </xsl:template>
    
    <xsl:template match="tei:attList">
        <!-- Continue here ...
             <xsl:apply-templates select="tei:attDef[@mode = $pos-modes]"/>
        -->
        <xsl:text>foo-bar</xsl:text>
    </xsl:template>
    
    <xsl:template match="tei:gi">
        <xsl:variable name="el-name" select="./text() => normalize-space()"/>
        <xsl:text>[{$el-name}]({$el-name}.md)</xsl:text>
    </xsl:template>
    
    <xsl:template match="tei:att">
        <xsl:variable name="att-name" select="./text() => normalize-space()"/>
        <xsl:text>[@{$att-name}](#{$att-name})</xsl:text>
    </xsl:template>
    
    <xsl:template match="text()">
        <xsl:copy-of select="."/>
    </xsl:template>
    
    <!--
         : A helper function to make a heading
         :
         :
         : @param $level The level of the heading as xs:integer
         : @param $title The title of the heading as xs:string
         : @return The heading as xs:string
    -->
    <xsl:function name="odd2md:make-heading" as="xs:string">
        <xsl:param name="level" as="xs:integer"/>
        <xsl:param name="title" as="xs:string"/>
        <xsl:sequence select="
            (for $i in 1 to $level
                return
                    '#') => string-join('') || ' ' || $title"/>
    </xsl:function>
    
    <!--
         : A helper function to join components with empty lines
         : the space of the components is normalized
         :
         :
         : @param $components The components to join as xs:string+
         : @return The components joined with empty lines as xs:string
    -->
    <xsl:function name="odd2md:join-components-with-empty-lines" as="xs:string">
        <xsl:param name="components" as="xs:string+"/>
        <xsl:sequence select="
            (for $c in $components
                return
                    $c => normalize-space()) => string-join($empty-line)"/>
    </xsl:function>
    
</xsl:stylesheet>
