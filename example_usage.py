from client import UnstructuredPdfDocumentTableExtractorClient

def main():
    client = UnstructuredPdfDocumentTableExtractorClient()
    doc = "INVOICE #8921\nCloud Compute Units 100 $0.05 $5.00\nStorage GB-Mo 500 $0.02 $10.00"
    res = client.extract_tables(doc)
    print(f"Accuracy: {res['extraction_accuracy_pct']}%")
    print("Structured Records:", res["structured_records_json"])
    print("\nMarkdown Table:")
    print(res["extracted_tables_markdown"][0])

if __name__ == "__main__":
    main()
