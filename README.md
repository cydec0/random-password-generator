# Password Generator

Generates random passwords with customizable length and character sets.

## Features

* Customizable Length
* Character Set Selection
* Error Handling

## How to Use

1.  Run script.
2.  Enter length.
3.  Choose sets (y/n).
4.  View password.
   
## Code

### `generate_password()`

* Generates password.
* Parameters: `length`, `use_digits`, `use_special_chars`.
* Uses `random.choice()`.
* Raises `ValueError` if no set is selected.

### `main()`

* Main function.
* Prompts user.
* Calls `generate_password()`.
* Prints output.

## Requirements

* Python 3.x
