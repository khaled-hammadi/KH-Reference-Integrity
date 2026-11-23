"""Command-line interface."""
import argparse
import json
from pathlib import Path
from .checker import validate_references

def main():
    parser = argparse.ArgumentParser(
        description="Run transparent first-pass checks on an academic reference list."
    )
    parser.add_argument("input", help="UTF-8 text file; one reference per line")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    parser.add_argument("--output", help="Optional output file")
    args = parser.parse_args()

    source = Path(args.input)
    references = source.read_text(encoding="utf-8").splitlines()
    report = validate_references(references)

    if args.format == "json":
        rendered = json.dumps(report, ensure_ascii=False, indent=2)
    else:
        lines = [
            f'{report["tool"]} v{report["version"]}',
            f'References checked: {report["reference_count"]}',
            f'Possible duplicate groups: {len(report["possible_duplicate_groups"])}',
            "-" * 60,
        ]
        for item in report["results"]:
            lines.append(
                f'[{item["index"]}] score={item["format_completeness_score"]}/100 '
                f'year={item["year_detected"] or "not detected"} '
                f'doi={item["doi_detected"] or "not detected"}'
            )
            if item["missing_indicators"]:
                lines.append("  Missing indicators: " + ", ".join(item["missing_indicators"]))
            if item["warnings"]:
                lines.append("  Warnings: " + ", ".join(item["warnings"]))
        lines.extend(["-" * 60, report["disclaimer"]])
        rendered = "\n".join(lines)

    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)

if __name__ == "__main__":
    main()
