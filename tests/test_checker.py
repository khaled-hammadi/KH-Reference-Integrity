import unittest
from kh_reference_integrity.checker import (
    extract_doi, normalize, validate_references
)

class CheckerTests(unittest.TestCase):
    def test_doi_extraction(self):
        self.assertEqual(
            extract_doi("See https://doi.org/10.1234/abc.def."),
            "10.1234/abc.def"
        )

    def test_normalization(self):
        self.assertEqual(normalize("  A   B "), normalize("a b"))

    def test_duplicate_detection(self):
        report = validate_references([
            "Smith, J. (2020). A useful title. Journal of Tests.",
            "Smith, J. (2020). A useful title. Journal of Tests."
        ])
        self.assertEqual(report["possible_duplicate_groups"], [[1, 2]])

    def test_empty_input(self):
        report = validate_references(["", "   "])
        self.assertEqual(report["reference_count"], 0)

if __name__ == "__main__":
    unittest.main()
