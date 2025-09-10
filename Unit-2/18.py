# Create a python function to accept python function as a
# dictionary and display its elements.

def display_dict_elements(input_dict):
    for key, value in input_dict.items():
        print(f"{key}: {value}")

# Example usage
sample_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

display_dict_elements(sample_dict)