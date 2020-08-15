## About

This is a collection of scripts for analyzing SSH logs and generating statistics.

## Example

The following plot shows what usernames are commonly being used to attempt breaking into a machine over SSH.
The data was collected over a period of four months on a personal server.

!(Most frequent names)[https://i.imgur.com/bI50cSm.png]

## Dependencies

For the Bash scripts, you will need [ripgrep](https://github.com/BurntSushi/ripgrep).
The Python scripts use [Matplotlib](https://matplotlib.org/) and [NumPy](https://numpy.org/).
