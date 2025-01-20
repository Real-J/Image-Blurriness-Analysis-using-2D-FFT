# Image Blurriness Analysis using 2D FFT

This Python project analyzes the blurriness of an image by calculating the high-frequency components using the 2D Fast Fourier Transform (FFT). The blurriness metric is determined by comparing the energy of high-frequency components to the total energy of the image's frequency spectrum.

## Features
- **2D FFT Implementation**: Computes the 2D FFT manually for the input image.
- **Blurriness Metric**: Quantifies the image's blurriness based on its frequency spectrum.
- **Visualization**: Displays the magnitude spectrum of the image's FFT.

## Prerequisites
To run this project, ensure you have Python installed along with the following libraries:

- `math`
- `cmath`
- `matplotlib`
- `Pillow` (PIL)
- `numpy`

You can install the necessary packages using pip:

```bash
pip install matplotlib pillow numpy
```

## Usage

### 1. Clone the Repository


### 2. Add Your Image
Place the grayscale image you want to analyze in the project directory. Update the `image_path` variable in the script with the path to your image file.

```python
image_path = "path/to/your/image.jpg"  # Replace with your image path
```

### 3. Run the Script
Execute the script using Python:

```bash
python analyze_blur.py
```

### 4. View Results
- **Blurriness Metric**: The script prints the blurriness metric to the console.
- **Blur Analysis**: A threshold determines whether the image is likely blurred or sharp.
- **Magnitude Spectrum Visualization**: The script displays the magnitude spectrum of the image's FFT.

## Example Output
```plaintext
Starting blur analysis...
Loading image...
Computing FFT...
Processing row 0/28
Processing row 10/28
Processing row 20/28
FFT computation took 12.34 seconds
Calculating magnitude spectrum...
Blurriness metric: 0.65
The image is likely blurred.
```

## Threshold Tuning
You can adjust the blurriness threshold in the script to better suit your application:

```python
if blurriness < 0.8:  # Tune this threshold as needed
    print("The image is likely blurred.")
else:
    print("The image is likely sharp.")
```

## Notes
- The script resizes all images to 28x28 pixels for FFT processing.
- Ensure the input image is grayscale. If not, the script converts it to grayscale automatically.
- The manual computation of 2D FFT is computationally intensive for large images; consider using optimized libraries like `numpy.fft` for larger datasets.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---
Feel free to contribute to this project by submitting issues or pull requests!

