import math
import cmath
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import time

def load_image_grayscale(image_path):
    # Load the image, resize to 28x28, and convert it to grayscale
    try:
        image = Image.open(image_path).convert('L').resize((28, 28))
        return np.array(image, dtype=float)
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        exit()

def fft_2d(image):
    """Compute the 2D FFT of an image manually."""
    M, N = image.shape
    fft_result = np.zeros((M, N), dtype=complex)

    for u in range(M):
        if u % 10 == 0:  # Debugging progress
            print(f"Processing row {u}/{M}")
        for v in range(N):
            sum_value = 0
            for x in range(M):
                for y in range(N):
                    angle = -2j * math.pi * ((u * x / M) + (v * y / N))
                    sum_value += image[x, y] * cmath.exp(angle)
            fft_result[u, v] = sum_value

    return fft_result

def magnitude_spectrum(fft_result):
    """Calculate the magnitude spectrum of the FFT result."""
    return np.log(1 + np.abs(fft_result))

def analyze_blurriness(image_path):
    # Step 1: Load image in grayscale
    print("Loading image...")
    image = load_image_grayscale(image_path)

    # Step 2: Compute the 2D FFT
    print("Computing FFT...")
    start_time = time.time()
    fft_result = fft_2d(image)
    print(f"FFT computation took {time.time() - start_time:.2f} seconds")

    # Step 3: Calculate the magnitude spectrum
    print("Calculating magnitude spectrum...")
    magnitude = magnitude_spectrum(fft_result)

    # Step 4: Analyze high-frequency components
    center_region = magnitude[magnitude.shape[0] // 4 : 3 * magnitude.shape[0] // 4,
                              magnitude.shape[1] // 4 : 3 * magnitude.shape[1] // 4]
    high_frequency_energy = np.sum(magnitude) - np.sum(center_region)
    total_energy = np.sum(magnitude)

    # Step 5: Compute blurriness metric
    blurriness = high_frequency_energy / total_energy

    return blurriness, magnitude

# Main script execution
if __name__ == "__main__":
    image_path = "/Users/mathew/Desktop/git py projects/grayscale_image.jpg"  # Replace with your image path
    print("Starting blur analysis...")

    blurriness, magnitude = analyze_blurriness(image_path)

    # Display results
    print(f"Blurriness metric: {blurriness}")
    plt.imshow(magnitude, cmap='gray')
    plt.title("Magnitude Spectrum")
    plt.colorbar()
    plt.show()

    if blurriness < 0.8:  # Define your threshold (tune as needed)
        print("The image is likely blurred.")
    else:
        print("The image is likely sharp.")
