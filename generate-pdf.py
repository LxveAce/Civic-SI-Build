"""
Generate a comprehensive PDF of the 2009 Honda Civic SI (FG2) build documentation.
Reads all markdown files from the repo and combines them into a single organized PDF.

Usage: python generate-pdf.py
Output: 2009-Civic-SI-Build-Guide.pdf
"""

import os
import re
from fpdf import FPDF

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Ordered list of markdown files to include
FILE_ORDER = [
    "README.md",
    "docs/vehicle-specs.md",
    "docs/mod-order-and-maintenance.md",
    "01-Clutch/overview.md",
    "02-Cold-Air-Intake/overview.md",
    "03-Short-Shifter-and-Bushings/overview.md",
    "04-Engine-Mounts/overview.md",
    "05-Brakes/overview.md",
    "06-Strut-Bar/overview.md",
    "07-Hondata-FlashPro/overview.md",
    "08-Valved-Exhaust/overview.md",
    "09-Headers/overview.md",
    "10-Intake-Manifold/overview.md",
    "11-Pulleys-and-Harmonic-Balancer/overview.md",
    "12-Flex-Fuel-and-Fuel-System/overview.md",
    "13-Clutch-Hydraulics/overview.md",
]

OUTPUT_FILE = os.path.join(BASE_DIR, "2009-Civic-SI-Build-Guide.pdf")


def sanitize_text(text):
    """Replace Unicode characters that latin-1 can't encode."""
    replacements = {
        '\u2014': '--',   # em dash
        '\u2013': '-',    # en dash
        '\u2018': "'",    # left single quote
        '\u2019': "'",    # right single quote
        '\u201c': '"',    # left double quote
        '\u201d': '"',    # right double quote
        '\u2026': '...',  # ellipsis
        '\u2022': '-',    # bullet
        '\u00b0': 'deg',  # degree
        '\u2192': '->',   # right arrow
        '\u2190': '<-',   # left arrow
        '\u2248': '~',    # approximately
        '\u2264': '<=',   # less than or equal
        '\u2265': '>=',   # greater than or equal
        '\u00d7': 'x',    # multiplication sign
        '\u2502': '|',    # box drawing vertical
        '\u251c': '|',    # box drawing
        '\u2514': '\\',   # box drawing
        '\u2500': '-',    # box drawing horizontal
        '\u2510': '+',    # box drawing
        '\u250c': '+',    # box drawing
        '\u2518': '+',    # box drawing
        '\u2524': '|',    # box drawing
        '\u252c': '+',    # box drawing
        '\u2534': '+',    # box drawing
        '\u253c': '+',    # box drawing
        '\u2550': '=',    # box drawing double horizontal
        '\u2551': '||',   # box drawing double vertical
        '\u25ba': '>',    # right pointer
        '\u25c4': '<',    # left pointer
        '\u2660': '',     # spade
        '\u2665': '',     # heart
        '\u2666': '',     # diamond
        '\u2663': '',     # club
    }
    for char, replacement in replacements.items():
        text = text.replace(char, replacement)
    # Fallback: replace any remaining non-latin-1 chars
    result = []
    for ch in text:
        try:
            ch.encode('latin-1')
            result.append(ch)
        except UnicodeEncodeError:
            result.append('?')
    return ''.join(result)


class BuildGuidePDF(FPDF):
    """Custom PDF class for the build guide."""

    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=20)
        self.toc_entries = []  # (level, title, page_number)

    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "I", 8)
            self.set_text_color(120, 120, 120)
            self.cell(0, 8, "2009 Honda Civic SI (FG2) - Complete Build Guide", align="C")
            self.ln(4)
            # Thin line under header
            self.set_draw_color(200, 200, 200)
            self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
            self.ln(4)

    def footer(self):
        if self.page_no() > 1:
            self.set_y(-15)
            self.set_font("Helvetica", "I", 8)
            self.set_text_color(120, 120, 120)
            self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def add_title_page(self):
        """Create the title page."""
        self.add_page()
        self.ln(60)
        self.set_font("Helvetica", "B", 28)
        self.set_text_color(20, 20, 20)
        self.multi_cell(0, 14, "2009 Honda Civic SI (FG2)", align="C")
        self.ln(4)
        self.set_font("Helvetica", "", 20)
        self.set_text_color(60, 60, 60)
        self.multi_cell(0, 10, "Complete Build Guide", align="C")
        self.ln(20)
        # Divider line
        cx = self.w / 2
        self.set_draw_color(180, 180, 180)
        self.set_line_width(0.5)
        self.line(cx - 40, self.get_y(), cx + 40, self.get_y())
        self.ln(20)
        # Vehicle info
        self.set_font("Helvetica", "", 12)
        self.set_text_color(80, 80, 80)
        specs = [
            "Chassis: FG2 (8th Gen Coupe)",
            "Engine: K20Z3 -- 2.0L i-VTEC, 197 HP / 139 lb-ft (stock)",
            "Transmission: 6-Speed Manual",
            "Mileage: ~170,000 miles",
        ]
        for spec in specs:
            self.cell(0, 8, spec, align="C")
            self.ln(8)
        self.ln(30)
        self.set_font("Helvetica", "I", 10)
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, "Generated: 2026-04-16", align="C")

    def add_toc_page(self):
        """Add a table of contents page. Must be called after all content is added."""
        # We insert the TOC at page 2 after everything is built.
        pass

    def register_section(self, level, title):
        """Register a section for the TOC."""
        self.toc_entries.append((level, title, self.page_no()))


def strip_markdown_links(text):
    """Convert [text](url) to just text."""
    return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)


def strip_inline_formatting(text):
    """Remove bold/italic markers, inline code backticks, etc."""
    text = strip_markdown_links(text)
    # Bold+italic
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'\1', text)
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    # Inline code
    text = re.sub(r'`([^`]+)`', r'\1', text)
    # HTML-style line breaks
    text = text.replace('<br>', ' ').replace('<br/>', ' ').replace('<br />', ' ')
    return text


def parse_table(lines, start_idx):
    """Parse a markdown table starting at start_idx. Returns (rows, end_idx).
    Each row is a list of cell strings."""
    rows = []
    i = start_idx
    while i < len(lines):
        line = lines[i].strip()
        if not line.startswith('|'):
            break
        # Split cells
        cells = [c.strip() for c in line.split('|')]
        # Remove empty first/last from leading/trailing |
        if cells and cells[0] == '':
            cells = cells[1:]
        if cells and cells[-1] == '':
            cells = cells[:-1]
        # Skip separator rows (|---|---|)
        if all(re.match(r'^[-:]+$', c) for c in cells):
            i += 1
            continue
        rows.append(cells)
        i += 1
    return rows, i


def render_table(pdf, rows):
    """Render a table as aligned plain text."""
    if not rows:
        return

    # Strip markdown formatting from cells
    clean_rows = []
    for row in rows:
        clean_rows.append([strip_inline_formatting(c) for c in row])

    # Calculate column widths based on content
    num_cols = max(len(r) for r in clean_rows)
    # Pad rows to same number of columns
    for r in clean_rows:
        while len(r) < num_cols:
            r.append("")

    # Measure max width per column (in characters)
    col_char_widths = [0] * num_cols
    for r in clean_rows:
        for j, cell in enumerate(r):
            col_char_widths[j] = max(col_char_widths[j], len(cell))

    # Cap column widths and calculate PDF widths
    usable_width = pdf.w - pdf.l_margin - pdf.r_margin - 4  # small margin
    total_chars = sum(min(w, 60) for w in col_char_widths) or 1

    # Use font size 7 for tables to fit more content
    pdf.set_font("Courier", "", 7)
    char_width = pdf.get_string_width("M")

    col_pdf_widths = []
    for w in col_char_widths:
        capped = min(w, 60)
        col_pdf_widths.append(max((capped / total_chars) * usable_width, 12))

    # Ensure total doesn't exceed usable width
    total_w = sum(col_pdf_widths)
    if total_w > usable_width:
        scale = usable_width / total_w
        col_pdf_widths = [w * scale for w in col_pdf_widths]

    # Render header row with underline
    if clean_rows:
        pdf.set_font("Courier", "B", 7)
        header = clean_rows[0]
        x_start = pdf.get_x()
        for j, cell in enumerate(header):
            pdf.cell(col_pdf_widths[j], 5, cell[:60], border=0)
        pdf.ln(5)
        # Underline
        pdf.set_draw_color(160, 160, 160)
        pdf.line(x_start, pdf.get_y(), x_start + sum(col_pdf_widths), pdf.get_y())
        pdf.ln(1)

    # Render data rows
    pdf.set_font("Courier", "", 7)
    for row in clean_rows[1:]:
        # Check if we need a new page
        if pdf.get_y() + 10 > pdf.h - pdf.b_margin:
            pdf.add_page()
        row_height = 5
        # Check for cells that need wrapping
        x_start = pdf.get_x()
        y_start = pdf.get_y()

        # Simple single-line rendering (truncate long cells)
        for j, cell in enumerate(row):
            max_chars = int(col_pdf_widths[j] / char_width) if char_width > 0 else 60
            display = cell[:max_chars] if len(cell) > max_chars else cell
            pdf.cell(col_pdf_widths[j], row_height, display, border=0)
        pdf.ln(row_height)

    pdf.ln(3)
    # Reset font
    pdf.set_font("Helvetica", "", 10)


def render_code_block(pdf, code_lines):
    """Render a code/preformatted block."""
    pdf.set_font("Courier", "", 7.5)
    pdf.set_fill_color(245, 245, 245)
    pdf.set_draw_color(200, 200, 200)

    x = pdf.get_x()
    y = pdf.get_y()

    for line in code_lines:
        if pdf.get_y() + 5 > pdf.h - pdf.b_margin:
            pdf.add_page()
        # Replace tabs with spaces
        line = line.replace('\t', '    ')
        # Truncate very long lines
        if len(line) > 120:
            line = line[:117] + "..."
        pdf.cell(0, 4.5, "  " + line, fill=True, new_x="LMARGIN", new_y="NEXT")

    pdf.ln(3)
    pdf.set_font("Helvetica", "", 10)


def write_rich_line(pdf, text, base_size=10):
    """Write a line with bold segments rendered properly."""
    text = strip_markdown_links(text)
    text = re.sub(r'`([^`]+)`', r'\1', text)

    # Split on bold markers
    parts = re.split(r'(\*\*[^*]+\*\*)', text)
    for part in parts:
        if part.startswith('**') and part.endswith('**'):
            pdf.set_font("Helvetica", "B", base_size)
            pdf.write(6, part[2:-2])
        else:
            # Handle italic
            sub_parts = re.split(r'(\*[^*]+\*)', part)
            for sp in sub_parts:
                if sp.startswith('*') and sp.endswith('*') and len(sp) > 2:
                    pdf.set_font("Helvetica", "I", base_size)
                    pdf.write(6, sp[1:-1])
                else:
                    pdf.set_font("Helvetica", "", base_size)
                    pdf.write(6, sp)
    pdf.ln(6)


def process_markdown(pdf, content, filename):
    """Process markdown content and render it to the PDF."""
    content = sanitize_text(content)
    lines = content.split('\n')
    i = 0
    in_code_block = False
    code_lines = []
    first_heading_done = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Code block toggle
        if stripped.startswith('```'):
            if in_code_block:
                render_code_block(pdf, code_lines)
                code_lines = []
                in_code_block = False
            else:
                in_code_block = True
                code_lines = []
            i += 1
            continue

        if in_code_block:
            code_lines.append(line.rstrip())
            i += 1
            continue

        # Empty line
        if stripped == '':
            i += 1
            continue

        # Horizontal rule
        if re.match(r'^---+$', stripped) or re.match(r'^\*\*\*+$', stripped):
            pdf.set_draw_color(200, 200, 200)
            y = pdf.get_y() + 2
            pdf.line(pdf.l_margin, y, pdf.w - pdf.r_margin, y)
            pdf.ln(6)
            i += 1
            continue

        # Headings
        heading_match = re.match(r'^(#{1,6})\s+(.+)$', stripped)
        if heading_match:
            level = len(heading_match.group(1))
            title = strip_inline_formatting(heading_match.group(2))

            # Register for TOC (only level 1 and 2)
            if level <= 2:
                pdf.register_section(level, title)

            # Skip the very first H1 if it's the file's main title (already shown as section header)
            # But still render it for README since it's the intro
            if level == 1:
                if pdf.get_y() > 40:
                    pdf.ln(4)
                pdf.set_font("Helvetica", "B", 18)
                pdf.set_text_color(20, 20, 20)
                pdf.multi_cell(0, 10, title)
                pdf.ln(3)
            elif level == 2:
                if pdf.get_y() > 50:
                    pdf.ln(3)
                pdf.set_font("Helvetica", "B", 14)
                pdf.set_text_color(40, 40, 40)
                pdf.multi_cell(0, 8, title)
                pdf.ln(2)
            elif level == 3:
                pdf.ln(2)
                pdf.set_font("Helvetica", "B", 12)
                pdf.set_text_color(50, 50, 50)
                pdf.multi_cell(0, 7, title)
                pdf.ln(1)
            else:
                pdf.ln(1)
                pdf.set_font("Helvetica", "B", 10)
                pdf.set_text_color(60, 60, 60)
                pdf.multi_cell(0, 6, title)
                pdf.ln(1)

            pdf.set_text_color(0, 0, 0)
            i += 1
            continue

        # Table
        if stripped.startswith('|'):
            rows, end_idx = parse_table(lines, i)
            if rows:
                render_table(pdf, rows)
            i = end_idx
            continue

        # Bullet points
        bullet_match = re.match(r'^(\s*)([-*+])\s+(.+)$', stripped)
        if bullet_match:
            indent_level = len(line) - len(line.lstrip())
            indent = 4 + (indent_level // 2) * 4
            text = bullet_match.group(3)

            pdf.set_font("Helvetica", "", 10)
            pdf.set_text_color(0, 0, 0)
            x = pdf.l_margin + indent
            pdf.set_x(x)
            pdf.write(6, "- ")  # bullet character
            # Write the rest with rich formatting
            text = strip_markdown_links(text)
            text = re.sub(r'`([^`]+)`', r'\1', text)

            # Handle bold inline
            parts = re.split(r'(\*\*[^*]+\*\*)', text)
            for part in parts:
                if part.startswith('**') and part.endswith('**'):
                    pdf.set_font("Helvetica", "B", 10)
                    pdf.write(6, part[2:-2])
                else:
                    sub_parts = re.split(r'(\*[^*]+\*)', part)
                    for sp in sub_parts:
                        if sp.startswith('*') and sp.endswith('*') and len(sp) > 2:
                            pdf.set_font("Helvetica", "I", 10)
                            pdf.write(6, sp[1:-1])
                        else:
                            pdf.set_font("Helvetica", "", 10)
                            pdf.write(6, sp)
            pdf.ln(6)
            i += 1
            continue

        # Numbered list
        num_match = re.match(r'^(\d+)\.\s+(.+)$', stripped)
        if num_match:
            num = num_match.group(1)
            text = num_match.group(2)
            pdf.set_font("Helvetica", "", 10)
            pdf.set_text_color(0, 0, 0)
            pdf.set_x(pdf.l_margin + 4)
            pdf.write(6, f"{num}. ")
            # Rich text for the content
            text = strip_markdown_links(text)
            text = re.sub(r'`([^`]+)`', r'\1', text)
            parts = re.split(r'(\*\*[^*]+\*\*)', text)
            for part in parts:
                if part.startswith('**') and part.endswith('**'):
                    pdf.set_font("Helvetica", "B", 10)
                    pdf.write(6, part[2:-2])
                else:
                    pdf.set_font("Helvetica", "", 10)
                    pdf.write(6, part)
            pdf.ln(6)
            i += 1
            continue

        # Regular paragraph text
        # Collect consecutive non-special lines into a paragraph
        para_lines = []
        while i < len(lines):
            l = lines[i].strip()
            if l == '' or l.startswith('#') or l.startswith('|') or l.startswith('```'):
                break
            if re.match(r'^---+$', l) or re.match(r'^\*\*\*+$', l):
                break
            if re.match(r'^[-*+]\s+', l):
                break
            if re.match(r'^\d+\.\s+', l):
                break
            para_lines.append(l)
            i += 1

        if para_lines:
            para_text = ' '.join(para_lines)
            pdf.set_font("Helvetica", "", 10)
            pdf.set_text_color(0, 0, 0)
            write_rich_line(pdf, para_text)
            pdf.ln(2)
            continue

        i += 1


def build_toc(pdf):
    """Build a table of contents from registered sections.
    This creates a new PDF with the TOC inserted after the title page."""
    return pdf.toc_entries


def main():
    pdf = BuildGuidePDF()
    pdf.set_left_margin(15)
    pdf.set_right_margin(15)

    # Title page
    pdf.add_title_page()

    # We'll build content first, then insert TOC
    # Reserve a TOC page placeholder -- we'll track entries and add TOC after

    # Process each markdown file
    section_pages = []  # (title, page_number)

    for filepath in FILE_ORDER:
        full_path = os.path.join(BASE_DIR, filepath)
        if not os.path.exists(full_path):
            print(f"  [SKIP] {filepath} -- file not found")
            continue

        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Derive a section title from the first heading in the file
        first_heading = None
        for line in content.split('\n'):
            m = re.match(r'^#\s+(.+)$', line.strip())
            if m:
                first_heading = strip_inline_formatting(m.group(1))
                break
        if not first_heading:
            first_heading = filepath
        first_heading = sanitize_text(first_heading)

        # Add a new page for this section
        pdf.add_page()
        page_num = pdf.page_no()
        section_pages.append((first_heading, page_num))

        print(f"  [OK] {filepath} (page {page_num})")

        # Process the markdown content
        process_markdown(pdf, content, filepath)

    # Now create final PDF with TOC inserted after title page
    # Since fpdf2 doesn't support inserting pages easily, we rebuild
    final = BuildGuidePDF()
    final.set_left_margin(15)
    final.set_right_margin(15)

    # Title page
    final.add_title_page()

    # TOC page
    final.add_page()
    final.set_font("Helvetica", "B", 22)
    final.set_text_color(20, 20, 20)
    final.cell(0, 14, "Table of Contents", align="C")
    final.ln(16)

    final.set_draw_color(200, 200, 200)
    final.line(final.l_margin, final.get_y(), final.w - final.r_margin, final.get_y())
    final.ln(8)

    # Each section entry -- page numbers will be offset by 1 (for TOC page)
    for title, page_num in section_pages:
        adjusted_page = page_num + 1  # +1 because we're inserting TOC page
        final.set_font("Helvetica", "", 11)
        final.set_text_color(40, 40, 40)

        # Truncate long titles
        display_title = title if len(title) < 70 else title[:67] + "..."

        # Title on left, page number on right with dots
        title_width = final.get_string_width(display_title)
        page_str = str(adjusted_page)
        page_width = final.get_string_width(page_str)
        available = final.w - final.l_margin - final.r_margin - title_width - page_width - 4
        dot_width = final.get_string_width(".")
        num_dots = max(3, int(available / dot_width)) if dot_width > 0 else 20
        dots = " " + "." * num_dots + " "

        final.cell(title_width + 2, 8, display_title)
        final.set_font("Helvetica", "", 9)
        final.set_text_color(150, 150, 150)
        final.cell(0, 8, dots + page_str, align="R")
        final.ln(8)

        final.set_text_color(40, 40, 40)

    # Now re-process all markdown files for the final PDF
    for filepath in FILE_ORDER:
        full_path = os.path.join(BASE_DIR, filepath)
        if not os.path.exists(full_path):
            continue

        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()

        final.add_page()
        process_markdown(final, content, filepath)

    # Save
    final.output(OUTPUT_FILE)
    print(f"\nPDF saved to: {OUTPUT_FILE}")
    print(f"Total pages: {final.page_no()}")


if __name__ == "__main__":
    main()
