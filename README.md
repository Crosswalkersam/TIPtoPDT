# TIPtoPDT
This script takes the .tip frames from satDump and converts them into a PDT-Telemetry-Explorer compatible format.

# Background
NOAA 15/18/19 transmit SEM-MEPED and HIRS data via a direct sounder broadcast (DSB) at 137MHz to the earth.
To demodulate and decode this data, [Project Desert Tortoise](https://github.com/nebarnix/Project-Desert-Tortoise) was created.
This data is not only transmitted via DSB, but is also part of the HRPT downstream on l-Band. 
The problem: Desert Tortoise cant handle HRPT. Thats why we use satdump to create a .tip file, which is then transformed into a .txt file using this script
and decoded using [PDT-Telemetry-Explorer](https://github.com/nebarnix/PDT-TelemetryExplorer).

# Installation
To run this script, you need to have python3 installed and added to PATH. After that, simply run `pip install tqdm`.

# Usage
To transcode TIP minorframes, simply drop the input file named `noaa_hrpt.tip` into the same directory as the script. 
Run the script and use PDT-Telemetry-Explorer to decode the created .txt file.
