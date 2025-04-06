from src.pdf import load_pdf

if __name__ == '__main__':
    docs = load_pdf("./src/assets/nke-10k-2023.pdf")

    print(len(docs))
    print("")
    print(f"{docs[0].page_content[:200]}\n")
    print("")
    print(docs[0].metadata)
