from pyscript import document

def create_order(event):
    # Get customer info
    name = document.getElementById("name").value
    address = document.getElementById("address").value
    contact = document.getElementById("contact").value
    
    # Check if fields are empty
    if not name or not address or not contact:
        document.getElementById("orderOutput").innerHTML = '<span class="error">ERROR: Please fill in all customer details</span>'
        return
    
    # Menu items
    items = [
        {"id": "burger", "name": "Burger", "price": 120},
        {"id": "pizza", "name": "Pizza", "price": 250},
        {"id": "fries", "name": "Fries", "price": 80},
        {"id": "soda", "name": "Soda", "price": 50},
        {"id": "icecream", "name": "Ice Cream", "price": 90}
    ]
    
    # Calculate total
    total = 0
    selected_items = []
    
    for item in items:
        checkbox = document.getElementById(item["id"])
        if checkbox.checked:
            total += item["price"]
            selected_items.append(item["name"])
    
    # Check if no items selected
    if not selected_items:
        document.getElementById("orderOutput").innerHTML = '<span class="error">ERROR: Please select at least one menu item</span>'
        return
    
    # Create order summary
    summary = f"""
    Order for: {name}
    Address: {address}
    Contact: {contact}
    
    Items ordered:
    """
    
    for item in selected_items:
        summary += f"- {item}\n"
    
    summary += f"\nTotal: ₱{total}"
    
    # Show result
    document.getElementById("orderOutput").innerText = summary
