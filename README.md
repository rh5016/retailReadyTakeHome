# Dick's Sporting Goods Requirements Assistant

This project is a tool designed to help warehouse workers follow the complex rules in the Dick's Sporting Goods Routing Guide to reduce chargebacks.

## Project Goal

The goal is to automate one of the many decision points for warehouse workers. I chose to focus on two areas:

1.  **Product Preparation:** Ensuring "Apparel on Hangers" meets the specific VAS (Value-Added Services) requirements.
2.  **Shipment Routing:** Determining the correct shipment method (Parcel vs. LTL).

I used **Section 5.3 (Hanging Requirements)**, **Section 14 (Domestic Transportation)**, and **Exhibit F (Hanger Chart)** of the DSG Routing Guide.

## How It Works

We use a simple two-step logical flow:

### 1. The Preparation Engine (`get_prep_instructions`)

This function looks up the apparel. It takes product details as input and returns a set of instructions based on the rules in Exhibit F.

-   **Input:** `{ "product_type": "Fleece Bottoms", "category": "WOMENS", "size": "M" }`
-   **Output:** `{ "hanger_code": 6010, "presentation": "CLOSED", "sizer_required": TRUE, "special_note": "None" }`

### 2. The Shipping Engine (`shipping_method`)

This function analyzes a complete weekly shipment for a one destination. It calculates the total billable weight and carton count to decide if the shipment is through Parcel LTL.

-   **Input:** A list of all cartons in the shipment.
-   **Output:** An instruction.

## How to Run the Project

1.  Clone the repository: `git clone ...`
2.  Install dependencies: `npm install` (or `pip install -r requirements.txt`)
3.  Run the main application: `node index.js` (or `python main.py`)
4.  (Optional) Run tests: `npm test` (or `pytest`)

## Future Work

* **Expand the Rule Set:** Incorporate logic for other product categories and shipping rules (e.g., carton labeling, palletization).
* **API-first Design:** Expose the logic via a simple REST API for easy integration with other warehouse management systems.
* **AI-Powered Parsing:** Develop a module to automatically parse updated routing guide PDFs, identify rule changes, and suggest updates to the logic engine, making the system more scalable and maintainable.