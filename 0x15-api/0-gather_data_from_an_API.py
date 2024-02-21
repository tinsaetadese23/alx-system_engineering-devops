#!/usr/bin/python3

import requests

def get_employee_todo_progress(employee_id):
    # Replace with the actual API endpoint
    api_url = "https://api.example.com/employee-todos"

    try:
        response = requests.get(f"{api_url}/{employee_id}")
        response_data = response.json()

        if response.status_code == 200:
            employee_name = response_data.get("employee_name")
            done_tasks = response_data.get("done_tasks")
            total_tasks = response_data.get("total_tasks")

            print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
            for task in response_data.get("completed_task_titles"):
                print(f"\t{task}")

        else:
            print(f"Error: Unable to fetch data for employee ID {employee_id}")

    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)

