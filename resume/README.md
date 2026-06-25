# Modular Resume System

This repository implements a modular resume compilation system. It splits the core resume content (jobs, education, projects, skills, activities) into individual reusable LaTeX modules. This allows you to automatically generate two completely different resume formats from a single source of truth:

1. **🎨 Design Resume (`main.pdf`)**: A polished, modern two-column layout using the `altacv.cls` class. Perfect for human reviewers, networking, and direct applications.
2. **🤖 ATS Resume (`main_single_column.pdf`)**: A highly optimized, linearly readable single-column layout using standard `article.cls`. Designed to be 100% readable by automated Applicant Tracking Systems (ATS) with tabular skills alignment and clean spacing.

Both resumes are designed to fit on **exactly one page**.

---

## 📂 Project Directory Structure

```
├── README.md                      # This documentation file
├── generate.py                    # Python build script (compiles PDFs, cleans files, generates previews)
│
├── wrappers/
│   ├── main.tex                   # Two-column layout entrypoint
│   └── main_single_column.tex     # Single-column layout entrypoint
│
└── shared modules (input files):
    ├── education.tex              # School and minor details
    ├── experience.tex             # Work history bullets
    ├── projects.tex               # Project bullet points & tech stacks
    ├── skills.tex                 # Technical skills categories and tags
    └── activities.tex             # Extracurricular involvements
```

---

## 🛠️ How to Edit

To update your resume, you only need to modify the shared text modules. Any changes here will propagate to **both** outputs automatically:

*   **Edit Education:** Modify [education.tex](file:///home/atom/Projects/Personal/resume/resume/education.tex)
*   **Edit Work Experience:** Modify [experience.tex](file:///home/atom/Projects/Personal/resume/resume/experience.tex)
*   **Edit Projects:** Modify [projects.tex](file:///home/atom/Projects/Personal/resume/resume/projects.tex)
*   **Edit Skills:** Modify [skills.tex](file:///home/atom/Projects/Personal/resume/resume/skills.tex)
*   **Edit Activities:** Modify [activities.tex](file:///home/atom/Projects/Personal/resume/resume/activities.tex)

---

## 🚀 How to Compile

A helper build script `generate.py` is included to manage compilation and clean-up.

### Prerequisites

Make sure you have a LaTeX distribution (like TeX Live) and Python 3 installed on your system.

```bash
# Ubuntu/Debian LaTeX dependencies:
sudo apt install texlive-latex-extra texlive-fonts-recommended poppler-utils
```

### Build Commands

Run the script from the project directory:

1. **Standard Compile (Recommended)**:
   Compiles both resumes and deletes temporary log/aux files.
   ```bash
   python3 generate.py
   ```

2. **Compile with Visual PNG Previews**:
   Compiles the resumes and renders PNG screenshots (`resume_page-1.png` and `resume_page_single_column-1.png`) for instant visual checks.
   ```bash
   python3 generate.py --preview
   ```

3. **Debug Compile**:
   Compiles the PDFs but leaves the `.aux`, `.log`, and `.out` files intact.
   ```bash
   python3 generate.py --no-clean
   ```

---

## 💡 Custom LaTeX Layout Notes

### Spacing & Margin Balancing
*   To keep the documents strictly on **one page**, the margins are set tightly (`0.35in` for single-column).
*   If you add substantial new text that overflows to a second page, you can slightly reduce `itemsep` in `main_single_column.tex` (e.g. `\setlist[itemize]{itemsep=0.7pt}`) or adjust margins inside `\geometry`.

### Skills Table Alignment
*   The single-column layout redirects the skills list from `skills.tex` into a tabular environment. 
*   It does this by locally redefining the `\cvsubsection` macro inside `main_single_column.tex` to serve as a cell delimiter and row end (`&` and `\\`). You do not need to format the raw `skills.tex` file as a table!
