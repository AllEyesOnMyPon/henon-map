# Henon Map - Visual Representation

This repository contains an implementation of the Henon Map in Python using `matplotlib` and `numpy`. The Henon Map is a two-dimensional, discrete-time dynamical system that exhibits chaotic behavior. It is defined by the following set of equations:

- \( x_{n+1} = 1 - a \cdot x_n^2 + y_n \)
- \( y_{n+1} = b \cdot x_n \)

Where:
- \( x_0 \) and \( y_0 \) are the initial conditions,
- \( a \) and \( b \) are the parameters of the system,
- \( n \) is the iteration count.

## Parameters Used

The parameters used in this implementation are:

- \( a = 1.4 \)
- \( b = 0.3 \)
- Initial values: \( x_0 = 0 \), \( y_0 = 0 \)
- Number of iterations: 10,000

### Justification for Parameter Selection

- **Parameter \( a = 1.4 \)**: This value for \( a \) is commonly used in studies of the Henon Map as it ensures the system demonstrates chaotic behavior. When \( a \) is set to 1.4 and \( b \) to 0.3, the Henon Map shows a well-known chaotic attractor with a dense, scattered structure. The choice of \( a = 1.4 \) results in a system that is sensitive to initial conditions, a hallmark of chaotic systems.
  
- **Parameter \( b = 0.3 \)**: This value for \( b \) is also a standard choice that helps maintain the chaotic behavior while keeping the system's dynamics stable. It influences the scaling of the \( y \)-values in each iteration, and the chosen value ensures that the attractor's structure is distinct and visually interesting.

These parameters have been selected because they are widely used in the study of chaotic systems, particularly in the context of the Henon Map. They lead to a clearly observable chaotic attractor, which makes it easier to visualize the behavior of the system and study the properties of chaos.

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/AllEyesOnMyPon/henon-map.git
    cd henon-map
    ```

2. Make sure you have Python installed on your system. You can download Python from [here](https://www.python.org/downloads/).

3. Install the required dependencies:
    ```bash
    pip install matplotlib numpy
    ```

## Usage

1. Run the script `henon_map.py` to generate and display the Henon Map visualization:
    ```bash
    python henon_map.py
    ```

2. The script will generate a scatter plot displaying the Henon Map's chaotic behavior. The points are plotted with a low opacity to better illustrate the density of points as the system evolves over time.

## Visualization Details

- The plot displays the \( x_n \) values on the horizontal axis and the \( y_n \) values on the vertical axis.
- The grid is enabled with dashed lines to make it easier to interpret the plot.
- The x-axis and y-axis ranges are set to cover values typically found in the Henon Map's chaotic attractor, with \( x \) ranging from -1.5 to 1.5 and \( y \) from -0.5 to 0.5.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This implementation is based on the Henon Map's well-known equations. For further details on chaotic systems and the Henon Map, you can refer to related research papers and books on chaos theory.
