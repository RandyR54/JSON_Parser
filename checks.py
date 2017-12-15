#!python3

# This file contains all the tests currently identified to validate
# the values associated with keys.

# Current rule(s) for objectCheck:
#     Single key/value pair, value is a string
def objectCheck(value):
    if isinstance(value, str):
        return(1)
    else:
        return(0)

# Current rule(s) for ipCheck:
#     Single key/value pair, value is a string
def ipCheck(value):
    if isinstance(value, str):
        return(1)
    else:
        return(0)

# Current rule(s) for idCheck:
#     Single key/value pair, value is a string
def idCheck(value):
    if isinstance(value, str):
        return(1)
    else:
        return(0)

# Current rule(s) for customerNameCheck:
#     Single key/value pair, value is a string
def customerNameCheck(value):
    if isinstance(value, str):
        return(1)
    else:
        return(0)

# Current rule(s) for customerEmailCheck:
#     Single key/value pair, value is a string
def customerEmailCheck(value):
    if isinstance(value, str):
        return(1)
    else:
        return(0)

# Current rule(s) for currencyCheck:
#     Single key/value pair, value is a string
def currencyCheck(value):
    if isinstance(value, str):
        return(1)
    else:
        return(0)

# Current rule(s) for sourceCheck:
#     Single key/value pair, value is a string
def sourceCheck(value):
    if isinstance(value, str):
        return(1)
    else:
        return(0)

# Current rule(s) for createdAtCheck:
#     Single key/value pair, value is a string
def createdAtCheck(value):
    if isinstance(value, str):
        return(1)
    else:
        return(0)

# Current rule(s) for updatedAtCheck:
#     Single key/value pair, value is a string
def updatedAtCheck(value):
    if isinstance(value, str):
        return(1)
    else:
        return(0)

# Current rule(s) for typeCheck:
#     Single key/value pair, value is a string
def typeCheck(value):
    if isinstance(value, str):
        return(1)
    else:
        return(0)

# Current rule(s) for guestStatusCheck:
#     Single key/value pair, value is a string
def guestStatusCheck(value):
    if isinstance(value, str):
        return(1)
    else:
        return(0)

# Current rule(s) for priceTypeCheck:
#     Single key/value pair, value is a string
def priceTypeCheck(value):
    if isinstance(value, str):
        return(1)
    else:
        return(0)

# Current rule(s) for arrivalCheck:
#     Single key/value pair, value is a string
def arrivalCheck(value):
    if isinstance(value, str):
        return(1)
    else:
        return(0)

# Current rule(s) for shortCodeCheck:
#     Single key/value pair, value is a string
def shortCodeCheck(value):
    if isinstance(value, str):
        return(1)
    else:
        return(0)

# Current rule(s) for phoneCheck:
#     Single key/value pair, value is a string
def phoneCheck(value):
    if isinstance(value, str):
        return (1)
    else:
        return (0)

# Current rule(s) for phoneCanonicalCheck:
#     Single key/value pair, value is a string
def phoneCanonicalCheck(value):
    if isinstance(value, str):
        return (1)
    else:
         return (0)

# Current rule(s) for experienceNameCheck:
#     Single key/value pair, value is a string
def experienceNameCheck(value):
    if isinstance(value, str):
        return(1)
    else:
        return(0)

# Current rule(s) for amountCheck:
#     Single key/value pair, value is a float or integer
def amountCheck(value):
    if isinstance(value, (float,int)):
        return(1)
    else:
        return(0)

# Current rule(s) for balanceCheck:
#     Single key/value pair, value is a float or integer
def balanceCheck(value):
    if isinstance(value, (float,int)):
        return(1)
    else:
        return(0)

# Current rule(s) for statusCheck:
#     Single key/value pair, value is a float or integer
def statusCheck(value):
    if isinstance(value, (float,int)):
        return(1)
    else:
        return(0)

# Current rule(s) for quantityCheck:
#     Single key/value pair, value is an integer
def quantityCheck(value):
    if isinstance(value, int):
        return(1)
    else:
        return(0)

# Current rule(s) for priceCheck:
#     Single key/value pair, value is a float or integer
def priceCheck(value):
    if isinstance(value, (float,int)):
        return(1)
    else:
        return(0)

# Current rule(s) for arrivalTimeCheck:
#     Single key/value pair, value is a float or integer
def arrivalTimeCheck(value):
    if isinstance(value, (float,int)):
        return(1)
    else:
        return(0)

# Current rule(s) for remindersCheck:
#     Single key, value is a dictionary with no nesting
def remindersCheck(value):
    if isinstance(value, dict):
        return(1)
    else:
        return(0)

# Current rule(s) for createdByCheck:
#     Single key, value is a dictionary with no nesting
def createdByCheck(value):
    if isinstance(value, dict):
        return(1)
    else:
        return(0)

# Current rule(s) for conversationCheck:
#     Single key, value is a dictionary with no nesting
def conversationCheck(value):
    if isinstance(value, dict):
        return(1)
    else:
        return(0)

# Current rule(s) for sellerCheck:
#     Single key, value is a dictionary with no nesting
def sellerCheck(value):
    if isinstance(value, dict):
        return(1)
    else:
        return(0)

# Current rule(s) for travelerCheck:
#     Single key, value is a dictionary with no nesting
def travelerCheck(value):
    if isinstance(value, dict):
        return(1)
    else:
        return(0)

# Current rule(s) for experienceCheck:
#     Single key, value is a dictionary with no nesting
def experienceCheck(value):
    if isinstance(value, dict):
        return(1)
    else:
        return(0)

# Current rule(s) for groupCheck:
#     Single key, value is a dictionary with no nesting
def groupCheck(value):
    if isinstance(value, dict):
        return(1)
    else:
        return(0)

# Current rule(s) for groupDiscountCheck:
#     Single key, value is a dictionary with no nesting
def groupDiscountCheck(value):
    if isinstance(value, dict):
        return(1)
    else:
        return(0)

# Current rule(s) for eventCheck:
#     Single key, value is a dictionary with no nesting
def eventCheck(value):
    if isinstance(value, dict):
        return(1)
    else:
        return(0)

# Current rule(s) for paymentRemindersCheck:
#     Single key, value is list containing a dictionary (maybe more than one)
def paymentRemindersCheck(value):
    if isinstance(value, list):
        return(1)
    else:
        return(0)

# Current rule(s) for notesCheck:
#     Single key, value is list containing a dictionary (maybe more than one), or maybe an empty list
def notesCheck(value):
    if isinstance(value, list):
        return(1)
    else:
        return(0)

# Current rule(s) for transactionsCheck:
#     Single key, value is list containing a dictionary (maybe more than one)
def transactionsCheck(value):
    if isinstance(value, list):
        return(1)
    else:
        return(0)

# Current rule(s) for metaCheck:
#
# def metaCheck(value):
#     if isinstance(value, list):
#         return(1)
#     else:
#         return(0)

# Current rule(s) for adjustmentsCheck:
#
# def adjustmentsCheck(value):
#     if isinstance(value, list):
#         return(1)
#     else:
#         return(0)

# Current rule(s) for tagsCheck:
#   Can be list of multiple dictionaries
def tagsCheck(value):
    if isinstance(value, list):
        return(1)
    else:
        return(0)

# Current rule(s) for demographicsCheck:
#
# def demographicsCheck(value):
#     if isinstance(value, list):
#         return(1)
#     else:
#         return(0)

# Current rule(s) for addOnsCheck:
#   Can abe list of multiple dictionaries
def addOnsCheck(value):
    if isinstance(value, list):
        return(1)
    else:
        return(0)

# Current rule(s) for guestsCheck:
#
def guestsCheck(value):
    if isinstance(value, list):
        return(1)
    else:
        return(0)

# Current rule(s) for guestsDataCheck:
#
def guestsDataCheck(value):
    if isinstance(value, list):
        return(1)
    else:
        return(0)

