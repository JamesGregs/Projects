#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Take average to determine shade of grey
            float b = image[i][j].rgbtBlue;
            float g = image[i][j].rgbtGreen;
            float r = image[i][j].rgbtRed;
            int average = round((b + g + r) / 3);

            // Set all three components to the average value
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtRed = average;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width/2; j++)
        {
            // Swap pixel end to end
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - j -1];
            image[i][width - j - 1] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Initialize sum and pixel variables
            int sumblue, sumgreen, sumred;
            sumblue = sumgreen = sumred = 0;
            float pixelCount = 0.00;

            for (int di = -1; di < 2; di++)
            {
                for (int dj = -1; dj < 2; dj++)
                {
                    int ni = i + di;
                    int nj = j + dj;
                    // Check if the neighboring pixel is within boundary
                    if (ni < 0 || ni > (height -1) || nj < 0 || nj > (width - 1))
                    {
                        continue;
                    }
                        // Accumulate the neighboring pixel values
                        sumred += image[ni][nj].rgbtRed;
                        sumgreen += image[ni][nj].rgbtGreen;
                        sumblue += image[ni][nj].rgbtBlue;
                        pixelCount++;
                }
            }

            // Calculate the average color value for the pixel
            temp[i][j].rgbtRed = round(sumred / pixelCount);
            temp[i][j].rgbtGreen = round(sumgreen / pixelCount);
            temp[i][j].rgbtBlue = round(sumblue / pixelCount);
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = temp[i][j].rgbtRed;
            image[i][j].rgbtGreen = temp[i][j].rgbtGreen;
            image[i][j].rgbtBlue = temp[i][j].rgbtBlue;
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    // Using Sobel Operator Algorithm
    RGBTRIPLE temp[height][width];
    int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int Gy[3][3] = {{-1, -2, -1}, {0, 0 ,0}, {1, 2, 1}};
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int greenx = 0;
            int redx = 0;
            int bluex = 0;
            int greeny = 0;
            int redy = 0;
            int bluey = 0;
            for (int di = 0; di < 3; di++)
            {
                for (int dj = 0; dj < 3; dj++)
                {
                    // Chech if pixels are valid if not skip the pixel
                    if (i - 1 + di < 0 || i - 1 + di > height - 1 || j - 1 + dj < 0 || j - 1 + dj > width - 1)
                    {
                        continue;
                    }
                    // Calculate Gx
                    greenx = greenx + (image[i - 1 + di][j - 1 + dj].rgbtGreen * Gx[di][dj]);
                    redx = redx + (image[i - 1 + di][j - 1 + dj].rgbtRed * Gx[di][dj]);
                    bluex = bluex + (image[i - 1 + di][j - 1 + dj].rgbtBlue * Gx[di][dj]);

                    // Calculate Gy
                    greeny = greeny + (image[i - 1 + di][j - 1 + dj].rgbtGreen * Gy[di][dj]);
                    redy = redy + (image[i - 1 + di][j - 1 + dj].rgbtRed * Gy[di][dj]);
                    bluey = bluey + (image[i - 1 + di][j - 1 + dj].rgbtBlue * Gy[di][dj]);
                }
            }
            // Calculate sq root Gx^2 + Gy^2
            int green = round(sqrt(pow(greenx, 2) + pow(greeny, 2)));
            int red = round(sqrt(pow(redx, 2) + pow(redy, 2)));
            int blue = round(sqrt(pow(bluex, 2) + pow(bluey, 2)));

            // Max value must be 255
            if (green > 255)
            {
                green = 255;
            }
            if (red > 255)
            {
                red = 255;
            }
            if (blue > 255)
            {
                blue = 255;
            }

            // Copy to temp
            temp[i][j].rgbtGreen = green;
            temp[i][j].rgbtRed = red;
            temp[i][j].rgbtBlue = blue;
        }
    }
    // Copy to actual image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtGreen = temp[i][j].rgbtGreen;
            image[i][j].rgbtRed = temp[i][j].rgbtRed;
            image[i][j].rgbtBlue = temp[i][j].rgbtBlue;
        }
    }
    return;
}
