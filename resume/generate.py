#!/usr/bin/env python3
import argparse
import subprocess
import glob
import os
import sys

def build_pdf(tex_file):
    print(f"Compiling {tex_file}...")
    try:
        # Run pdflatex twice for cross-references/hyperlinks
        result = subprocess.run(["pdflatex", "-interaction=nonstopmode", tex_file], capture_output=True, text=True)
        if result.returncode != 0:
            print(result.stdout, file=sys.stderr)
            print(result.stderr, file=sys.stderr)
            result.check_returncode()
        
        # Second run
        result = subprocess.run(["pdflatex", "-interaction=nonstopmode", tex_file], capture_output=True, text=True)
        if result.returncode != 0:
            print(result.stdout, file=sys.stderr)
            print(result.stderr, file=sys.stderr)
            result.check_returncode()
            
        print(f"Successfully built {tex_file.replace('.tex', '.pdf')}")
    except Exception as e:
        print(f"Error compiling {tex_file}. Check details above.", file=sys.stderr)
        sys.exit(1)

def generate_preview(pdf_file, output_prefix):
    print(f"Generating preview for {pdf_file}...")
    try:
        subprocess.run(["pdftoppm", "-png", "-r", "150", pdf_file, output_prefix], check=True)
        print(f"Generated preview {output_prefix}-1.png")
    except subprocess.CalledProcessError as e:
        print(f"Error generating preview for {pdf_file}.", file=sys.stderr)

def clean_temp_files():
    print("Cleaning auxiliary build files...")
    exts = ["*.aux", "*.log", "*.out", "*.run.xml", "*.bcf", "*.fls", "*.fdb_latexmk", "*.dvi"]
    for ext in exts:
        for file in glob.glob(ext):
            try:
                os.remove(file)
            except Exception:
                pass

def main():
    parser = argparse.ArgumentParser(description="Modular Resume Generator & Builder")
    parser.add_argument("--preview", action="store_true", help="Generate PNG preview images")
    parser.add_argument("--no-clean", action="store_true", help="Do not clean LaTeX auxiliary files")
    args = parser.parse_args()

    # Build both resumes
    build_pdf("main.tex")
    build_pdf("main_single_column.tex")

    if args.preview:
        generate_preview("main.pdf", "resume_page")
        generate_preview("main_single_column.pdf", "resume_page_single_column")

    if not args.no_clean:
        clean_temp_files()

    print("Done! Both resumes have been compiled.")

if __name__ == "__main__":
    main()
