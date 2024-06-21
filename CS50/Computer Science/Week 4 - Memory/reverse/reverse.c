#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    // Ensure proper usage
    // TODO #1
    if (argc != 3)
    {
        printf("Usage: ./reverse [flag] inwavfile outwavefile\n");
        return 1;
    }
    // Open input file for reading
    // TODO #2
    FILE *inputwavfile = fopen(argv[1], "r");
    if (inputwavfile == NULL)
    {
        printf("Failed to open file");
        return 1;
    }

    // Read header
    // TODO #3
    WAVHEADER header;
    fread(&header, sizeof(WAVHEADER), 1, inputwavfile);

    // Use check_format to ensure WAV format
    // TODO #4
    if (check_format(header) == 0)
    {
        printf("Not a WAV file\n");
        return 1;
    }

    // Open output file for writing
    // TODO #5
    FILE *outwavfile = fopen(argv[2], "w");
    if (outwavfile == NULL)
    {
        printf("Failed to open output file\n");
        return 1;
    }

    // Write header to file
    // TODO #6
    fwrite(&header, sizeof(WAVHEADER), 1, outwavfile);

    // Use get_block_size to calculate size of block
    // TODO #7
    int size = get_block_size(header);

    // Write reversed audio to file
    // TODO #8
    if (fseek(inputwavfile, size, SEEK_END))
    {
        return 1;
    }

    BYTE reverse[size];
    while (ftell(inputwavfile) - size > sizeof(header))
    {
        if (fseek(inputwavfile, -2 * size, SEEK_CUR))
        {
            return 1;
        }
        fread(reverse, size, 1, inputwavfile);
        fwrite(reverse, size, 1, outwavfile);
    }

    fclose(inputwavfile);
    fclose(outwavfile);
}

int check_format(WAVHEADER header)
{
    // TODO #4
    if (header.format[0] == 'W' && header.format[1] == 'A' && header.format[2] == 'V' && header.format[3] == 'E')
    {
        return 1;
    }
    return 0;
}

int get_block_size(WAVHEADER header)
{
    // TODO #7
    int size = (header.numChannels * header.bitsPerSample) / 8;
    return size;
}