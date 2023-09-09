from pathlib import Path

# Directories
PROJECT_DIR = Path(__file__).parent.parent.parent.absolute()

BUILD_DIR = PROJECT_DIR / "build"

SRC_DIR = PROJECT_DIR / "src"
SCHEMA_DIR = SRC_DIR / "schema"
COMMONS_DIR = SCHEMA_DIR / "commons"
ELEMENTS_DIR = SCHEMA_DIR / "elements"
EXAMPLES_DIR = SCHEMA_DIR / "examples"

UTILS_DIR = PROJECT_DIR / "utils"
SCHEMA_UTILS_DIR = UTILS_DIR / "schema"
TEI_STYLESHEETS = SCHEMA_UTILS_DIR / "lib/tei_stylesheets/odds"
XSLT_BASE_DIR = SCHEMA_UTILS_DIR / "xsl"

# XSLT Stylesheets
XSLTS = {
    "change-start": XSLT_BASE_DIR / "change-rng-start.xsl",
    "clean": XSLT_BASE_DIR / "clean-compiled.xsl",
    "meta": XSLT_BASE_DIR / "fill-meta.xsl",
    "odd2odd": TEI_STYLESHEETS / "odd2odd.xsl",
    "odd2rng": TEI_STYLESHEETS / "odd2relax.xsl",
    "path": XSLT_BASE_DIR / "resolve-path.xsl",
    "specs": XSLT_BASE_DIR / "resolve-specs.xsl",
    "vars": XSLT_BASE_DIR / "resolve-sch-let.xsl",
    "xi": XSLT_BASE_DIR / "resolve-xi.xsl",
}

# Other Configuration Options
DOCS_LANG = ["de", "fr"]
SUPPORTED_FILE_TYPES = ("md", "gif", "jpg", "jpeg", "png", "svg")
