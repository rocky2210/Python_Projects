def box(result):
    box_width = len(result) + 4  # Adjust the width based on the length of the result

    # Print the top line
    print('+' + '-' * box_width + '+')

    # Print the side line
    print('| ' + result + ' |')

    # Print the bottom line
    print('+' + '-' * box_width + '+')

result = "1"
box(result)