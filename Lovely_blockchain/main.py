from datetime import datetime
from blockchain_classes.blockchain_class import Blockchain
from blockchain_classes.block_class import Block
from blockchain_classes.vote_system_account import VotingSystemAccount
from blockchain_classes.account_class import Account

START_DATE = datetime(2021, 9, 1)


if __name__ == "__main__":
    step = 1

    # Initializes the blockchain
    print(f"Step{step}. Initializes the blockchain:")
    step += 1
    blockchain = Blockchain()
    blockchain.print()

    # Create students accounts
    print("-" * 50)
    print("\nCreates accounts of students and voting system:")
    student1 = Account(123, "Andrii", "Tsemko", START_DATE)
    print(f"Student1 account: {student1.account_id}")
    student2 = Account(124, "Yaroslav", "Berko", START_DATE)
    print(f"Student2 account: {student2.account_id}")

    # Create Vote System Account
    vote_system_acc = VotingSystemAccount(1, "Head os student government")
    print(f"Vote System Account: {vote_system_acc.account_id}\n\n")
    print("Creates a voting tickets for specified students:")
    transactions = vote_system_acc.create_transaction_for_voting([student1.account_id, student2.account_id])
    for tx in transactions:
        print(tx)

    print("-" * 50)
    print(f"\n\nStep{step}. Created new block with added transaction of creating voting tickets for two students accounts:")
    step += 1
    block = Block(transactions, blockchain.get_blockHistory()[-1].block_id)

    try:
        blockchain.validate_block(block)
    except Exception as ex:
        print("\n\nERROR!!!")
        print(ex)
        print("BLOCK WAS NOT ADDED!\n")

    blockchain.print()

    print("-" * 50)
    print(f"\nStep{step}. Students votes:")
    step += 1
    print("\nVoting tickets (each student have tickets):")
    print(
        f"Student1 has next voting_tickets: [{', '.join([str(tx.transaction_id) for tx in student1.get_voting_tickets(blockchain)])}]")
    print(
        f"Student2 has next voting_tickets: [{', '.join([str(tx.transaction_id) for tx in student2.get_voting_tickets(blockchain)])}]")

    print("\nLet's try to spent voting ticket of student1 by student2 and vice verse")
    # Students voting:
    tx1 = student1.create_vote_transaction(student2.get_voting_tickets(blockchain)[-1]  # confused spending voting tickt
                                           .transaction_id,             # Get last tx of voting ticket
                                           vote_system_acc.account_id,  # Get id of voting system
                                           1                            # Vote for 1'st person
                                           )
    print(tx1)
    tx2 = student2.create_vote_transaction(student1.get_voting_tickets(blockchain)[-1]  # confused spending voting tickt
                                           .transaction_id,             # Get last tx of voting ticket
                                           vote_system_acc.account_id,  # Get id of voting system
                                           2                            # Vote for 1'st person
                                           )
    print(tx2)

    print("-" * 50)
    print(f"\n\nStep{step}. Try to create a new block with confused spent voting tickets.")
    step += 1
    voted_block = Block({tx1, tx2}, blockchain.get_blockHistory()[-1].block_id)

    try:
        blockchain.validate_block(voted_block)
    except Exception as ex:
        print("\n\nERROR!!!")
        print(ex)
        print("BLOCK WAS NOT ADDED!\n")

    print("Student1 cannot spent student2 voting ticket, so block wasnot added.")
    blockchain.print()

    print("\nLet's try to create correct votes.")
    # Students voting:
    tx1 = student1.create_vote_transaction(student1.get_voting_tickets(blockchain)[-1]
                                           .transaction_id,  # Get last tx of voting ticket
                                           vote_system_acc.account_id,  # Get id of voting system
                                           1  # Vote for 1'st person
                                           )
    print(tx1)
    tx2 = student2.create_vote_transaction(student2.get_voting_tickets(blockchain)[-1]
                                           .transaction_id,  # Get last tx of voting ticket
                                           vote_system_acc.account_id,  # Get id of voting system
                                           2  # Vote for 1'st person
                                           )
    print(tx2)

    print("-" * 50)
    print(f"\n\nStep{step}. Created new block with spent votes by students:")
    step += 1
    voted_block = Block({tx1, tx2}, blockchain.get_blockHistory()[-1].block_id)

    try:
        blockchain.validate_block(voted_block)
    except Exception as ex:
        print("\n\nERROR!!!")
        print(ex)
        print("BLOCK WAS NOT ADDED!\n")

    blockchain.print()

    print("\nVoting tickets (Now students does not have voting tickets):")
    print(
        f"Student1 has next voting_tickets: [{', '.join([str(tx.transaction_id) for tx in student1.get_voting_tickets(blockchain)])}]")
    print(
        f"Student2 has next voting_tickets: [{', '.join([str(tx.transaction_id) for tx in student2.get_voting_tickets(blockchain)])}]")

    print("-" * 50)
    print(f"\n\nStep{step}. Let's create a new parallel vote system and tries to spent a voting ticket of it on previous"
          f" vote system:")
    step += 1

    # Create Vote System Account
    vote_system_acc2 = VotingSystemAccount(2, "General Secretary")
    print(f"Vote System Account: {vote_system_acc2.account_id}\n\n")
    print("Creates a voting tickets for specified students for VoteSystem2:")
    transactions2 = vote_system_acc2.create_transaction_for_voting([student1.account_id])
    for tx in transactions2:
        print(tx)
    print("Creates a voting tickets for specified students for VoteSystem1:")
    transactions1 = vote_system_acc.create_transaction_for_voting([student1.account_id])
    for tx in transactions1:
        print(tx)

    print("Created new block with added transaction of creating voting tickets for two students accounts "
          "by two vote systems")
    block = Block({*transactions1, *transactions2}, blockchain.get_blockHistory()[-1].block_id)

    try:
        blockchain.validate_block(block)
    except Exception as ex:
        print("\n\nERROR!!!")
        print(ex)
        print("BLOCK WAS NOT ADDED!\n")

    blockchain.print()

    print("-" * 50)
    print(f"\n\nStep{step}. Let's try to spent a voting ticket from VoteSystem1 for VoteSystem2")
    step += 1

    # Students voting:
    tx1 = student1.create_vote_transaction(list(transactions2)[0].transaction_id,  # Get voting ticket from VoteSys2
                                           vote_system_acc.account_id,             # Get id of VoteSys1
                                           3  # Vote for 1'st person
                                           )
    print(tx1)

    print("-" * 50)
    print(f"\n\nStep{step}. Let's try to add this transaction to blockchain:")
    step += 1
    voted_block = Block({tx1}, blockchain.get_blockHistory()[-1].block_id)

    try:
        blockchain.validate_block(voted_block)
    except Exception as ex:
        print("\n\nERROR!!!")
        print(ex)
        print("BLOCK WAS NOT ADDED!\n")

    print("Student cannot spent his voting ticket from VoteSystem1 for VoteSystem2 and vice verse.")
    blockchain.print()

    print("-" * 50)
    print(f"\n\nStep{step}. Let's print results of voting of VoteSystem1:")
    step += 1
    for tx in vote_system_acc.get_results_of_voting(blockchain):
        print(tx)
