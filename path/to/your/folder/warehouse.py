<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Warehouse Management System</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background-color: #f5f5f5;
      margin: 0;
      padding: 0;
    }

    .container {
      max-width: 800px;
      margin: 50px auto;
      padding: 30px;
      background-color: #fff;
      border-radius: 10px;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
    }

    h1 {
      text-align: center;
      color: #333;
    }

    .form-group {
      margin-bottom: 20px;
    }

    label {
      display: block;
      margin-bottom: 8px;
      font-weight: bold;
    }

    input, select {
      width: 100%;
      padding: 10px;
      font-size: 16px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }

    button {
      padding: 12px 20px;
      font-size: 16px;
      background-color: #4CAF50;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      transition: background-color 0.3s;
    }

    button:hover {
      background-color: #45a049;
    }

    .result {
      margin-top: 20px;
      padding: 15px;
      background-color: #e8f5e9;
      border: 1px solid #c8e6c9;
      border-radius: 5px;
    }

    .inventory {
      margin-top: 30px;
      background-color: #f9f9f9;
      padding: 20px;
      border-radius: 8px;
    }

    .inventory h2 {
      margin-top: 0;
    }

    .inventory ul {
      list-style-type: none;
      padding: 0;
    }

    .inventory li {
      margin-bottom: 10px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Warehouse Management System</h1>

    <div class="form-group">
      <label for="item">Item Name</label>
      <input type="text" id="item" placeholder="Enter item name" />
    </div>

    <div class="form-group">
      <label for="quantity">Quantity</label>
      <input type="number" id="quantity" placeholder="Enter quantity" />
    </div>

    <button onclick="addItem()">Add Item</button>
    <button onclick="removeItem()">Remove Item</button>
    <button onclick="viewInventory()">View Inventory</button>

    <div class="result" id="result"></div>

    <div class="inventory" id="inventory">
      <h2>Inventory</h2>
      <ul id="inventoryList"></ul>
    </div>
  </div>

  <script>
    let warehouse = {};

    function addItem() {
      const item = document.getElementById("item").value.trim();
      const quantity = parseInt(document.getElementById("quantity").value);

      if (!item || isNaN(quantity) || quantity <= 0) {
        showResult("Please enter a valid item name and quantity.");
        return;
      }

      if (warehouse[item]) {
        warehouse[item] += quantity;
      } else {
        warehouse[item] = quantity;
      }

      showResult(`${quantity} ${item}(s) added to the warehouse.`);
      clearInputs();
      updateInventory();
    }

    function removeItem() {
      const item = document.getElementById("item").value.trim();
      const quantity = parseInt(document.getElementById("quantity").value);

      if (!item || isNaN(quantity) || quantity <= 0) {
        showResult("Please enter a valid item name and quantity.");
        return;
      }

      if (warehouse[item] && warehouse[item] >= quantity) {
        warehouse[item] -= quantity;
        if (warehouse[item] === 0) {
          delete warehouse[item];
        }
        showResult(`${quantity} ${item}(s) removed from the warehouse.`);
      } else if (warehouse[item]) {
        showResult(`Insufficient stock for ${item}. Current stock: ${warehouse[item]}`);
      } else {
        showResult(`${item} not found in the warehouse.`);
      }

      clearInputs();
      updateInventory();
    }

    function viewInventory() {
      const inventoryList = document.getElementById("inventoryList");
      inventoryList.innerHTML = "";

      if (Object.keys(warehouse).length === 0) {
        inventoryList.innerHTML = "<li>Warehouse is empty.</li>";
        return;
      }

      for (const [item, quantity] of Object.entries(warehouse)) {
        const li = document.createElement("li");
        li.textContent = `${item}: ${quantity}`;
        inventoryList.appendChild(li);
      }
    }

    function showResult(message) {
      const resultDiv = document.getElementById("result");
      resultDiv.textContent = message;
    }

    function clearInputs() {
      document.getElementById("item").value = "";
      document.getElementById("quantity").value = "";
    }

    function updateInventory() {
      viewInventory();
    }
  </script>
</body>
</html>
