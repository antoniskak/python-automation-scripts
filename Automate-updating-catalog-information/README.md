# DESCRIPTION

## Part of a Project of Google IT Automation with Python Professional Certificate

### Qwiklabs Assessment: Automate updating catalog information

### Assignment Introduction
You work for an online fruits store, and you need to develop a system that will update the catalog information with data provided by your suppliers. The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description. The contents of the HTML file need to be uploaded to a web service that is already running using Django. You also need to gather the name and weight of all fruits from the .txt files and use a Python request to upload it to your Django server.

You will create a Python script that will process the images and descriptions and then update your company's online website to add the new products.

Once the task is complete, the supplier should be notified with an email that indicates the total weight of fruit (in lbs) that were uploaded. The email should have a PDF attached with the name of the fruit and its total weight (in lbs).

Finally, in parallel to the automation running, we want to check the health of the system and send an email if something goes wrong.

### Fetching Supplier Data
After downloading the supplier data `supplier-data.tar.gz` and extracting the contents of the compressed file a directory named `supplier-data` is created with two subdirectories named `images` and `descriptions`.
The subdirectory `images` contain images of various fruits, while the `descriptions` subdirectory has text files containing the description of each fruit.

### My python scripts:
**changeImage.py:**

Processes the supplier's images within the `/supplier-data/images` directory. Using the `PIL` library the script changes the images' resolution from 3000x2000 to 600x400 pixel and the format from .TIFF to .JPEG.

**supplier_image_upload.py:**

Takes the previously processed jpeg images and uploads them to the web server using the `requests` module.

**run.py:**

Adds fruit images and their descriptions from the supplier on the fruit catalog web-server. The script uses `POST` to automatically send the images and their respective description in JSON format. 
The files are written in the following format:
<li> name </li>
<li> weight (in lbs) </li>
<li> description </li>
<br>

**report.py:**

The `generate_report()` method builds a PDF report using the ReportLab PDF library.

**emails.py:**

The `generate_email` method generates an email using the smtplib module.

**report_email.py:**

Processes the text data from the `supplier-data/descriptions` directory and calls the `reports.generate_report` method passing the text description processed from the text files as the `paragraph` argument, the report title as the `title` argument, and the file path of the PDF to be generated as the `attachment argument` 
It then passes the arguments for the email template, generates the email with `emails.generate_email` method and sends the email.

**health_check.py:**

Runs in the background monitoring some of the system statistics: CPU usage, disk space, available memory and name resolution. Moreover, this Python script should send an email if there are problems, such as:
<li> Report an error if CPU usage is over 80% </li>
<li> Report an error if available disk space is lower than 20% </li>
<li> Report an error if available memory is less than 500MB </li>
<li> Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1" </li>
<br>

To test out my script I installed `stress` tool in order to impose high CPU Load:

`sudo apt install stress`

`stress --cpu 8`

When stress runs maximizes the CPU utilization and when running health_check.py in another SSH connection an  **"Error - CPU usage is over 80%"** email is automaticaly sent.
This can be automated by using a user cron job:

`crontab -e`

and setting up the complete path for `health_check.py` script.


