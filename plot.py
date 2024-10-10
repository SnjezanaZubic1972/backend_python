import matplotlib.pyplot as plt

# Data for the blockchain
block_indices = [0, 1, 2, 3]
timestamps = [
    "2024-09-16 18:53:07.193901",
    "2024-09-16 18:53:07.193981",
    "2024-09-16 18:53:07.194045",
    "2024-09-16 18:53:07.194105"
]
data = [
    "Genesis Block",
    "Transaction Data 1",
    "Transaction Data 2",
    "Transaction Data 3"
]
hashes = [
    "036b40ed767cca54606f0e08ac69a41b7f1618db11b52d966a502e30a1f66b75",
    "4db21a636dd0add911549f67b9822de4203f7ae7d31bbc01d9ac513c8c15a527",
    "dc0ee25255ca7bae56f56202d53d5439e4b406b28f58eab20042efb8accbeda5",
    "c0522064b11d085b6a875215482de0975f370df504497bfb1c3e4ed14f3930ad"
]
# Create a figure and axis
plt.figure(figsize=(12, 6))

# Create a bar chart for block indices
plt.bar(block_indices, range(len(block_indices)), color='skyblue')

# Adding titles and labels
plt.title('Blockchain Visualization')
plt.xlabel('Block Index')
plt.ylabel('Block Height')

# Adding block details as text on the bars
for i in range(len(block_indices)):
    plt.text(block_indices[i], i, f'Block #{block_indices[i]}\n'
                                   f'Timestamp: {timestamps[i]}\n'
                                   f'Data: {data[i]}\n'
                                   f'Hash: {hashes[i]}\n'
                                   f'Previous Hash: {hashes[i-1] if i > 0 else "0"}',
             ha='center', va='bottom', fontsize=8, bbox=dict(facecolor='white', alpha=0.5))

# Customizing x-axis ticks
plt.xticks(block_indices)

# Adding a grid
plt.grid(axis='y')

# Show the plot
plt.tight_layout()
plt.show()