def read_and_write_file(input_file, output_file):
    try:
        # Reading from the  file
        with open(input_file, 'r') as file:
            data = file.read()

        # Processing the data (you can add your own logic here)
        processed_data = data.upper()

        # Writing to the output file
        with open(output_file, 'w') as file:
            file.write(processed_data)

        print(f"File '{input_file}' processed and saved as '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    input_file_path = "expl.txt"
    output_file_path = "output.txt"

    read_and_write_file(input_file_path, output_file_path)
