class Meme:
    """
    Simple class for representation of memes, written for the sake of readability.
    """

    def __init__(self, label, weight, value):
        self.label = label
        self.weight = weight
        self.value = value

    def __repr__(self):
        return (
            "meme: "
            + self.label
            + "  weight:  "
            + str(self.weight)
            + "  value: "
            + str(self.value)
        )


def calculate(usb_size, memes):
    """
    Function for calculating max possible value of memes that can fit on a given usb_stick.
    Returns a tuple containing max possible value and set of memes' names/labels.
    Everything has been done in order to let xXxDankScavengerxXx earn his living.
    """

    # Just some basic tests at the start
    if memes is None or usb_size is None:
        raise TypeError("Memes or usb_size cannot be None")
    if not memes or usb_size == 0:
        return 0

    # Try to convert usb_size into int in order to accept strings as well
    try:
        max_weight = 1024 * int(usb_size)
    except ValueError:
        raise ValueError("Couldn't convert usb_size to int")

    # Check for correct data in memes
    for meme in memes:
        if not isinstance(meme, tuple):
            raise TypeError("Memes has to be a list of tuples")
        if len(meme) != 3:
            raise ValueError("Number of the values inside a tuple is wrong")
        if not isinstance(meme[0], str):
            raise TypeError("Name of a meme has to be a string")
        if not isinstance(meme[1], int):
            raise TypeError("Size of a meme has to be an int")
        if not isinstance(meme[2], int):
            raise TypeError("Price of a meme has to be an int")

    # Zip input for easier data manipulating
    items = list()
    items.append(Meme(label="", weight=0, value=0))  # Include no-item sub-problem
    for meme in memes:
        items.append(Meme(label=meme[0], weight=meme[1], value=meme[2]))

    # Create the [n+1, usb_size*1024 + 1] table and fill it with zeros
    rows = len(items)
    cols = max_weight + 1  # Include capacity = 0 sub-problem
    table = [[0] * cols for _ in range(rows)]  # Fill the table with zeros

    # Actual algorithm for a Knapsack 0-1 problem
    # Dynamic programming, bottom-up approach
    # Skips no-item and capacity = 0 sub-problems
    for i in range(1, rows):
        for j in range(1, cols):
            if j >= items[i].weight:  # If current max_capacity(j) can fit the i-th item
                # Check whether it's profitable to use i-th item.
                table[i][j] = max(
                    items[i].value + table[i - 1][j - items[i].weight], table[i - 1][j]
                )
            else:  # Otherwise, just use a solution to previous sub-problem
                table[i][j] = table[i - 1][j]

    # Retrieve wanted memes' labels
    labels = set()
    i = rows - 1
    j = cols - 1
    max_value = table[i][j]
    while table[i][j] != 0:
        # Find place where sub-problems' solutions differ
        if table[i - 1][j] == table[i][j]:
            i -= 1
        elif table[i][j - 1] == table[i][j]:
            j -= 1
        # And then add i-th item to the labels set
        else:
            labels.add(items[i].label)
            j -= items[i].weight
            i -= 1

    # Return a tuple consisting of max possible value and set of memes' names
    return max_value, labels
