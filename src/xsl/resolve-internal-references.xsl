<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:tei="http://www.tei-c.org/ns/1.0"
    xmlns:rng="http://relaxng.org/ns/structure/1.0" xmlns="http://www.tei-c.org/ns/1.0"
    expand-text="yes" exclude-result-prefixes="#all" version="3.0">

    <!--
    : This stylesheets includes some templates to resolve all internal references,
    : which are part of the compiled odd. Afterwards the result can easily be used
    : for the documentation.
    :
    : @author: Bastian Politycki, Swiss Law Sources
    -->


    <xsl:output method="xml" indent="yes"/>

    <xsl:param name="modes" as="xs:string+"
        select="('add-att-descriptions', 'resolve-keys-and-names')"/>

    <xsl:template match="/">
        <xsl:variable name="initial-odd" select="."/>
        <!-- We are using xsl:iterate here, because this gives us the ability to test the results from each mode seperatly -->
        <xsl:iterate select="$modes">
            <xsl:param name="odd" as="node()+" select="$initial-odd"/>
            <xsl:on-completion select="$odd"/>
            <xsl:variable name="mode-name" select="." as="xs:string"/>
            <xsl:variable name="odd-result" as="node()+">
                <xsl:choose>
                    <xsl:when test="$mode-name = 'add-att-descriptions'">
                        <xsl:apply-templates select="$odd" mode="add-att-descriptions"/>
                    </xsl:when>
                    <xsl:when test="$mode-name = 'resolve-keys-and-names'">
                        <xsl:apply-templates select="$odd" mode="resolve-keys-and-names"/>
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:message
                            select="'Unknown mode: &quot;' || $mode-name || '&quot;, returning odd.'"/>
                        <xsl:copy-of select="$odd"/>
                    </xsl:otherwise>

                </xsl:choose>
            </xsl:variable>
            <xsl:next-iteration>
                <xsl:with-param name="odd" select="$odd-result"/>
            </xsl:next-iteration>
        </xsl:iterate>
    </xsl:template>

    <!-- Copy all nodes per Mode -->
    <xsl:template match="@* | node()" mode="#all">
        <xsl:copy>
            <xsl:apply-templates select="@*" mode="#current"/>
            <xsl:apply-templates mode="#current"/>
        </xsl:copy>
    </xsl:template>

    <!--
    : A template to fill every tei:attDef with corresponding tei:desc-elements,
    : which are missing, if the attributes are inherited from a class.
    :
    : @author: Bastian Politycki
    -->
    <xsl:template
        match="tei:attDef[not(tei:desc)][ancestor::tei:elementSpec][not(@mode = 'delete')]"
        mode="add-att-descriptions">
        <xsl:variable name="classes" as="xs:string*"
            select="ancestor::tei:elementSpec//tei:memberOf/@key"/>
        <xsl:variable name="context" as="element(tei:attDef)" select="."/>
        <xsl:copy>
            <xsl:copy-of select="@*"/>
            <xsl:choose>
                <xsl:when test="$classes => exists()">
                    <xsl:variable name="descriptions" as="element(tei:desc)*">
                        <xsl:copy-of
                            select="$context/root()//tei:attDef[@ident = $context/@ident][ancestor::tei:classSpec/@ident = $classes]/tei:desc"
                        />
                    </xsl:variable>
                    <xsl:choose>
                        <xsl:when test="$descriptions => exists()">
                            <xsl:copy-of select="$descriptions"/>
                        </xsl:when>
                        <xsl:otherwise>
                            <xsl:copy-of
                                select="$context/root()//tei:attDef[@ident = $context/@ident][ancestor::tei:classSpec]/tei:desc"
                            />
                        </xsl:otherwise>
                    </xsl:choose>

                </xsl:when>
                <xsl:otherwise>
                    <xsl:copy-of
                        select="$context/root()//tei:attDef[@ident = $context/@ident][ancestor::tei:classSpec]/tei:desc"
                    />
                </xsl:otherwise>
            </xsl:choose>
            <xsl:copy-of select="node()"/>
        </xsl:copy>
    </xsl:template>

    <!--
    : A template to resolve the values of datatypes, which are referenced by tei:dataRef.
    :
    : @author: Bastian Politycki
    -->
    <xsl:template match="tei:datatype[tei:dataRef[@key]]" mode="resolve-keys-and-names">
        <xsl:copy-of select="tei:find-referenced-by-key(./tei:dataRef, ./tei:dataRef/@key)"/>
    </xsl:template>

    <xsl:function name="tei:find-referenced-by-key" as="element(tei:valList)?">
        <xsl:param name="context" as="element(tei:dataRef)"/>
        <xsl:param name="key" as="xs:string"/>
        <xsl:variable name="dataSpec" as="element(tei:dataSpec)"
            select="$context/root()//tei:dataSpec[@ident = $key]"/>
        <xsl:variable name="output" as="element(tei:valList)?">
            <xsl:choose>
                <xsl:when test="$dataSpec[.//tei:valList]">
                    <xsl:sequence select="$dataSpec//tei:valList"/>
                </xsl:when>
                <xsl:otherwise/>
            </xsl:choose>
        </xsl:variable>
        <xsl:sequence select="$output"/>
    </xsl:function>



</xsl:stylesheet>
