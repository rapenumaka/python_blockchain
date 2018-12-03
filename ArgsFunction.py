blockchain =[[1]]



# block chain model

# add_blockvalue() taking the argument transactionAmount

def add_blockvalue(transactionAmount):
    blockchain.append([blockchain[-1], transactionAmount])
    print(blockchain)

p = True

add_blockvalue(3.23)
add_blockvalue(4.23)
add_blockvalue(6.73)
add_blockvalue(3.38)
add_blockvalue('arvind')
add_blockvalue(p)


