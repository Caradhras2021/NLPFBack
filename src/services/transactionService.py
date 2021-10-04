from models.transactionModels import Transaction, getTransactionModel


def getTransactionService():
    transactions = getTransactionModel()
    

    return transactions