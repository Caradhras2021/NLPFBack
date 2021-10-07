from models.transactionModels import transactionModel

def transactionService(filters, pageNumber, pageSize):
    arrayFilters = []
    for key, value in filters.items():
        if (str(value) != ""):
            arrayFilters.append({key: value})
    transactions = transactionModel(arrayFilters, pageNumber, pageSize)
    return transactions
