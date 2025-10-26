@echo off
echo ================================================
echo Deep Learning Assignment - PDF Submission Generator
echo ================================================
echo.

echo Installing required dependencies...
pip install reportlab

echo.
echo Generating PDF submission...
python generate_submission_pdf.py

echo.
echo ================================================
echo PDF submission generated successfully!
echo Check the current directory for the PDF file.
echo ================================================
pause
