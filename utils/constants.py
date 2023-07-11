from pathlib import Path

PROJECT_DIR = Path(__file__).parent.parent.absolute()
DIST_DIR = PROJECT_DIR / "dist"
SRC_DIR = PROJECT_DIR / "src"
EXAMPLES_DIR = SRC_DIR / "examples"
COMMON_DIR = SRC_DIR / "common"
ELEMENTS_DIR = SRC_DIR / "elements"
XSLT_BASE = PROJECT_DIR / SRC_DIR / "xsl"
TEI_STYLESHEETS = PROJECT_DIR / SRC_DIR / "lib/tei_stylesheets/odds"
XSLTS = {
    "change-start": XSLT_BASE / "change-rng-start.xsl",
    "clean": XSLT_BASE / "clean-compiled.xsl",
    "meta": XSLT_BASE / "fill-meta.xsl",
    "odd2odd": TEI_STYLESHEETS / "odd2odd.xsl",
    "odd2rng": TEI_STYLESHEETS / "odd2relax.xsl",
    "path": XSLT_BASE / "resolve-path.xsl",
    "specs": XSLT_BASE / "resolve-specs.xsl",
    "vars": XSLT_BASE / "resolve-sch-let.xsl",
    "xi": XSLT_BASE / "resolve-xi.xsl",
}
SPECIFIED_ELEMENTS = r'target="elements/(\w+)\.xml"'
