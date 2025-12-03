def calculate_reciprocal_rank(retrieved_docs, relevant_docs):
    """
    Calculates the Reciprocal Rank (RR) for a single query.
    This is the inverse of the rank of the *first* correct document.
    """
    retrieved_ids = [doc_id for doc_id, score in retrieved_docs]
    for rank, doc_id in enumerate(retrieved_ids, 1):
        if doc_id in relevant_docs:
            return 1.0 / rank
    return 0.0  # No relevant document was found

def calculate_precision_at_k(retrieved_docs, relevant_docs, k):
    """
    Calculates Precision@k.
    P@k = (Number of relevant docs in top-k) / k
    """
    if k == 0:
        return 0.0
        
    retrieved_ids_at_k = [doc_id for doc_id, score in retrieved_docs[:k]]
    relevant_found = 0
    for doc_id in retrieved_ids_at_k:
        if doc_id in relevant_docs:
            relevant_found += 1
    
    return relevant_found / k

def calculate_average_metric(evaluation_results, metric_name):
    """Calculates the average of any metric stored in the results dict."""
    total_metric = sum(result[metric_name] for result in evaluation_results.values())
    return total_metric / len(evaluation_results)
