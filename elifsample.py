import sys
blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]

def add_value(transaction_amount, last_trasaction = [1]):
    """Append a new value and a last blockchain value to the blockchain
      :transaction_amount : The amount should be added
      :last_transaction: the last blockchain transaction(default [1])
    """
    blockchain.append([last_trasaction,transaction_amount])

def get_user_input():
    user_input = float(input('Your transaction amount please : '))
    return user_input

# Get the first transaction input and add the value to the blockchain

blockchain.append([1])

"""
tx_amount = get_user_input()
add_value(tx_amount)
"""

# Get the second transaction input and add the value to the blochchain
"""
tx_amount = get_user_input()
add_value(last_trasaction=get_last_blockchain_value(), transaction_amount=tx_amount)


# Get the third transaction input and add the value to the blockchain

tx_amount = get_user_input()
add_value(tx_amount,get_last_blockchain_value())
"""
# Output the blockchain list to the console
print(blockchain)




def print_blocks():
    for blocks in blockchain:
        print('Outputting blocks')
        print(blocks)

# While loop
# this is an infinite loop
while True:
    print("Choose the following options [1],[2],[3]")
    print("1 - Add transaction amount to blockchain")
    print("2 - Print the blockchain")
    print("3 - Exit the program")

    input_token = input()

    if input_token == '1':
      tx_amount = get_user_input()
      add_value(tx_amount, get_last_blockchain_value())

    elif input_token == '2':
      print_blocks()

    elif input_token == '3':
      sys.exit(0)

    else:
        print("Enter was invalid please select - 1 | 2 | 3")

    # Outputting the blockchain list to the console



print('Done')
