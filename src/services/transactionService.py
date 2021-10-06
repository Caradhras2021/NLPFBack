from models.transactionModels import getTransactionModel, transactionModel

def transactionService(filters):
    arrayFilters = []
    for key, value in filters.items():
        if (str(value) != ""):
            arrayFilters.append({key: value})
    transactions = transactionModel(arrayFilters)
    return transactions
        
def getTransactionsService():
    transactions = getTransactionModel()
    return transactions