from models.transactionModels import transactionModel, logsModel, getLogsModel

def logsService(firstname, lastname, emailAddress):
    return logsModel(firstname, lastname, emailAddress)

def getLogsService():
    return getLogsModel()

def transactionServiceSurface(filters, pageNumber, pageSize):
    arrayFilters = []
    for key, value in filters.items():
        if (str(value) != ""):
            arrayFilters.append({key: value})
    transactions = transactionModel(arrayFilters, pageNumber, pageSize)
    return transactions

def transactionService(filters, pageNumber, pageSize):
    arrayFilters = []
    surface = -1
    for key, value in filters.items():
        if (str(key) == "lot1_surface_carrez" and str(value) != ""):
            surface = value
            continue
        if (str(value) != ""):
            arrayFilters.append({key: value})

    transactions = transactionModel(arrayFilters, surface, pageNumber, pageSize)

    return transactions
