class UnstructuredPdfDocumentTableExtractorClient:
    def extract_tables(self, document_raw_text: str, output_format: str = "MARKDOWN") -> dict:
        table_md = "| Item | Qty | Unit Price | Total |\n|---|---|---|---|\n| Cloud Compute Units | 100 | $0.05 | $5.00 |\n| Storage GB-Mo | 500 | $0.02 | $10.00 |"
        records = [
            {"item": "Cloud Compute Units", "qty": 100, "unit_price": 0.05, "total": 5.00},
            {"item": "Storage GB-Mo", "qty": 500, "unit_price": 0.02, "total": 10.00}
        ]
        return {
            "extracted_tables_markdown": [table_md],
            "structured_records_json": records,
            "extraction_accuracy_pct": 99.4
        }
