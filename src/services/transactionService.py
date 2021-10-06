from models.transactionModels import Transaction, getTransactionModel, transactionModel

def transactionService(query, startIndex, blockSize):
    transactions = transactionModel(query, startIndex, blockSize)
    print(transactions)
    for doc in transactions:
        print(doc)



def getTransactionsService():
    transactions = getTransactionModel()
    

    return transactions