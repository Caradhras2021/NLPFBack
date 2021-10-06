from models.transactionModels import getTransactionModel, transactionModel

def transactionService(filters):
    transactions = transactionModel(filters)
    return transactions
        
def getTransactionsService():
    transactions = getTransactionModel()
    return transactions