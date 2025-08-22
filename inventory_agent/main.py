from agents import Agent, function_tool

# Simple in-memory inventory store
inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 7
}

@function_tool
def check_stock(item: str) -> str:
    qty = inventory.get(item.lower(), 0)
    return f"{item} has {qty} units in stock."

@function_tool
def update_stock(item: str, delta: int) -> str:
    current_qty = inventory.get(item.lower(), 0)
    new_qty = max(current_qty + delta, 0)
    inventory[item.lower()] = new_qty
    return f"Updated {item} stock to {new_qty} units."

# Create specialized agents
catalog_agent = Agent(
    name="Catalog Agent",
    instructions="Handle inventory stock lookups like 'check stock for apple'.",
    tools=[check_stock]
)

update_agent = Agent(
    name="Update Agent",
    instructions="Handle inventory updates like 'add 5 bananas' or 'remove 2 oranges'.",
    tools=[update_stock]
)

# Main coordinator agent
coordinator_agent = Agent(
    name="Coordinator Agent",
    instructions="Route inventory-related commands to the correct agent.",
    handoffs=[catalog_agent, update_agent]
)
