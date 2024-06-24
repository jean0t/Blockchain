from blockchain.blockchain import Blockchain
from blockchain.block import Block

from datetime import datetime

# Initialize the blockchain
blockchain = Blockchain()

blockchain.add_block(Block(1, datetime.now(), "Transaction 1", ""))
blockchain.add_block(Block(2, datetime.now(), "Transaction 2", ""))
blockchain.add_block(Block(3, datetime.now(), "Transaction 3", ""))


# Print its contents
for block in blockchain.chain:
	print(f"Block {str(block.index)}")
	print(f"Timestamp: {str(block.timestamp)}")
	print(f"Data: {str(block.data)}")
	print(f"Hash: {str(block.hash)}")
	print(f"Previous Hash: {str(block.previous_hash)}")
	print("\n")

