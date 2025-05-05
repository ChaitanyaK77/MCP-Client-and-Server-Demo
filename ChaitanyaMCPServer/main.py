from mcp.server.fastmcp import FastMCP
from typing import List

# this is just a sample dummy data set which i created randomly
employee_travel_data = {
    '''you have employee id and their request for travel and city.... and approval given or not'''
    "E001": {"requests": ["2024-12-10 to 2024-12-15 - New York"], "approved": 1},
    "E002": {"requests": [], "approved": 0}
}

# I have created an MCP server here 
mcp = FastMCP("TravelDesk")

# Tool: Submit travel request ... this toll just submits a travel request 
@mcp.tool()
def submit_travel_request(employee_id: str, destination: str, start_date: str, end_date: str) -> str:
    """Submit a travel request with destination and date range...."""
    if employee_id not in employee_travel_data:
        return "Employee ID not found."

    request = f"{start_date} to {end_date} - {destination}"
    employee_travel_data[employee_id]["requests"].append(request)
    return f"Travel request submitted for {destination} from {start_date} to {end_date}."

# Tool: View travel request history....kind of like read,,
@mcp.tool()
def get_travel_history(employee_id: str) -> str:
    """Get submitted travel requests for the employee"""
    data = employee_travel_data.get(employee_id)
    if data:
        history = ', '.join(data["requests"]) if data["requests"] else "No travel requests submitted."
        return f"Travel history for {employee_id}: {history}"
    return "Employee ID not found."

# Tool: Count of approved trips....whether they r approvd or not
@mcp.tool()
def approved_trips_count(employee_id: str) -> str:
    """Get the number of approved trips"""
    data = employee_travel_data.get(employee_id)
    if data:
        return f"{employee_id} has {data['approved']} approved trip(s)."
    return "Employee ID not found."

# Resource: Time-pass greetings ;)
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Personalized greeting for travel desk"""
    return f"Hi {name}, welcome to the Travel Desk developed by MCP learner :)! Need help planning a work trip?"

if __name__ == "__main__":
    mcp.run()
