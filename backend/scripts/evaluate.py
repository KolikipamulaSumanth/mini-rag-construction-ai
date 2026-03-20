from app.services.rag_pipeline import RAGPipeline

SAMPLE_QUESTIONS = [
    "What factors affect construction project delays?",
    "What does the policy say about timelines?",
    "What responsibilities are assigned to vendors?",
]


if __name__ == "__main__":
    pipeline = RAGPipeline()
    for question in SAMPLE_QUESTIONS:
        response = pipeline.ask(question=question, top_k=4)
        print("=" * 80)
        print(f"Question: {question}")
        print(f"Answer: {response.answer}")
        print(f"Retrieved chunks: {len(response.retrieved_context)}")
